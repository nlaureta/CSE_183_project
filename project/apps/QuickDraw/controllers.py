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
    # Get all the words that the user has already drawn.
    used_words = [row['word'] for row in db(db.draw.user_id == get_user()).select(db.draw.word).as_list()]  

    # Count the total number of words in the 'words' table
    total_records = db(db.words).count()

    # Check if the user has already drawn all the words.
    if len(used_words) >= total_records:
        return dict(message="all_words_drawn")

    # Initialize the word to None. This variable will store the word we're going to return.
    word = None

    while True:
        # Generate a random index within the range of total records in the 'words' table
        random_index = random.randint(0, total_records - 1) 

        # Fetch the word at the random index. We limit the selection to only one record at the random index.
        potential_word_row = db(db.words).select(db.words.word, limitby=(random_index, random_index + 1)).first()

        # If a word was fetched (i.e., if the fetched row is not None)
        if potential_word_row:
            # Extract the word string from the Row
            potential_word = potential_word_row['word']

            # If this word hasn't been drawn by the user yet
            if potential_word not in used_words:
                # Set this as the word we're going to return
                word = potential_word
                # And break out of the loop, since we've found a word
                break 

    # Return the word as a dictionary. The 'word' key will contain the word string.
    return dict(word=word)