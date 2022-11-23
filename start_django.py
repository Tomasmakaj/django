# Creating a virtual environment to work with Django
python3 -m venv 11_env

# To Activate the Virtual Environment
source 11_env/bin/activate

# If your using Powershell without the word source to activate the virtual environment you might need to capitalize Activate

# To Stop using virtual environment enter
deactivate

# Install Django once the environment is activarted enter:
pip3 install django or pip install django

# Creating a project in Django (remember to look for the 11_env in parentheses)
django-admin startproject learning log .

# This command tells Django to set up a new project called learning_log 
# The dot at the end of the command creates the new project with a directory structure that will make it easy to deploy the app to a server when finished
# Dont forget the dot if you forget delete the files and folders that were created and run the command again with the dot

# Creating the Database
python manage.py migrate

