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
SOCIAL = (('twitter', 'https://twitter.com/Dennis00481552'),
          ('github', 'https://github.com/SJHH-Nguyen-D/'),)

DEFAULT_PAGINATION = 5

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

SUMMARY_MAX_LENGTH = None

HEADER_COVER = 'static/images/home-bg.jpg'

# Pelican Themes
THEME = "attila" # installed with pelican-themes --install /path/to/attila/theme/from/githubrepo

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

AUTHORS_BIO = {
  "Dennis Nguyen-Do": {
    "name": "Dennis Nguyen-Do",
    "cover": "https://live.staticflickr.com/4271/35222820026_0cf1cf8183_k_d.jpg",
    "image": "assets/img/avatar.png",
    "website": "unavailable",
    "linkedin": "https://www.linkedin.com/in/dennisnguyendo/",
    "github": "SJHH-Nguyen-D",
    "location": "Toronto, ON",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}