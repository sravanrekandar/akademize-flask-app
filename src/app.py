"""Flask App."""
import json
import uuid
from flask import Flask
from flask_restx import Api, Resource
from flask_restx import reqparse
from heros import get_heros, set_heros

app = Flask(__name__)
api = Api(app)


@api.route("/")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


@api.route("/heros")
class Heros(Resource):
    def get(self):
        heros = get_heros()["data"]
        return {"success": True, "data": heros}


hero_create_request_parser = reqparse.RequestParser()
hero_create_request_parser.add_argument(
    "name",
    type=str,
    location="json",
    required=True,
)
hero_create_request_parser.add_argument(
    "alter_ego",
    type=str,
    location="json",
    required=True,
)


@api.route("/create-hero")
class CreateHero(Resource):
    @api.expect(hero_create_request_parser)
    def post(self):
        heros = get_heros()["data"]
        new_hero = None
        try:
            args = hero_create_request_parser.parse_args()
            name = args.get("name")
            alter_ego = args.get("alter_ego")
            new_hero = {"id": str(uuid.uuid4()), "name": name, "alter_ego": alter_ego}
            heros.append(new_hero)
            set_heros(heros)
        except BaseException as err:
            return {"success": False, "message": str(err)}

        return {
            "success": True,
            "data": new_hero,
        }


@api.route("/hero/<string:id>")
class Hero(Resource):
    def get(self, id):
        heros = get_heros()["data"]
        my_hero = None
        for hero in heros:
            if hero["id"] == id:
                my_hero = hero
                break

        if my_hero is None:
            return {
                "success": False,
                "message": f"Hero with id {id} not found in our records.",
            }

        return {"success": True, "data": my_hero}


@api.route("/delete-hero/<string:id>")
class DeleteHero(Resource):
    def post(self, id):
        heros = get_heros()["data"]

        my_hero = None
        for hero in heros:
            if hero["id"] == id:
                my_hero = hero
                break

        if my_hero is None:
            return {
                "success": False,
                "message": f"Hero with id {id} not found in our records.",
            }

        heros.remove(my_hero)
        set_heros(heros)

        return {
            "success": True,
            "message": "The requested here is removed successfully.",
        }


@api.route("/search-hero/<string:search_string>")
class SearchHero(Resource):
    def get(self, search_string):
        heros = get_heros()["data"]
        filtered_heros = []
        l_search_string = search_string.lower()
        for hero in heros:
            if (hero["name"].lower().find(l_search_string) != -1) or (
                (hero["alter_ego"].lower().find(l_search_string) != -1)
            ):
                filtered_heros.append(hero)
        return {
            "success": True,
            "data": {
                "message": f"Heros matching the search criteria {search_string}",
                "heros": filtered_heros,
            },
        }
