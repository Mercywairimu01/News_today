from flask import Blueprint

main = Blueprint('main',__name__)
from . import error
from . import views
