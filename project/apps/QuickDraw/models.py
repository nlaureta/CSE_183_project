"""
This file defines the database models
"""

import datetime
import random
from py4web.utils.populate import FIRST_NAMES, LAST_NAMES, IUP
from .common import db, Field, auth
from pydal.validators import *

def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_username():
    return auth.current_user.get('username') if auth.current_user else None

def get_user():
    return auth.current_user.get('id') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later

db.define_table(
    'draw',
    Field('word'),
    Field('user_id'),
    Field('url'),
    auth.signature
)

db.define_table(
    'words',
    Field('word'),
    Field('category'),
    Field('num_let')
)

if db(db.words).isempty():
    w = [
        {"word": "Strawberry", "category": "object", "num_let": "10"},
        {"word": "Battery", "category": "object", "num_let": "7"},
        {"word": "Shark", "category": "animal", "num_let": "5"},
        {"word": "Rabbit", "category": "animal", "num_let": "6"},
        {"word": "Frog", "category": "animal", "num_let": "4"},
        {"word": "Monkey", "category": "animal", "num_let": "6"},
        {"word": "Cook", "category": "verb", "num_let": "4"},
        {"word": "Sleep", "category": "verb", "num_let": "5"},
        {"word": "Canada", "category": "place", "num_let": "6"},
        {"word": "Desert", "category": "place", "num_let": "6"}
    ]
    for item in w:
        db.words.insert(word=item["word"], category=item["category"], num_let=item["num_let"])

db.commit()
