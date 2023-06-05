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
    randid = random.randrange(1, 20)
    rows = db(db.words.id == randid).select()
    return dict(rows=rows)

# I think we do not need to connect correct word and guess word here
# but we still need this function to connect wordGuess.html
@action("wordGuess", method=["GET", "POST"])
@action.uses('wordGuess.html',db,  auth.user )
def words():
    # if request.method == "POST":
    #     guessed_word = request.forms.get("guess").lower() 
    #     correct_word = "apple"  
        
    #     if guessed_word == correct_word:
    #         redirect(URL('/index'))
    
    return dict()

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
    total_records = db(db.draw).count()

    # Check if there are any records in the draw table
    if total_records == 0:
        return dict(urls=[], message="No images in the database")

    # If there are records, proceed with getting a random image
    random_index = random.randint(0, total_records - 1) # get random image in our database
    urls = db(db.draw).select(limitby=(random_index, random_index + 1))
    return dict(urls=urls)

@action('/getWords')
@action.uses(db, auth.user)
def getWords():
    used_words = [row['word'] for row in db(db.draw.user_id == get_user()).select(db.draw.word).as_list()]  
    total_records = db(db.words).count()
    word = None

    while True:
        random_index = random.randint(0, total_records - 1)  
        potential_word_row = db(db.words).select(db.words.word, limitby=(random_index, random_index + 1)).first()
        if potential_word_row:
            potential_word = potential_word_row['word']
            if potential_word not in used_words:  
                word = potential_word
                break  

    return dict(word=word)