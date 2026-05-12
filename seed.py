from database import abrir_conexao, criar_tabelas

def banco():
    conexao = abrir_conexao("ideias.db")
    criar_tabelas(conexao)
    cursor = conexao.cursor()

    # Linguagens
    linguagens = [
        "INSERT INTO linguagens (nome_linguagem, domina) VALUES ('Java', 0)",
        "INSERT INTO linguagens (nome_linguagem, domina) VALUES ('Python', 0)",
        "INSERT INTO linguagens (nome_linguagem, domina) VALUES ('HTML', 0)",
        "INSERT INTO linguagens (nome_linguagem, domina) VALUES ('CSS', 0)",
        "INSERT INTO linguagens (nome_linguagem, domina) VALUES ('JavaScript', 0)",
        "INSERT INTO linguagens (nome_linguagem, domina) VALUES ('TypeScript', 0)",
        "INSERT INTO linguagens (nome_linguagem, domina) VALUES ('React', 0)",
    ]

    for linguagem in linguagens:
        cursor.execute(linguagem)
    
    conexao.commit()

if __name__ == "__main__":
    banco()