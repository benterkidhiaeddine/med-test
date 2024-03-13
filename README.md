# Description

This is going to be a platform where medical students cas answer Multiple choice questions about different medical subjects called Modules From Anatomy, Physiology to More Clinical Subjects such as Cardiology and Neurology . The Students can choose which Subjects they are going to be tested on, the corresponding years that those questions were created in and the different Chapters from which the questions were derived . This will make it possible for students to Create their own customized revision session.

# Challenges

The data for the multiple choice questions is not available simply for direct usage for a web application and must first be derived from test Files with different formats such as
(.png , .jpeg , and .pdf) and they need to be corrected , cleaned and organized in a structured manner to store in a SQL database . (Right now I am going with a SQL database because I am using Django and it works best with SQL type database such as PostGresSQL)

# Installation Instructions


# Docker installation



# Non Docker installation




1. First install pipenv in your global python installation if you don't have it

```
pip install pipenv --user

```

2. run the following command to start a virtualenv and install dependencies

```
pipenv install

```

3. run the virtual environment of pipenv

```
pipenv shell

```

4.  cd into the directory of the project and run the migrations to create the database (At the moment it's an sqlite db just suitable for developemnt)

```
cd medTest
python manage.py migrate

```

5. Once that setup you can run the development server with

```
python manage.py runserver 127.0.0.1:8000
```


- The development server will be running on port 8000, On your local machine.

# Note about the developement server

- This server is for developement purposes only and should not be used in production. In production we will be using a 
wsgi server preferably gunicorn + Ngnix

