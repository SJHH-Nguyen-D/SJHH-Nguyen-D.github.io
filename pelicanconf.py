#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dennis Nguyen-Do'
SITENAME = 'Denny-4/7 Data Science Blog'
SITEURL = ''

HEADER_COVER = "/home/dennis/Documents/datascience_adventures/pythonscripts/datascience_job_portfolio/SJHH-Nguyen-D.github.io/content/assets/img/35222820026_46cc483a34_z.jpg"

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# If content doesn't reload upon update, set this option to False
LOAD_CONTENT_CACHE = False

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
SOCIAL = (('Twitter (#Dennis00481552)', 'https://twitter.com/Dennis00481552'),
          ('LinkedIn (dennisnguyendo)', 'https://www.linkedin.com/in/dennisnguyendo/'),
          ('GitHub (SJHH-Nguyen-D)', 'https://github.com/SJHH-Nguyen-D/'),)

DEFAULT_PAGINATION = 5

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

SUMMARY_MAX_LENGTH = None

# HEADER_COVER = 'content/assets/img/34875474670_a97e36c750_z.jpg' # japanese temple replica

# Pelican Themes
THEME = "attila" # installed with pelican-themes --install /path/to/attila/theme/from/githubrepo

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True