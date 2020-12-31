RUNNNING INSTRUCTIONS:

This app uses Flask, a Python framework used for web development. 

If Flask is not already installed on your computer, follow these instructions (https://flask.palletsprojects.com/en/1.1.x/installation/). You will need to have Python installed before you can install Flask.

You will also need to create a database to link the SQL tables to. On a Mac, use the terminal command 'createdb [database_name]. Then go into the project directory and link it to the SQL tables with the command 'psql -d [database_name] -f db/cooking_academy.sql'

Use the terminal command 'flask run' to launch the app. 

You can populate tables before launching flask by adding python commands to console.py, and running that first.



PROJECT BRIEF:

This app is based on the Gym.md file included in this directory. However, to differentiate it from other projects the theme has been changed from a gym to a cooking academy. However, the functionality is the same.