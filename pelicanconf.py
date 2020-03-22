#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'André Thiago'
SITENAME = 'Robô Aprendiz'
SITETITLE = 'Robô Aprendiz'
SITESUBTITLE = 'Aprendizagem de máquina com técnicas de IA'
SITEDESCRIPTION = SITETITLE + ' - ' + SITESUBTITLE
SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/artificial-intelligence.png'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

#DEFAULT_LANG = 'pt'
MAIN_MENU = True
LINKS_IN_NEW_TAB = 'internal'
USE_FOLDER_AS_CATEGORY = False
HOME_HIDE_TAGS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Sobre', '#'),
         ('Contato', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = (('Arquivos', '/archives.html'),
             ('Categorias', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'themes/Flex' #'themes/clean-blog'

# Path to the folder containing the plugins
PLUGIN_PATHS = ['pelican-plugins']
# Enabled plugins
PLUGINS = ['sitemap', 'pelican-ipynb.markup', 'i18n_subsites']

# sitemap plugin configuration
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}

# jupyter plugin configuration
MARKUP = ('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_SKIP_CSS=True

# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

# Translate to German.
DEFAULT_LANG = 'pt_BR'
#OG_LOCALE = 'pt_BR'
#LOCALE = 'pt_BR'

# Default theme language.
I18N_TEMPLATES_LANG = 'pt_BR'
