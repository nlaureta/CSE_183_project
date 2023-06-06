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
    'result',
    Field('win'),
    Field('user_id'),
    Field('draw_id', 'reference draw')
)

db.define_table(
    'words',
    Field('word'),
    Field('category'),
)

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
        {"word": "Desert", "category": "place"},
        {"word": "Waffles", "category": "object"},
        {"word": "Cupcake", "category": "object"},
        {"word": "Atlantis", "category": "place"},
        {"word": "Sandcastle", "category": "object"},
        {"word": "Dolphin", "category": "animal"},
        {"word": "Lion", "category": "animal"},
        {"word": "Farm", "category": "place"},
        {"word": "Hospital", "category": "place"},
        {"word": "Beach", "category": "place"},
        {"word": "Yoshi", "category": "creature"},
        {"word": "Leprechaun", "category": "people"},
        {"word": "Pirate", "category": "people"},
        {"word": "Superman", "category": "people"},
        {"word": "Panda", "category": "animal"},
        {"word": "Mars", "category": "place"},
        {"word": "Starfish", "category": "animal"},
        {"word": "Peanut", "category": "food"},
        {"word": "Robot", "category": "object"},
        {"word": "Nurse", "category": "people"},
        {"word": "Dragon", "category": "creature"},
        {"word": "Mermaid", "category": "oreature"},
        {"word": "Lollipop", "category": "food"},
        {"word": "Kitten", "category": "animal"},
        {"word": "Castle", "category": "place"},
        {"word": "Space", "category": "place"},
        {"word": "Train", "category": "object"},
        {"word": "Playground", "category": "place"},
        {"word": "Piano", "category": "object"},
        {"word": "Lobster", "category": "animal"},
        {"word": "Minivan", "category": "object"},
        {"word": "Slipper", "category": "object"},
        {"word": "Computer", "category": "object"},
        {"word": "Volleyball", "category": "object"},
        {"word": "Snowflake", "category": "object"},
        {"word": "Lamp", "category": "object"},
        {"word": "Igloo", "category": "object"},
        {"word": "Pizza", "category": "food"},
        {"word": "Book", "category": "object"},
        {"word": "Flower", "category": "object"},
        {"word": "Egg", "category": "food"},
        {"word": "Butterfly", "category": "animal"},
        {"word": "Baseball", "category": "object"},
        {"word": "Apple", "category": "food"},
        {"word": "Kitchen", "category": "place"},
        {"word": "Home", "category": "place"},
        {"word": "Hat", "category": "object"},
        {"word": "Goldfish", "category": "animal"},
        {"word": "Umbrella", "category": "object"},
        {"word": "Spiderweb", "category": "object"},
        {"word": "Jellyfish", "category": "animal"},
        {"word": "Leaf", "category": "object"},
        {"word": "Desk", "category": "object"},
        {"word": "Seaweed", "category": "object"},
        {"word": "Cheese", "category": "food"},
        {"word": "Ninja", "category": "people"},
        {"word": "Unicorn", "category": "creature"},
        {"word": "Noodles", "category": "food"},
        {"word": "Whale", "category": "animal"},
        {"word": "Mushroom", "category": "food"},
        {"word": "Fairy", "category": "creature"},
        {"word": "Lawnmower", "category": "object"},
        {"word": "Milkshake", "category": "food"},
        {"word": "Thunderstorm", "category": "object"},
        {"word": "Junkyard", "category": "place"},
        {"word": "Chocolate", "category": "food"},
        {"word": "Snowman", "category": "object"},
        {"word": "Squirrel", "category": "animal"},
        {"word": "Bottle", "category": "object"},
        {"word": "Pillow", "category": "object"},
        {"word": "Skeleton", "category": "object"},
        {"word": "Tree", "category": "object"},
        {"word": "Zebra", "category": "animal"},
        {"word": "Potato", "category": "food"},
        {"word": "Thermometer", "category": "object"},
        {"word": "Rainbow", "category": "object"},
        {"word": "Cow", "category": "animal"},
        {"word": "Jeans", "category": "object"},
        {"word": "Pikachu", "category": "creature"},
        {"word": "Pumpkin", "category": "object"},
        {"word": "Batman", "category": "people"},
        {"word": "Shrek", "category": "people"},
        {"word": "Wolverine", "category": "creature"},
        {"word": "Moon", "category": "object"},
        {"word": "Sushi", "category": "food"},
        {"word": "Mailbox", "category": "object"},
        {"word": "Toast", "category": "food"},
        {"word": "Fireworks", "category": "object"},
        {"word": "Snake", "category": "animal"},
        {"word": "Human", "category": "people"},
        {"word": "Octopus", "category": "animal"},
        {"word": "Pig", "category": "animal"},
    ]
    for item in w:
        db.words.insert(word=item["word"], category=item["category"])

db.commit()
