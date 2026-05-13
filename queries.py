from database import abrir_conexao
import random


def sortear(conexao, categoria, dificuldade):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ideias WHERE categoria = ? AND dificuldade = ?", (categoria, dificuldade))
    resultados = cursor.fetchall()
    sorteio = random.choice(resultados)
    return sorteio
if __name__ == "__main__":
    sortear()

def listar_linguagem(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM linguagens")
    resultados = cursor.fetchall()
    return resultados

def listar_bibliotecas(conexao, id_linguagem):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM bibliotecas WHERE id_linguagem_id = ?", (id_linguagem,))
    resultados = cursor.fetchall()
    return resultados

def adicionar_ideias(conexao, nome_ideias, descricao, categoria, dificuldade):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES (?, ?, ?, ?)", (nome_ideias, descricao, categoria, dificuldade))
    resultados = conexao.commit()
    return resultados
