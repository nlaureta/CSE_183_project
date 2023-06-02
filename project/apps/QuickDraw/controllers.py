from py4web import action, request, abort, redirect, URL
from .common import db, session, T, cache, auth, logger
from .models import get_user_email, get_user
from .settings import APP_FOLDER
import os, json
import random

@action('/QuickDraw/index', method=['GET'])
@action.uses('index.html', auth.user)
def redirect_to_main_menu():
    redirect(URL('mainMenu'))

@action('mainMenu')
@action.uses('mainMenu.html', auth.user)
def mainMenu():
    return dict()

@action('/index')
@action.uses('index.html', db,  auth.user)
def index():
    randid = random.randrange(1, 10)
    rows = db(db.words.id == randid).select()
    return dict(rows=rows)


@action("wordGuess", method=["GET", "POST"])
@action.uses('wordGuess.html',db,  auth.user )
def words():
    randid = random.randrange(1,10)
    rows = db(db.words.id == randid).select(db.words.num_let)
    if request.method == "POST":
        guessed_word = request.forms.get("guess").lower() 
        correct_word = "apple"  
        
        if guessed_word == correct_word:
            redirect(URL('/index'))
    
    return dict(rows=rows)

@action("homepage")
@action.uses('homepage.html', auth.user )
def homepage():
    return dict()

@action('/saveCanvas', method=['POST'])
@action.uses(db, auth.user)
def saveCanvas():
  word = request.json.get('word')
  url = request.json.get('url')  # Get dataURL from the POST request

  # Insert the new draw into the database
  id = db.draw.insert(word=word, user_id=get_user(), url=url)

  # Return the id of the new draw
  return dict(id=id)

@action('/getImages')
@action.uses(db, auth.user)
def getImages():
    urls = db(db.draw).select(limitby=(0, 1))
    return dict(urls=urls)