#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dennis Nguyen-Do'
SITENAME = 'Denny-4/7 Data Science Blog'
SITEURL = ''
SITE_DESCRIPTION = u'My name is Dennis Nguyen-Do. This is my personal blog.'

PATH = 'content'

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
# PAGE_PATHS = ['pages']
# ARTICLE_PATHS = ['blog']

# STATIC PATHS needs to be set to allow us to reference our photos with: /assets/image.png
# This folder is also just a basename, and is relative to the PATH specified so: content/assets
# static paths will be copied without parsing their contents
# remember, don't be using slashes in the string for the assets folder...things do not load this way
# however, when you make reference to them in the reference line, you can add the slash, but you don't put the path into quotations
STATIC_PATHS = ['assets']

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# If content doesn't reload upon update, set this option to False
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)


# Social widget
SOCIAL = (('twitter', 'https://twitter.com/Dennis00481552'),
          ('github', 'https://github.com/SJHH-Nguyen-D/'),)

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 1
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None}

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

SUMMARY_MAX_LENGTH = None

HEADER_COVER = "/assets/head_cover_general.jpg"

HEADER_COVERS_BY_TAG = {
  'articles_cover': 'assets/head_cover_articles.jpg', 
  'pages_cover': '/assets/head_cover_pages.jpg',
  'general_cover': '/assets/head_cover_general.jpg',
}

# Pelican Themes
THEME = "attila" # installed with pelican-themes --install /path/to/attila/theme/from/githubrepo

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

AUTHORS_BIO = {
  "Dennis Nguyen-Do": {
    "name": "Dennis Nguyen-Do",
    "cover": "unavailable",
    "image": "unavailable",
    "website": "unavailable",
    "linkedin": "https://www.linkedin.com/in/dennisnguyendo/",
    "github": "SJHH-Nguyen-D",
    "location": "Toronto, ON",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}


# If you want to disable creation of html files that use tags, uncomment the two lines below
# TAGS_SAVE_AS = ''
# TAG_SAVE_AS = ''

# if you only want to build out a select few pages at a time instead of creating everything from scratch, put them in this list
# If you want to build up everything from scratch because you're not sure which files you made changes in already, you can uncomment the line below
# WRITE_SELECTED = ['/2019/10/sharpestminds-project-part-2.html', '/2018/09/test.html']

# ************ TEMPLATES **********************
# If you want to generate custom pages besides your blog entries, 
# you can point any Jinja2 template file with a path pointing to
# the file and the destination path for the generated file.
# TEMPLATE_PAGES = {'templates/books.html': 'output/pages/books.html',
#                   'templates/resume.html': 'output/pages/resume.html',
#                   'templates/contact.html': 'output/pages/contact.html'}


DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

THEME_TEMPLATES = ['/theme/templates/']
