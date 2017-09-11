
import string
import random
from user import User
from werkzeug.security import generate_password_hash
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String

def connect(user='postgres', password='', db='postgres', host='localhost', port=5432):

    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    conn = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=conn, reflect=True)

    return conn, meta


def build_sample_db():

    conn, meta = connect()

    usuario = Table('user', meta,
        #Column('first_name', String, primary_key=True),
        Column('first_name', String),
        Column('last_name', String),
        Column('login', String),
        Column('email', String),
        Column('password', String),
        schema='public'
    )

    meta.drop_all(conn)
    meta.create_all(conn)

    """
    
    test_user = User(login="test", password=generate_password_hash("test"))
    db.session.add(test_user)    
    
    first_names = [
        'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie','Sophie', 'Mia',
        'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
        'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    ]

    last_names = [
        'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
        'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
        'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    ]

    for i in range(len(first_names)):
      
        user = User()
        user.first_name = first_names[i]
        user.last_name = last_names[i]
        user.login = user.first_name.lower()
        user.email = user.login + "@example.com"
        user.password = generate_password_hash(''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10)))
        db.session.add(user)

    db.session.commit()
    """

    usuarios = [
        { "first_name":"java", "last_name":"script", "login":"java", "email":"java@java.com", "password":"123456"  },
        { "first_name":"java1", "last_name":"script1", "login":"java1", "email":"java@java.com", "password":"123456"  },
        { "first_name":"java2", "last_name":"script2", "login":"java2", "email":"java@java.com", "password":"123456"  },
        { "first_name":"java3", "last_name":"script3", "login":"java3", "email":"java@java.com", "password":"123456"  },
        { "first_name":"java4", "last_name":"script4", "login":"java4", "email":"java@java.com", "password":"123456"  }        
    ]
   
    conn.execute(meta.tables['user'].insert, usuarios)
    
    return

