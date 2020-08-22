# todoapp
#запуск окружения

#source my-venv/bin/activate
#cd todoapp
#python manage.py runserver


#установка окружения
#$ pip install virtualenv

#Теперь перейдите в папку где вы будете хранить код
#для этого модуля, и создайте там вирутальное
#окружение:
#virtualenv my-venv --python=python3.7 (узнать версию)

#запуск окружения

#source my-venv/bin/activate



#установка django
#(my-venv) $ pip install Django==2.1.5
#проверить

#(my-venv) $ python
#>>> import django
#>>> django.get_version()
#'2.1.5'
#>>> exit()
#(my-venv) $

#Чтобы выйти из окружения, используйте команду
#deactivate. Можно после выхода
#проверить, что действительно в основную систему
#Django установлена не была:
#(my-venv) $ deactivate
#$ python
#>>> import django
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#ModuleNotFoundError: No module named 'django'
#>>>


#pip freeze
#dj-database-url==0.5.0
#Django==2.1.5
#django-heroku==0.3.1
#Pillow==7.1.2
#psycopg2==2.8.5
#pytz==2020.1
#q==2.6
#whitenoise==5.1.0


#Create database tables

#./manage.py migrate
#(Optional) Create a super user to rule other users

#./manage.py createsuperuser
#Run django server

#./manage.py runserver


#запуск сервера
#cd 12 cd todoapp
#python manage.py runserver

#settings DEBUG = True
