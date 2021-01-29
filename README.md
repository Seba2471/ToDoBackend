# ToDoBackend

# Create the project directory
mkdir tutorial

cd tutorial

# Create a virtual environment to isolate our package dependencies locally

python3 -m venv env

source env/bin/activate

# On Windows use `env\Scripts\activate`

#Clone repository

git clone https://github.com/Seba2471/ToDoBackend.git

cd ToDoBackend

# Install Django and Django REST framework into the virtual environment
pip install django

pip install djangorestframework

python -m pip install django-cors-headers

pip install django-filter

pip install djangorestframework-simplejwt

python manage.py migrate

python manage.py runserver
