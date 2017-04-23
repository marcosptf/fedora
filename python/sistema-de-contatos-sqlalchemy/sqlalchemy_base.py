# -*- coding: utf-8 -*-
#criando uma instancia do create_engine
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine("mysql://root:123456@localhost:3306/sistema_de_contatos", echo=True)
