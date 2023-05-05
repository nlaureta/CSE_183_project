from py4web import action, request, abort, redirect, URL
from .common import db, session, T, cache, auth, logger
from .models import get_user_email
from .settings import APP_FOLDER
import os, json

@action('index')
@action.uses('index.html', auth)
def index():
    filename = os.path.join(APP_FOLDER, "data", "table.json")
    f = open(filename)
    data = json.load(f)
    return dict(data=data)
