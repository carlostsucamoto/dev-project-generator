from database import abrir_conexao
from queries import sortear, listar_linguagem, listar_bibliotecas, adicionar_ideias

conexao = abrir_conexao("ideias.db")
print(sortear(conexao, "projeto", "intermediario"))