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