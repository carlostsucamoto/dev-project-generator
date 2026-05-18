from database import abrir_conexao
import random


def sortear(conexao, categoria, dificuldade):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ideias WHERE categoria = ? AND dificuldade = ?", (categoria, dificuldade))
    resultados = cursor.fetchall()
    if not resultados:
        return None
    sorteio = random.choice(resultados)
    return sorteio

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
    conexao.commit()
def marcar_realizado(conexao, id_ideia):
    cursor = conexao.cursor()
    cursor.execute("UPDATE ideias SET realizado = 1 WHERE id_ideias = ?", (id_ideia,))      
    conexao.commit()
if __name__ == "__main__":
    pass
