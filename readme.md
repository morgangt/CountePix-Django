Counter Object for Django
=========================

Counting Hits
-------------
The main business-logic for evaluating and counting a Hit is done. You can use this class method directly in your own Views or you can use one of the Views packaged with this app.


Quick start
===========

1. Add a folder to the project

2. Add "django_counter_field" to your INSTALLED_APPS setting:

INSTALLED_APPS = (
    ...
    'django_counter_field',
)

3. first get the related HitCount object for your model object

from apps.hitcounter.models import Counter

...

Counter.hit(MODEL)
