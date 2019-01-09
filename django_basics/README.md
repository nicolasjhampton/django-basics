# Create a project

`django-admin startproject learning_site`

# start the server for the project

navigate into the project folder beside manage.py

`python manage.py runserver 0.0.0.0:8000`

# run the initial migrations

`python manage.py migrate`

# create a pluggable app

`python manage.py startapp courses`

# create the migration for your first model once the class has been created

`python manage.py makemigrations courses`

# then run the courses migrations

`python manage.py migrate courses`
