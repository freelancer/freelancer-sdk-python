# Force Beer
## What does the app do?
The app posts a Freelancer local project on behalf of the logged in user. The project's task is to deliver a beer to a specified location.
The logged in user can then accept a bid for the project, and pay for it using the app.

## How do I use it?
Log into the app using your Freelancer account, and click the big 'USE THE FORCE' button. This will post a standardised project to Freelancer for you. 
When bids for this project start to arrive, Stormtroopers will appear below the button, with their bid-amount underneath their character. When you're satisfied with a bid,
click one of the Stormtroopers and they will be awarded with the project. A 'pay' button will appear above their heads when you do this. Once you have received the beer, press the 'pay' button
and they will be paid via the Freelancer platform, and you will have a beer.

# Setting up the App

## Set up your Freelancer Client
Navigate to the Freelancer API documentation and follow the steps for creating a client, found [here](https://developers.freelancer.com/docs/authentication/creating-a-client).

Once you've created your client, you will be provided with your client_id and client_secret key for the app. Copy these values into the `CLIENT_ID` and `CLIENT_SECRET` variables in`config.py`.

## Set up your local virtual environment
First, set up a Python virtual environment using virtualenv.

`$ pip install virtualenv`

Then navigate to the directory where you want to store your environment and run:

`$ virtualenv <my_environment_name>`

Once this is done, you can activate your environment with:

`source /path/to/environment/bin/activate`

## Install the requirements
Using pip in the environment, install the requirements as specified in requirements.txt with:

`$ pip install -r /path/to/requirements.txt`

## Set up your PostgreSQL database
Here's a good [guide](https://www.techrepublic.com/blog/diy-it-guy/diy-a-postgresql-database-server-setup-anyone-can-handle/) to setting up a PostgreSQL database.
Once you've gone through the guide and set up your database user, go to `config.py` and set `SQLALCHEMY_DATABASE_URI` to:

`SQLALCHEMY_DATABASE_URI = 'postgresql://<database_user_name>:<database_user_password>@localhost:5432/<database_name>'`

Once that's done, open your terminal to the app's root directory and run

```
$ python
>>> from app import db
>>> db.create_all()
>>> exit()
```

## Run the Application
Force Beer uses the Python-Flask framework. So you can run the Flask application by running

`$ export FLASK_APP=app.py`

`$ flask run`