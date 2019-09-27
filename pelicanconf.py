#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dennis Nguyen-Do'
SITENAME = 'Denny-4/7 Data Science Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter (#Dennis00481552)', 'https://twitter.com/Dennis00481552'),
          ('LinkedIn (dennisnguyendo)', 'https://www.linkedin.com/in/dennisnguyendo/'),
          ('GitHub (SJHH-Nguyen-D)', 'https://github.com/SJHH-Nguyen-D/'),)

DEFAULT_PAGINATION = 5

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Pelican Themes
THEME = "/home/dennis/Desktop/Link to datascience_job_portfolio/pelican-themes/attila/"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True