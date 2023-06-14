'''Neste desafio você irá implementar uma aplicação de integração com SQLite
com base em um esquema relacional disponibilizado. Sendo assim, utilize o
esquema dentro do contexto de cliente e conta para criar as classes de sua API.
Essas classes irão representar as tabelas do banco de dados relacional dentro
da aplicação.'''

import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine, inspect
from sqlalchemy import select

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key = True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False)
    endereco = Column(String(150), nullable=False)

    conta = relationship("Conta", back_populates="cliente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"
    

class Conta(Base):
    __tablename__ = "conta"
    
    id = Column(Integer, primary_key = True)
    tipo = Column(String(2), nullable = False)
    agencia = Column(Integer, nullable = False)
    numero = Column(String(4), nullable = False)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable = False)
        
    cliente = relationship("Cliente", back_populates="conta")
    
    def __repr__(self):
    	return f"Conta(id={self.id},tipo={self.tipo}, agencia={self.agencia}, numero={self.numero}, id_cliente={self.id_cliente}, saldo={self.saldo})"
    	
    print(Cliente.__tablename__)
    print(Conta.__tablename__)
    
    #Conectando com o banco de dados e criando as classes como tabelas nele
    
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    
    #Verificacao
    
    inspector_engine = inspect(engine)
    print(inspector_engine.get_table_names())
    
    with Session(engine) as session:
    	cliente_01 = Cliente(
    		nome='Mariana'
    		cpf='12203364499'
    		endereco='Rua Codigo Github, Rio de Janeiro"
    	)
    	
    	cliente_02 = Cliente(
    		nome='Arthur'
    		cpf='98827701100'
    		endereco='Rua Curso DIO, Rio de Janeiro'
    	)
    	
    	cliente_03 = Cliente(
    		nome='Fulane'
    		cpf='24405563966'
    		endereco='Rua Linguagem Python, São Paulo'
    	)
    	
    	session.add_all([cliente_01,cliente_02,cliente_03])
    	session.commit()
    	
    	#Acessando clientes através de uma filtragem
    	
    	stmt = select(Cliente).where(Cliente.nome.in_(['Mariana']))
    	for resultado in session.scalars(stmt):
    		print(resultado)
    		
    	stmt_ordenacao = select(Cliente).order_by(Cliente.nome.desc())
    	for resultado in session.scalars(stmt_ordenacao):
    		print(resultado)
    
    with Session(engine) as session:
    	conta_01 = Conta(
    		tipo = 'CC'
    		agencia = 0001
    		numero = '101'
    		saldo = 650
    		id_cliente = 7 
    	)
    	
    	conta_02 = Conta(
    		tipo = 'CC'
    		agencia = 0001
    		numero = '102'
    		saldo = 651
    		id_cliente = 4
    	)
    	
    	conta_03 = Conta(
    		tipo = 'CP'
    		agencia = 0001
    		numero = '900'
    		saldo = 999.95
    		id_cliente = 100
    	)
    	
    	session.add_all([conta_01,conta_02,conta_03])
    	session.commit()
    	
    	stmt = select(Conta).where(Conta.cliente_id.in_([7]))
    	
    	for conta in session.scalars(stmt):
    		print(conta)
    		
    		
    stmt_join = select(Cliente.nome, Conta.tipo, Conta.saldo).join_from(Cliente, Conta)
    for resultado in session.scalars(stmt_join):
    	print(resultado)
    
    connection = engine.connect()
    resultados = connection.execute(stmt_join).fetchall()
    
    for resultado in resultados:
    	print(resultado)	
    	
    session.close()
    		
