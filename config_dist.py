# encoding: utf-8

"""
Globale Konfiguration für die Webapp und Kommandozeilen-Scripte

Die Einstellungen in dieser Datei müssen der jeweiligen Umgebung angepasst
und der Name der Datei zu "config.py" geändert werden.

Copyright (c) 2012 Marian Steinbach

Hiermit wird unentgeltlich jeder Person, die eine Kopie der Software und
der zugehörigen Dokumentationen (die "Software") erhält, die Erlaubnis
erteilt, sie uneingeschränkt zu benutzen, inklusive und ohne Ausnahme, dem
Recht, sie zu verwenden, kopieren, ändern, fusionieren, verlegen,
verbreiten, unterlizenzieren und/oder zu verkaufen, und Personen, die diese
Software erhalten, diese Rechte zu geben, unter den folgenden Bedingungen:

Der obige Urheberrechtsvermerk und dieser Erlaubnisvermerk sind in allen
Kopien oder Teilkopien der Software beizulegen.

Die Software wird ohne jede ausdrückliche oder implizierte Garantie
bereitgestellt, einschließlich der Garantie zur Benutzung für den
vorgesehenen oder einen bestimmten Zweck sowie jeglicher Rechtsverletzung,
jedoch nicht darauf beschränkt. In keinem Fall sind die Autoren oder
Copyrightinhaber für jeglichen Schaden oder sonstige Ansprüche haftbar zu
machen, ob infolge der Erfüllung eines Vertrages, eines Delikts oder anders
im Zusammenhang mit der Software oder sonstiger Verwendung der Software
entstanden.
"""

import locale

LOCALE = 'de_DE'

locale.setlocale(locale.LC_ALL, LOCALE)

# Absolute path to webapp folder
WWW_PATH = '/Users/marian/github/offeneskoeln/webapp'

# Path for static files
STATIC_PATH = WWW_PATH + '/static'

# Path for thumbnails
THUMBS_PATH = STATIC_PATH + '/thumbs'

# Name of the location. Use unicode if needed.
#LOCATION_NAME = u'K\xf6ln'
LOCATION_NAME = 'Mannheim'

# Type of database. Currently, only "mongodb" is supported
DB_TYPE = 'mongodb'

# Database configuration
DB_HOST = 'localhost'
DB_PORT = 27017
DB_USER = ''
DB_PASS = ''
DB_NAME = 'scrapearis'

# We generate thumbnails for these attachment types
THUMBNAILS_VALID_TYPES = ['jpg', 'pdf', 'tif', 'bmp', 'png', 'gif']

# Sizes (heights) of generated thumbnails
THUMBNAILS_SIZES = [800, 300, 150]

# File suffix for generated thumbnails
THUMBNAILS_SUFFIX = 'jpg'

# Path to GPL Ghostscript executable
GS_CMD = '/Path/to/bin/gs'

# Path to pdftotext executable
PDFTOTEXT_CMD = '/Path/to/bin/pdftotext'

# Word lists paths for ElasticSearch
ES_PATH_BASE = '/Path/to/offeneskoeln/config/'
STOPWORDS_PATH_GLOBAL = ES_PATH_BASE + 'stopwords_de_global.txt'
SYNONYMS_PATH_GLOBAL = ES_PATH_BASE + 'synonyms_global.txt'

# ElasticSearch settings
ES_HOST = 'localhost'
ES_PORT = 9200

# Path to mongodump executable
MONGODUMP_CMD = '/Path/to/bin/mongodump'

# Which collections should be contained in database dumps?
DB_DUMP_COLLECTIONS = ['submissions', 'sessions', 'attachments', 'locations']
DB_DUMP_TEMPFOLDER = 'datadump'

####################################################
# Webapp configuration

# Absolute path to the webapp folder in the file system
BASE_PATH = '/Path/to/offeneskoeln/webapp'


# Partial path to the static directory
STATIC_URL = BASE_URL + 'static/'

# Partial path to the thumbs directory
THUMBS_URL = BASE_URL + 'static/thumbs/'

# Partial path to the submissions RSS feed
SUBMISSION_RSS_URL = 'static/rss/dokumente.xml'

# Disqus Comments shortname
DISQUS_SHORTNAME = 'your_disqus_shortname'

# This has to be False for production!
DEBUG = True

MONGO_HOST = DB_HOST
MONGO_PORT = DB_PORT
MONGO_DBNAME = DB_NAME

# Attachment URL pattern
ATTACHMENT_DOWNLOAD_URL = BASE_URL + 'anhang/%s.%s'

MAP_TILE_URL_SCHEMA = 'http://otile1.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.jpg'
MAP_TILE_ZOOMLEVEL_MIN = 4
MAP_TILE_ZOOMLEVEL_MAX = 18
MAP_TILE_ATTRIBUTION = 'Map Data © <a href="http://www.openstreetmap.org">OpenStreetMap</a> contributors, Tiles courtesy of <a href="http://www.mapquest.com/" target="_blank">MapQuest</a>.'



