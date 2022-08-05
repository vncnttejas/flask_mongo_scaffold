## Basic Flask Scaffolding with MongoDB

- [Basic Flask Scaffolding with MongoDB](#basic-flask-scaffolding-with-mongodb)
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Get Started](#get-started)
    - [Poetry way](#poetry-way)
    - [Global python/virtualenv way](#global-pythonvirtualenv-way)

### Description

A simple Flask+Mongo scaffold to quickly get started with app development. Highlights are listed in the list below.

- Uses `python-dotenv` to fetch env variables from `.env` file
- Uses the Flask Mongo for Mongo DB connection
- Uses blueprint to create a suite of roots, a sample suite called [animals](./app/animals) are provided


### Prerequisites
- Check the [pyproject.toml](./pyproject.toml) file
- Needs poetry cli [python package](https://python-poetry.org/) (Optional)
- Needs Mongo DB string to be based in the .env file

### Get Started

#### Poetry way
- Install the dependencies with poetry
  ```shell
  $ poetry install
  ```
- Set poetry shell
  ```shell
  $ poetry shell
  ```
- Make a copy of the `.env.example` file and name it as `.env`
- Set the `db` and `env` values in .env file
- Run the script
  ```shell
  $ python app.py
  ```

#### Global python/virtualenv way
- Create a virtual env
- Use the `requirements.txt` file to install the dependencies
- Make a copy of the `.env.example` file and name it as `.env`
- Set the `db` and `env` values in .env file
- Run `python app.py` to start the app

