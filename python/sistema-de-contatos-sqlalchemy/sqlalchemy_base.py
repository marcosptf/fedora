# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("mysql://root:123456@localhost/sistema_de_contatos",
                      encoding='utf8mb4',
                      echo=True)    

