1) # modify settings.py to use sqlite3 as db
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': 'db.sqlite3',
     }
 }

2) Add category and packages(if not present) from admin panel to check
    -(py manage.py createsuperuser)
