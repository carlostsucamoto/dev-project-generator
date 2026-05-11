import sqlite3

def abrir_conexao(ideias_db):
    try:

        conexao = sqlite3.connect(ideias_db)
        return conexao
    except sqlite3.Error as e:
        return f"Erro: {e}"