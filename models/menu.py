# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(IMG(_src=URL('static', "images", 'logo.png'), _alt="logo"), _href=URL('index'))
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Main Page'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('Start Browsing'), False, URL('default', 'main'), []),
        (T('Category'), False, '#', [
            (T('Alcohol'), False, URL('default', 'alcohol')),
            (T('Alcohol free'), False, URL('default', 'alcohol_free')),
            (T('Breakfast'), False, URL('default', 'breakfast')),
            (T('Brunch'), False, URL('default', 'brunch')),
            (T('Dairy product free'), False, URL('default', 'dairy_product_free')),
            (T('Dessert'), False, URL('default', 'dessert')),
            (T('Dinner'), False, URL('default', 'dinner')),
            (T('Gluten free'), False, URL('default', 'gluten_free')),
            (T('Kosher'), False, URL('default', 'kosher')),
            (T('Lunch'), False, URL('default', 'lunch')),
            (T('Pescetarian'), False, URL('default', 'pescetarian')),
            (T('Snacks'), False, URL('default', 'snack')),
            (T('Vegan'), False, URL('default', 'vegan')),
            (T('Vegetarian'), False, URL('default', 'vegetarian')),
        ]),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
