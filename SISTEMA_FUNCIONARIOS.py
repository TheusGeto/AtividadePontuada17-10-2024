#ALUNOS: Matheus Gabriel e Iury Alves
import os
import time
from dataclasses import dataclass
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
BASE_FUNCIONARIOS = create_engine("sqlite:///meubanco.db")

# Criando conexão com o banco de dados
Session = sessionmaker(bind=BASE_FUNCIONARIOS)
session = Session()

Base = declarative_base()

os.system("cls || clear")

# Classe para representar um funcionario
class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(String, unique=True)
    setor = Column(String)
    funcao = Column(String)
    salario = Column(float)
    telefone = Column(String)

    def __init__(self, nome, cpf, setor,funcao, telefone,  salario, sexo, idade):  # Inicia os atributos do objeto, define os valores iniciais dos dados
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.telefone = telefone
        self.setor = setor
        self.funcao = funcao
        self.salario = salario

Base.metadata.create_all(BASE_FUNCIONARIOS)  # Cria as tabelas no banco de dados
        
        

def limpar_terminal():  # Para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_funcionario():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("Cpf: ")
    setor = input("Setor: ")
    funcao = input("Função: ")
    salario = float(input("Salario: "))
    telefone = input("Telefone: ")

    novo_funcionario = Funcionario(nome, idade, cpf, setor, funcao, salario, telefone)
    session.add(novo_funcionario)
    session.commit
    print("Funcionário adicionado com sucesso!")