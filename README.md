# ToDoBackend

# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

#Clone repository
git clone https://github.com/Seba2471/ToDoBackend.git
cd ToDoBackend
python manage.py migrate
