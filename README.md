1) # modify settings.py to use sqlite3 as db
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': 'db.sqlite3',
     }
 }

2) Add category and packages(if not present) from admin panel to check
   
3) To create superuser(py manage.py createsuperuser)
