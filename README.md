JSONDB allows python to access a local JSON text file like a database. Changes will be saved to the disk json file. This is extremely useful for easily setting up and interfacing with config files


Example Usage:
from JSONDB import JSONDB

jsondb = JSONDB('data.json')

VERSION = jsondb.get('version')

DEBUG = jsondb.get_bool('debug')
