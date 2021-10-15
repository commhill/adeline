"""
Entry point for Flask
"""

from flask import Flask

app: Flask = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    """
    Just a demo endpoint
    """
    return "<p>Hello, World!</p>"


def main() -> None:
    app.run()
