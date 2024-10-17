# Atividade

## Objetivo: Em dupla, usando funções implemente um CRUD com os dados informados abaixo.

class Funcionario:
    def _init__(self, nome, idade, cpf, setor, funcao, salario, telefone)

# Tecnologias:
Será necessário utilizar as tecnologias abaixo:
-ORM: SQLAlchemy
-Banco de dados: SQLite
-Versionamento: Git

## Resultado esperado:
Um sistema onde o usuário veja um menu e escolher dentre as opções disponíveis.

RH System
1- Adicionar funcionário
2- Consultar um funcionário
3- Atualizar os dados de um funcionário
4- Excluir um funcionário
5- Listar todos os funcionários
0- Sair do sistema.

Menu deve ser exibido apos as açoes

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com o banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

Base = declarative_base()