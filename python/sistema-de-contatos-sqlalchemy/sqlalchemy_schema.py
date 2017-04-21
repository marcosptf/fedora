# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String

class Contatos(Base):
    __tablename__ = "contatos"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(250)) #colocar not null
    email = Column(String(50))
    whatsapp = Column(String(12))
    facebook = Column(String(50))
    twitter = Column(String(50))
    website = Column(String(50))
    endereco = Column(String(250))
    bairro = Column(String(50))
    cidade = Column(String(50))
    estado = Column(String(50))
    
    def __repr__(self):
        return """
        <Contatos(name='%s', email='%s', whatsapp='%s', facebook='%s', twitter='%s', website='%s',
        endereco='%s',bairro='%s',cidade='%s',estado='%s')>
        """ % (self.id, self.nome, self.email, self.whatsapp, self.facebook, self.twitter,self.website,
        self.endereco, self.bairro, self.cidade, self.estado)




