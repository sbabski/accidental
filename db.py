from pymongo import MongoClient
from bson import ObjectId
from extractor import *
from pprint import pprint

client = MongoClient()
db = client.preproduction
users = db.users
media = db.media
tropes = db.tropes


#print out and compare to old results
#also make sure all tropes are /main/ not external or anything

#count tropes for user
#simple vs complex adding:
  #create instance of each trope a media uses, but don't fill it with media until that is called
#decide if worth storing
#eventually have to deal with replacing things
#after doing gui interface


def add_user(name, favs=[]):
  if(len(favs) != 25):
    print('List needs to have 25 items')
    return 0

  def build():
    fav_results = []
    for item in favs:
      media_id = add_media(item[1], item[0])
      fav_results.append({'media_id': media_id, 'weight': item[2]})
    return {'name': name, 'favs': fav_results}

  return add_document(users, {'name': name}, build)

def add_media(title, type):
  def build():
    tropes = parse_page(title, type)
    trope_list = []
    for item in tropes:
      trope_list.append(add_trope_simple(item))
    return {'title': title, 'tropes': trope_list, 'type': type}

  return add_document(media, {'title': title}, build)

def add_media_simple(title, type):
  def build():
    return {'title':title, 'type': type}

def add_trope_simple(title):
  def build():
    return {'title': title}

  return add_document(tropes, {'title': title}, build)

def add_document(collection, query, builder):
  ex = collection.find(query)
  if ex.count() != 0:
    if ex.count() != 1:
      print('ERROR')
      return 0
    else:
      #if complex, need to see if it's previously been only simply added
      return ex[0]['_id']

  result = collection.insert_one(builder())
  return result.inserted_id

users.drop()
media.drop()
tropes.drop()
#pprint(parse_page('amelie', 'film'))
#pprint(parse_page('dragon ball z', 'anime'))
#pprint(parse_page('kill bill', 'film'))
#pprint(parse_page('elfen lied', 'manga'))
#pprint(parse_page('repo men', 'film'))
pprint(parse_page('ratchet and clank', 'western animation'))
'''add_user('plot', [
    ["franchise", "ratchet and clank", 1],
    ["series", "kikaider", 1],
    ["film", "the matrix", 1],
    ["film", "daft punks electroma", 1],
    ["literature", "a wind named amnesia", 1],
    ["film", "tetsuo the iron man", 1],
    ["film", "eden log", 1],
    ["film", "deadly friend", 1],
    ["film", "la jetee", 1],
    ["series", "extant", 1],
    ["film", "quintet", 1],
    ["literature", "the lathe of heaven", 1],
    ["film", "existenz", 1],
    ["film", "repo men", 1],
    ["anime", "sailor moon crystal", 1],
    ["film", "chronicle", 1],
    ["anime", "cowboy bebop", 1],
    ["film", "the city of lost children", 1],
    ["anime", "rahXephon", 1],
    ["film", "cyborg", 1],
    ["anime", "the place promised in our early days", 1],
    ["anime", "toward the terra", 1],
    ["manga", "venus wars", 1],
    ["anime", "elfen lied", 1],
    ["film", "the maze runner", 1]
])'''
'''add_user('mood', [
    ["film", "the red circle", 1],
    ["film", "heat", 1],
    ["anime", "kill la kill", 1],
    ["anime", "patlabor", 1],
    ["film", "mad max beyond thunderdome", 1],
    ["film", "batman", 1],
    ["anime", "night raid 1931", 1],
    ["film", "kill bill", 1],
    ["franchise", "zatoichi", 1],
    ["film", "the quick and the dead", 1],
    ["film", "snake eyes", 1],
    ["film", "spies", 1],
    ["film", "a chinese ghost story", 1],
    ["film", "cube", 1],
    ["manga", "x 1999", 1],
    ["light novel", "no 6", 1],
    ["literature", "ivanhoe", 1],
    ["film", "the beach", 1],
    ["anime", "earth maiden arjuna", 1],
    ["manga", "lone wolf and cub", 1],
    ["film", "the lord of the rings", 1],
    ["series", "treasure island 2012", 1],
    ["film", "the giver", 1],
    ["series", "gotham", 1],
    ["film", "a fistful of dollars", 1]
])'''
'''add_user('aw', [
    ["western animation", "the last unicorn", 1],
    ["film", "the dark crystal", 1],
    ["film", "scream1996", 1],
    ["film", "alien", 1],
    ["film", "requiem for a dream", 1],
    ["film", "a scanner darkly", 1],
    ["film", "blow", 1],
    ["film", "goodfellas", 1],
    ["film", "sixteen candles", 1],
    ["anime", "kikis delivery service", 1],
    ["film", "clueless", 1],
    ["film", "rebecca", 1],
    ["film", "thirteen", 1],
    ["anime", "castle in the sky", 1],
    ["film", "valley girl", 1],
    ["anime", "howls moving castle", 1],
    ["anime", "ghost in the shell", 1],
    ["anime", "blood the last vampire", 1],
    ["series", "skins", 1],
    ["anime", "flcl", 1],
    ["anime", "samurai champloo", 1],
    ["anime", "ergo proxy", 1],
    ["western animation", "the boondocks", 1],
    ["western animation", "south park", 1],
    ["anime", "digimon adventure", 1]
])'''
print(tropes.find().count())
'''add_user('gm', [
    ["film", "the professional", 1],
    ["film", "the big lebowski", 1],
    ["film", "pulp fiction", 1],
    ["film", "fight club", 1],
    ["film", "two thousand one a space odyssey", 1],
    ["film", "kill bill", 1],
    ["film", "magnolia", 1],
    ["film", "yojimbo", 1],
    ["film", "requiem for a dream", 1],
    ["film", "the thin red line", 1],
    ["film", "dr strangelove", 1],
    ["film", "his girl friday", 1],
    ["film", "rushmore", 1],
    ["film", "mad max 2 the road warrior", 1],
    ["film", "amelie", 1],
    ["film", "high noon", 1],
    ["anime", "ghost in the shell", 1],
    ["anime", "akira", 1],
    ["anime", "cowboy bebop", 1],
    ["anime", "samurai champloo", 1],
    ["anime", "dragon ball z", 1],
    ["series", "lost", 1],
    ["series", "the x files", 1],
    ["western animation", "family guy", 1],
    ["series", "star trek the next generation", 1]
])'''
'''
for document in users.find():
  pprint(document)
for document in media.find():
  pprint(document)
'''
print(tropes.find().count())
#for document in tropes.find():
  #pprint(document)