# flask-postgresql-docker
This repo is a simple Newsletter project. This process is for WINDOWS10.

#### First, download and install python and docker-desktop

`<link>` : <https://www.python.org/downloads/windows/>

`<link>` : <https://docs.docker.com/desktop/install/windows-install/>

#### Second, install requirements

`pip install -r requirements.txt`

#### Third, set environment variables

    SET FLASK_APP=project
    SET FLASK_DEBUG=True
    SET POSTGRES_USER=nladmin
    SET POSTGRES_PASSWORD=admin123
    SET POSTGRES_HOST=localhost
    SET POSTGRES_PORT=5432
    SET POSTGRES_DB=newsletter

#### Lastly, dockerize postgresql and start Flask App.

    C:\%PATH%\NewsLetter> docker compose up
  
    C:\%PATH%\NewsLetter> python -m flask run

#### Thats all!

> Login page credentials are "admin:admin123".

> You can just run " **app_run.bat** "

### Resources:

[1] https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

[2] https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application

[3] https://haseebmajid.dev/blog/simple-app-flask-sqlalchemy-and-docker

[4] https://bulma.io/documentation/

[5] https://roytuts.com/docker-compose-dockerizing-flask-mysql-app/
