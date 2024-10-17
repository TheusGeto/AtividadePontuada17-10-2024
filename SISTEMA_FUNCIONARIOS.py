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

# Estrutura de dados:
@dataclass
# Classe para representar uma pessoa
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome, cpf, setor,funcao, telefone,  salario, sexo, idade):  # Inicia os atributos do objeto, define os valores iniciais dos dados
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.telefone = telefone
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        
        

def limpar_terminal():  # Para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')