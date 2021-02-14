"""Flask App."""
from flask import Flask

app = Flask(__name__)

header_html = """
<p>
    <a href="/">Home</a>
    <a href="/contact">Contact</a>
    <a href="/dynamic/Sravan">Message</a>
</p>
"""


@app.route("/")
def hello():
    """Hello."""
    return f"""
        {header_html}
        <div>
            <h1>My First Flask App!</h1>
            <p>Started today</p>
        <div>
    """


@app.route("/contact")
def contact():
    """Contact View."""
    return f"""
        {header_html}
        <div>
            <h1>Contact!</h1>
            <p>
                Phone XXX
                <br>
                Address XXX
                XXXX
                XXXXX
            </p>
        <div>
    """


@app.route("/dynamic/<name>")
def dynamic_content(name):
    """Content."""
    return f"""
        {header_html}
        <p>Hello {name}</p>
    """


if __name__ == "__main__":
    app.run()
