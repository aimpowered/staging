#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Shaomei Wu'
SITENAME = 'AIMPOWER'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Google Scholar', 'https://scholar.google.com/citations?user=Y0xVWqYAAAAJ'),
         ('Facebook Research Profile', 'https://research.fb.com/people/wu-shaomei/'),
         ('Automatic Alt-text', 'https://about.fb.com/news/2016/04/using-artificial-intelligence-to-help-blind-people-see-facebook/'),)

HIDE_SIDEBAR = True

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='/Users/shaomeiwu/git/pelican-themes/pelican-bootstrap3'
#THEME='/Users/shaomeiwu/git/pelican-themes/Just-Read'
#THEME="simple"
#BOOTSTRAP_THEME='readable' ## good
#BOOTSTRAP_THEME='cerulean'
#BOOTSTRAP_THEME='cosmo'  ## good
#BOOTSTRAP_THEME='custom'
#BOOTSTRAP_THEME='cyborg'
#BOOTSTRAP_THEME='darkly'
#BOOTSTRAP_THEME='flatly'
#BOOTSTRAP_THEME='journal' ##good
BOOTSTRAP_THEME='lumen'
#BOOTSTRAP_THEME='readable-old'
#BOOTSTRAP_THEME='sandstone'
#BOOTSTRAP_THEME='shamrock'
#BOOTSTRAP_THEME='slate'
#BOOTSTRAP_THEME='superhero'
#BOOTSTRAP_THEME='spacelab'
#BOOTSTRAP_THEME='united'
#BOOTSTRAP_THEME='yeti'

PLUGIN_PATHS = ['/Users/shaomeiwu/git/pelican-plugins',]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
