# Tourism Management System

A travel booking web application built with Django and PostgreSQL. This system allows users to explore various travel packages, select travel dates, and book trips based on group size through an intuitive and responsive interface.

## Features

- User registration and authentication  
- Browse and search travel packages by category  
- Select travel dates and group size for bookings  
- Manage bookings and view booking history (if implemented)  
- Responsive design for seamless experience on all devices  

## Technologies Used

- Python 3.x  
- Django Web Framework  
- PostgreSQL Database  
- HTML5, CSS3, Bootstrap (or other CSS framework if used)  

### Configuration
1) modify settings.py to use sqlite3 as db
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': 'db.sqlite3',
     }
 }

2) Add category and packages(if not present) from admin panel to check
   
3) To create superuser(py manage.py createsuperuser)
