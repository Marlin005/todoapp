
import re

# путь к базе

db_link_p = "postgres://admin:oocooSh7@postgres.host:5432/my_db"
db_link_s = "sqlite:///C:/Users/admin/site_db.sqlite3"
# def parse_db_url(db_link):
# 	if db_link.startwith("postgres"):
# 		dic  = f{

# 		}
# 		pass

# args = "-t 500 -x -c 3 -d --long-option 456 -testing weird-behaviour"
args =  "sqlite:///C:/Users/admin/site_db.sqlite3"
matches = re.findall(r'(-///?[\w-]+)(.*?)(?= -|$)', args)

result = {}
for match in matches:
    result[match[0]] = True if not match[1] else match[1].strip()

print (result)
# # пусть в settings.py
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# # требуется такую строку 
# # postgres://admin:oocooSh7@postgres.host:5432/my_db

#  # развернуть в словарь на выходе из функции
#  # То есть такая ссылка воспринимается как 
#  # postgres://<USER>:<PASSWORD>@<HOST>: <PORT>/<NAME>
#  {
# 	'ENGINE': 'django.db.backends.postgresql_psycopg2', 'USER': 'admin',
# 	'PASSWORD': 'oocooSh7',
# 	'HOST': 'postgres.host',
# 	'PORT': '5432',
# 	'NAME': 'my_db'
# } 

# # если на вход приходит строка
# # sqlite:///C:/Users/admin/site_db.sqlite3

# {
# 	'ENGINE': 'django.db.backends.sqlite3',
# 	'NAME': 'C:/Users/admin/site_db.sqlite3'
# }
