# Telegram Bot for Pizzeria

This is a Telegram bot project. This bot can show the pizzeria menu.
You can edit a database of this bot by using admin console available at
url address [http://your_site_url/admin](http://127.0.0.1:5000/admin).

This project also provide you create the database and load data from a file.
For this purposes you can use scripts create_db.py and load2databse.py .

# Create the database

For creating the database, you must set several enviroment variables,
such :
FLASK_APP - file with flask app,
DATABASE_DIR - name of database directory,
DATABASE_FILENAME - name of database file,
FLASK_USER - user for admin console,
FLASK_USER_PASSWD - password of user

For example:

    export FLASK_APP='server.py'
    export DATABASE_DIR='sqlite'
    export DATABASE_FILENAME='app.db'
    export FLASK_USER='admin'
    export FLASK_USER_PASSWD='secret'

Next you may run a script create_db.py and create migrations :

    flask db init
    flask db migrate
    flask db upgrade

# Load data from a file
For load data from a file you must use file models_json.py for add and edit
data like json array. For load data to the database, use a script
load2database.py.

# How to Use

Step 1. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

Step 2. Launch

```
#!bash

$ # the token below is not actual, you need to register a new one
$ BOT_TOKEN="110831855:AAE_GbIeVAUwk11O12vq4UeMnl20iADUtM" python3 bot.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
