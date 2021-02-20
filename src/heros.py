import json


def get_heros():
    heros = []
    with open("src/data/heros.json", "r") as f:
        heros = json.loads(f.read())
    return {"success": True, "data": heros}


def set_heros(heros):
    with open("src/data/heros.json", "w") as f:
        f.write(json.dumps(heros))
    return {"success": True, "message": "Heros list updated successfully."}
