# Python/Flask Directory Listing Script
A simple script that will list the contents of a directory it is pointed to in the config and allow you to download the files easily.
Best run with *gunicorn* and Heroku-ready.

## How to install?
The installation is pretty simple!
. Make sure you are running Linux or OS X. Windows may work but is not supported!
- Clone this repo using ```git clone git@github.com:JacobCZ/flask-directory-list.git```
- Make sure you have **pip** and **virtualenv** installed
- Run ```virtualenv venv``` to create a new virtual env and ```source venv/bin/activate``` to switch to it
- Install the requirements with ```pip install -r requirements.txt```
- Edit the configuration in the ```app.py``` file
- Run with ```gunicorn app:app```
- Profit! :fireworks:

## Deploying to heroku
- Register on Heroku
- Download and install [Heroku Toolbelt](https://toolbelt.heroku.com/)
- ```heroku login``` to log-in to Heroku
- ```heroku create [name]``` to create a new heroku app (replace name with something, omit brackets)
- ```git push heroku master``` to deploy
- ```heroku ps:scale web=1``` to create one (free) Heroku dyno
- Profit!

## License?
This script is published under the **[Do Whatever You Feel Like, I Don't Fucking Care license](https://github.com/JacobCZ/DWYFLIDFC)**. That means you can literally do anything you fucking want. Fork it, modify it, rewrite it, sell it... I don't care!

## Any issues?
If you have any issues with this script, please create an issue [here](https://github.com/JacobCZ/flask-directory-list/issues). You can also fix the error yourself and create a pull request!
