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

def get_time():
    return datetime.datetime.utcnow()

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later

db.define_table(
    'draw',
    Field('word_id'),
    Field('user_id'),
    Field('url'),
    auth.signature
)

db.define_table(
    'words',
    Field('word'),
    Field('category'))

if db(db.words).isempty():
    w = [
        {"word": "Strawberry", "category": "object"},
        {"word": "Battery", "category": "object"},
        {"word": "Shark", "category": "animal"},
        {"word": "Rabbit", "category": "animal"},
        {"word": "Frog", "category": "animal"},
        {"word": "Monkey", "category": "animal"},
        {"word": "Cook", "category": "verb"},
        {"word": "Sleep", "category": "verb"},
        {"word": "Canada", "category": "place"},
        {"word": "Desert", "category": "place"}
    ]
    for item in w:
        db.words.insert(word=item["word"], code=item["category"])

db.commit()
