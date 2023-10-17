from flask import render_template
from app.home import homeBp

@homeBp.route("", strict_slashes = False)
def index():
    return render_template("/index.html")