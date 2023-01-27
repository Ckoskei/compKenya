- creating virtual env: myenv
    pythn -m venv <name>

- activating virtual env: 
    .\<name>\Scripts\activate(windows) | source <name>/bin/activate(linux)


- deactivating virtual env: 
    deactivate

- installing django: 
    pip install django / python -m pip install django

- checking django version:
     python -m django --version

- create first django project: demoproject
    django-admin | manage.py
    django-admin startproject <name> .

- Run development server:
    python manage.py runserver

- Migrations, 
    - python .\manage.py makemigrations = data is loaded in db(backend)
    - python .\manage.py migrate

- Create Superuser
    python .\manage.py createsuperuser
- Admin, 


- Create first django app:my app
    django-admin startapp <name> | python .\manage.py startapp <name>

    // manage = is provided locally

    sqlmigrate : myapp
        python .\manage.py sqlmigrate <name_app> <name_migrations> dont include _initial.py
    showmigrations:
    python .\manage.py showmigratio
ns  = where X means its already done
