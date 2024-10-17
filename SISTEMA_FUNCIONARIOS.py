#ALUNOS: Matheus Gabriel e Iury Alves
import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
BASE_FUNCIONARIOS = create_engine("sqlite:///meubanco.db")

# Criando caminho proo banco de dados
Session = sessionmaker(bind=BASE_FUNCIONARIOS)
session = Session()

Base = declarative_base()

# Classe para representar um funcionario
class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(String, unique=True)
    setor = Column(String)
    funcao = Column(String)
    salario = Column(Float)
    telefone = Column(String)

    def __init__(self, nome, idade, cpf, setor, funcao, salario, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.setor = setor
        self.funcao = funcao
        self.salario = salario

Base.metadata.create_all(BASE_FUNCIONARIOS)  # Cria as tabelas no banco de dados

def limpar_terminal():  # Para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_funcionario():#Para adicionar o funcionario novo
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    setor = input("Setor: ")
    funcao = input("Função: ")
    salario = float(input("Salário: "))
    telefone = input("Telefone: ")

    novo_funcionario = Funcionario(nome, idade, cpf, setor, funcao, salario, telefone)
    session.add(novo_funcionario)
    session.commit()
    print("Funcionário adicionado com sucesso!")

def consultar_funcionario():#Consulta de funcionarios
    cpf = input("Digite o CPF do funcionário: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        print(f"Nome: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}, Função: {funcionario.funcao}, Salário: {funcionario.salario}, Telefone: {funcionario.telefone}")
    else:#caso o CPF nao esteja certo, ou nao esteja no sistema
        print("Funcionário não encontrado.")

def atualizar_funcionario():#Atualizando Funcionarios
    cpf = input("Digite o CPF do funcionário que deseja atualizar: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        funcionario.nome = input("Novo Nome: ")
        funcionario.idade = int(input("Nova Idade: "))
        funcionario.setor = input("Novo Setor: ")
        funcionario.funcao = input("Nova Função: ")
        funcionario.salario = float(input("Novo Salário: "))
        funcionario.telefone = input("Novo Telefone: ")

        session.commit()
        print("Funcionário atualizado com sucesso!")
    else:#caso o CPF nao esteja certo, ou nao esteja no sistema
        print("Funcionário não encontrado.")

def excluir_funcionario():#Excluindo funcionarios
    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print("Funcionário excluído com sucesso!")
    else:#caso o CPF nao esteja certo, ou nao esteja no sistema
        print("Funcionário não encontrado.")

def listar_funcionarios():#Listando os funcionarios
    funcionarios = session.query(Funcionario).all()
    for f in funcionarios:
        print(f"ID: {f.id}, Nome: {f.nome}, CPF: {f.cpf}, Setor: {f.setor}, Função: {f.funcao}, Salário: {f.salario}, Telefone: {f.telefone}")

def main(): #Funçao para o menu
    while True:
        limpar_terminal()
        print("RH System")
        print("1 - Adicionar funcionário")
        print("2 - Consultar um funcionário")
        print("3 - Atualizar os dados de um funcionário")
        print("4 - Excluir um funcionário")
        print("5 - Listar todos os funcionários")
        print("0 - Sair do sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_funcionario()
        elif opcao == '2':
            consultar_funcionario()
        elif opcao == '3':
            atualizar_funcionario()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '5':
            listar_funcionarios()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

        input("Pressione Enter para continuar...")

if __name__ == "__main__": # verifica se o arquivo está sendo executado diretamente.
    main()