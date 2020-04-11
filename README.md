Health of India: Fight Covid19
==============================

An application to map symptomatic patients of covid19 on map and collect continuous health updates from individuals. Visit
[covid19.thepodnet.com](https://covid19.thepodnet.com).

![image](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)
![image](https://img.shields.io/badge/code%20style-black-000000.svg)
[![GitHub license](https://img.shields.io/github/license/Podnet/Fight-Covid19.svg?logo=github)](https://github.com/Podnet/Fight-Covid19/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Podnet/Fight-Covid19.svg?logo=github)](https://github.com/Podnet/Fight-Covid19/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/Podnet/Fight-Covid19.svg?logo=github&color=teal)](https://github.com/Podnet/Fight-Covid19/network/members) 
[![GitHub top language](https://img.shields.io/github/languages/top/Podnet/Fight-Covid19?color=blue&logo=python)](https://github.com/Podnet/Fight-Covid19)

License
:   MIT

Setup
-----

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Podnet/Fight-Covid19?logo=github)](https://github.com/Podnet/Fight-Covid19/) 
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Podnet/Fight-Covid19?color=bluevoilet&logo=github)](https://github.com/Podnet/Fight-Covid19/commits/) 
[![GitHub repo size](https://img.shields.io/github/repo-size/Podnet/Fight-Covid19?logo=github)](https://github.com/Podnet/Fight-Covid19/)

1.  Clone the repository
    ```console
    $ git clone https://github.com/Podnet/Fight-Covid19
    ```

2.  Create a virtual environment using virtualenv or venv.
     ```console
     $ virtualenv -p python3 venv/ 
     $ source venv/bin/activate
     ```

3.  Install python packages
     ```console
     $ pip3 install -r requirements/local.txt
     ```

4.  Install OS dependencies (For linux systems only, others have to install it manually)
    ```console
    $ sudo ./utility/install\_os\_dependencies.sh install
    ```

5.  Setup Postgres database (assuming you have already installed it)
    ```console
    $ sudo -i -u postgres 
    $ createdb fight_covid19 
    $ createuser --interactive 
    Enter name of role to add: <username>
    Shall the new role be a superuser? (y/n) y
    ```

6.  Point django to the database instance. Create a .env file with the
    following content:
    ```env
    # These variables are used locally
    DJANGO_SETTINGS_MODULE=config.settings.local
    DJANGO_SECRET_KEY=07FGJkO46oezqJsAOVuUho0rSfB6jMdOZmmdYMdIDYJ8py17qF4IUC8QNNGbLiLE
    DATABASE_NAME=fight_covid19
    DATABASE_USER=apoorva
    DATABASE_PASSWORD=apple007
    DATABASE_HOST=127.0.0.1
    DATABASE_PORT=5432
    BROKER_URL=redis://localhost:6379
    CELERY_RESULT_BACKEND=redis://localhost:6379
    CELERY_ACCEPT_CONTENT=application/json
    CELERY_TASK_SERIALIZER=json
    CELERY_RESULT_SERIALIZER=json
    REDIS_URL=redis://localhost:6379/1

    ```
    
    ```console
    $ touch .env
    $ nano .env
    <paste the contents of the file>
    Do the same in config/.env
    $ touch config/.env
    $ nano config.env
    ```
    
    
7.  Run project locally
    ```console
    $ python manage.py runserver
    ```

Todo
----

1.  Update this README docs to post instructions for installation
2.  Tasks to perform
3.  Optimizations to perform on database

Settings
--------

Moved to
[settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

Basic Commands
--------------

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out
    the form. Once you submit it, you'll see a "Verify Your E-mail
    Address" page. Go to your console to see a simulated email
    verification message. Copy the link into your browser. Now the
    user's email should be verified and ready to go.
-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with py.test

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS
compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Sentry

Sentry is an error logging aggregator service. You can sign up for a
free account at <https://sentry.io/signup/?code=cookiecutter> or
download and host it yourself. The system is setup with reasonable
defaults, including 404 logging and integration with the WSGI
application.

You must set the DSN url in production.

### API Endpoints

- **users** : ``GET,POST,PUT,DELETE,OPTIONS`` : Details of users registered
    - **current_user** : ``GET`` : Current User
- **healthentry** : ``GET,POST`` : Entry by the users
- **coronacases** : ``GET`` : Total Cases of Corona
- **healthstat** : ``GET`` : Health Stats generated by us

## Issues

[![GitHub issues](https://img.shields.io/github/issues/Podnet/Fight-Covid19?logo=github)](https://github.com/Podnet/Fight-Covid19/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=git&logoColor=white)](https://github.com/Podnet/Fight-Covid19/pulls) 
[![GitHub last commit](https://img.shields.io/github/last-commit/Podnet/Fight-Covid19?logo=github)](https://github.com/Podnet/Fight-Covid19/)

> // No Issues now.

**NOTE**: **Feel free to [open issues](https://github.com/Podnet/Fight-Covid19/issues/new/choose)**. Make sure you follow the Issue Template provided.

## Contribution Guidelines

[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/Podnet/Fight-Covid19?logo=git&logoColor=white)](https://github.com/Podnet/Fight-Covid19/compare) 
[![GitHub contributors](https://img.shields.io/github/contributors/Podnet/Fight-Covid19?logo=github)](https://github.com/Podnet/Fight-Covid19/graphs/contributors) 

- Write clear meaningful git commit messages (Do read [this](http://chris.beams.io/posts/git-commit/)).

- Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check [this](https://github.com/blog/1506-closing-issues-via-pull-requests) for more info)

- When you make very very minor changes to a PR of yours (like for example fixing a text in button, minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at [here](https://davidwalsh.name/squash-commits-git))

- When you're submitting a PR for a UI-related issue, it would be really awesome if you add a screenshot of your change or a link to a deployment where it can be tested out along with your PR. It makes it very easy for the reviewers and you'll also get reviews quicker.

- Please follow the [PR Template](https://github.com/Podnet/Fight-Covid19/blob/master/.github/PULL_REQUEST_TEMPLATE.md) to create the PR.

- Always create PR to `develop` branch.

- Please read our [Code of Conduct](./CODE_OF_CONDUCT.md).

- Refer [this](https://github.com/Podnet/Fight-Covid19/blob/master/CONTRIBUTING.md) for more.


[![with love](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/Podnet/Fight-Covid19/) [![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://github.com/Podnet/Fight-Covid19/) [![smile please](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/Podnet/Fight-Covid19/)
