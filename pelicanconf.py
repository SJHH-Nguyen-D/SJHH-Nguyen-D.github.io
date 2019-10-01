#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dennis Nguyen-Do'
SITENAME = 'Denny-4/7 Data Science Blog'
SITEURL = ''
SITE_DESCRIPTION = u'My name is Dennis Nguyen-Do. This is my personal blog.'

# LANDING_PAGE_ABOUT = {'details': """<div><p>My name is Dennis.
# I’ve dabbled with web development, desktop scripting, pygame developement and reinforcement learning.
# I’m currently a Master’s graduate in eHealth/Health Informatics.

# <img src="" alt="It's a picture of me!" width="" height="">

# As an avid independent learner and lover of analytics, I dove into the world of data science some 4 odd years ago,
# having first exposure through my undergraduate and graduate statistics courses. My internship for my master's program provided me an opportunity to work on Through a combination of database
# management, data mining, machine learning and programming MOOCs/class courses, and the amazing power of the internet, I
# have been able to get to where I am today in my career.

# With this personal blog, I intend to share my projects I’m currently working on or have worked on in the past,
# partly also as a way of establishing an archive. If you find anything interesting, feel absolutely.</p></div>"""}

PATH = 'content'
# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
# PAGE_PATHS = ['pages']
# ARTICLE_PATHS = ['blog']

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

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

SUMMARY_MAX_LENGTH = None

HEADER_COVER = 'https://live.staticflickr.com/4271/35222820026_0cf1cf8183_k_d.jpg'

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

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

THEM_TEMPLATES = ['/theme/templates/']

PAGINATED_DIRECT_TEMPLATES = ['index']