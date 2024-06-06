from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymongo


engine = create_engine("sqlite:///meu_banco_de_dados.db")


Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String)


class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    idcliente = Column(Integer)
    saldo = Column(Integer)


Base.metadata.create_all(engine)  # Cria as tabelas no banco de dados

Session = sessionmaker(bind=engine)
session = Session()

cliente1 = Cliente(nome="João", cpf="123456789", endereco="Rua A")
conta1 = Conta(tipo="Corrente", agencia="123", num=1001, idcliente=1, saldo=1000.0)

session.add(cliente1)
session.add(conta1)
session.commit()

# Exemplo: Recuperar todos os clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(cliente.nome, cliente.cpf)

# import pymongo

client = pymongo.MongoClient("mongodb://seu_host:27017/")
db = client["meu_banco_nosql"]
bank_collection = db["bank"]

cliente_doc = {
    "nome": "João",
    "cpf": "123456789",
    "endereco": "Rua A"
}

conta_doc = {
    "tipo": "Corrente",
    "agencia": "123",
    "num": 1001,
    "idcliente": 1,
    "saldo": 1000.0
}

bank_collection.insert_one(cliente_doc)
bank_collection.insert_one(conta_doc)

# Exemplo: Recuperar todas as contas
contas = bank_collection.find()
for conta in contas:
    print(conta)
