@ECHO OFF
:: This batch file uses for dockerizing postgresql, setting anvironment variables and running flask app 

:: python -m pip install virtualenv
:: python -m virtualenv .venv
:: .venv\Scripts\activate
python -m pip install -r requirements.txt

SET FLASK_APP=project
SET FLASK_DEBUG=True
SET POSTGRES_USER=nladmin
SET POSTGRES_PASSWORD=admin123
SET POSTGRES_HOST=localhost
SET POSTGRES_PORT=5432
SET POSTGRES_DB=newsletter

START cmd /k "docker compose up"
START cmd /k "python -m flask run"

START http://localhost:5000

:: PAUSE