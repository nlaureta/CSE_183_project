from py4web import action, request, abort, redirect, URL
from .common import db, session, T, cache, auth, logger
from .models import get_user_email
from .settings import APP_FOLDER
import os, json
import random

@action('/birds', method=['GET'])
@action.uses('index.html', auth)
def redirect_to_main_menu():
    redirect(URL('mainMenu'))

@action('mainMenu')
@action.uses('mainMenu.html', auth)
def mainMenu():
    return dict()

@action('/index')
@action.uses('index.html', auth)
def index():
    return dict()

@action("words")
@action.uses(db, 'wordTest.html')
def words():
    randid = random.randrange(1, 10)
    rows = db(db.words.id == randid).select()
    return dict(rows=rows)
