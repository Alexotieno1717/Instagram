## Instagram
### Author
* Alex Otieno

### Description
This is a clone of Instagram where people share their images and videos for other users to view. Users can sign up, login, view and post photos, search and follow other users.

### Live link
Click (View Site)[instagramapp01.herokuapp.com/] to visit the site

### User Story
* Sign in to the application to start using.
* Upload a pictures to the application.
* Search for different users using their usernames.
* See your profile with all your pictures.
* Follow other users and see their pictures on my timeline.

### Setup and Installation

Cloning the repository:
    https://github.com/Alexotieno1717/Instagram

Navigate into the folder and install requirements
    cd Instagram and  pip install -r requirements.txt 

Install and activate Virtual
    python3 -m venv venv - source venv/bin/activate 
Setup Database
    python manage.py makemigrations instagram
Migrate
    python manage.py migrate 
Run the application
    python manage.py runserver 
Open in browser
    Open the application on your browser 127.0.0.1:8000.

### Technology used
* Python3.6
* Django 1.11
* Heroku

### Known Bugs
Some functionalty did not work search,likes and comment as expected

### 