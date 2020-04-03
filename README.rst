Health of India: Fight Covid19
==============================

An application to map symptomatic patients of covid19 on map and collect continuous health updates from individuals.
Visit covid19.thepodnet.com_.

.. _covid19.thepodnet.com: https://covid19.thepodnet.com


.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

Setup
-----
1. Clone the repository
    ::
    
    $ git clone https://github.com/meticulousCraftman/Fight-Covid19
  
2. Create a virtual environment using virtualenv or venv.
    ::
    
    $ virtualenv -p python3 venv/
    $ source venv/bin/activate

3. Install python packages
    ::
    
    $ pip3 install -r requirements/local.txt
    
4. Install OS dependencies (For linux systems only, others have to install it manually)
    ::
    
    $ sudo ./utility/install_os_dependencies.sh install

5. Setup Postgres database (assuming you have already installed it)
    ::
    
    $ sudo -i -u postgres
    $ createdb fight_covid19
    $ createuser --interactive
      Enter name of role to add: <username>
      
      Shall the new role be a superuser? (y/n) y
    
6. Point config.settings.base.py file to the correct database instance.
6. Run project locally
    ::
    
    $ python manage.py runserver

Todo
----
1. Update this README docs to post instructions for installation
2. Tasks to perform
3. Optimizations to perform on database


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy fight_covid19

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.




