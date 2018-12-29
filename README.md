# FLASK CHAT API

## List Endpoint in Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](-)

## Installing VIRTUALENV

Please follow the steps here:

* https://virtualenv.pypa.io/en/latest/installation/

## Requirements
- Python 3.7
- Git
- Virtualenv

## Editor (IDE)
- Visual Studio Code (Recommended)
- Sublime 3
- Atom

After installing one of those editors, please make sure that you install [EditorConfig](http://editorconfig.org/) plugin so that every user will use the same editor configuration for this project.

## Coding Syle Guide

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Structure Project
```sh
project_name/
.... app/
........ config/
........ controller/
........ library/
........ middleware/
........ model/
........ __init__.py
........ logger.py
........ route.py
... .editorconfig
... .env.example
... .gitignore
... README.md
... requirements.txt
... run.py
```

## Step By Step
Open your Terminal :
```sh
$ sudo apt-get install python3.7-dev libmysqlclient-dev
$ git clone https://github.com/yuliandwiwidodo/flask-chat-api
$ cd flask-chat-api
$ cp .env.example .env
$ virtualenv -p python3.7 virenv
$ source virenv/bin/activate
$ pip3.7 install -r requirements.txt
$ python main.py
```
## Who do I talk to? ##

If you have any questions, don't hesitate to ask us in  <yulian.dwi.widodo@gmail.com>

**Yulian Dwi Widodo**