# rotten-potatoes-api

School project.
Forked from [flask-jwt-auth](https://github.com/realpython/flask-jwt-auth)

### Env variables
Copy/paste "*.env.example*" and rename it to "*.env*" before opening it with a text editor. Set all the variables after the comment.

### Create DB

Create the databases in `psql`:

```sh
$ psql
# create database flask_jwt_auth
# create database flask_jwt_auth_test
# \q
```

Create the tables and run the migrations:

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
```

### Run the Application

```sh
$ python manage.py runserver
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)

> Want to specify a different port?

> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
