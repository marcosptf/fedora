"""
+Capitulo 9 - Flask Login + Flask Admin + Flask Redis + Memcached + PostgreSql
https://aws.amazon.com/pt/elasticache/what-is-redis/
https://pypi.python.org/pypi/Flask-And-Redis/0.7
https://pypi.python.org/pypi/Flask-Cache-Redis-Cluster/0.0.5
https://pypi.python.org/pypi/Flask-PyMemcache/0.0.5
https://pypi.python.org/pypi/Flask-Login/0.4.0
https://pypi.python.org/pypi/Flask-Admin/1.5.0
http://flask-admin.readthedocs.io/en/latest/

a intencao deste capitulo, ehcriar um miniblog usando todas estas 
tecnologias, com exemplos claros e bem detalhados;


"""


from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here



# Flask and Flask-SQLAlchemy initialization here
#admin = Admin(app, name='microblog', template_mode='bootstrap3')
#admin.add_view(ModelView(User, db.session))
#admin.add_view(ModelView(Post, db.session))



app.run()



















