# dhruthi-hospitals
# Dt7-Solutions
#https://github.com/DT7Solutions/Dt7-Solutioins.git




#install env
#pip install virtualenv
# create virtual environment
#python -m venv env-dhruthi

# activate virtual environment
#env-dhruthi\Scripts\activate

# install libs
pip freeze > requirements.txt 
pip install -r requirements.txt

# create django  project
Django-admin startproject "PROJECTNAME"

# create django app 
python manage.py startapp "APP NAME"

# create super user 
python manage.py createsuperuser
# migration process 
python manage.py makemigrations 

# run migrations 
python manage.py migrate 

# Run project or applications
python manage.py runserver
