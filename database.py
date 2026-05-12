import sqlite3

def abrir_conexao(ideias_db):
    try:

        conexao = sqlite3.connect(ideias_db)
        return conexao
    
    except sqlite3.Error as e:
        return f"Erro: {e}"


def criar_tabelas(conexao):
    cursor = conexao.cursor()
    linguagens = """
        CREATE TABLE IF NOT EXISTS linguagens  (
        id_linguagem INTEGER primary key,
        nome_linguagem VARCHAR NOT NULL,
        domina BOOLEAN NOT NULL
        );
    """
    cursor.execute(linguagens)
    conexao.commit()

    bibliotecas = """
        CREATE TABLE IF NOT EXISTS bibliotecas (
        id_biblioteca INTEGER primary key,
        id_linguagem_id INTEGER NOT NULL,
        nome_biblioteca VARCHAR NOT NULL,
        domina BOOLEAN NOT NULL,
        FOREIGN KEY (id_linguagem_id) REFERENCES linguagens (id_linguagem)
        );
    """
    cursor.execute(bibliotecas)
    conexao.commit()

    ideias = """
        CREATE TABLE IF NOT EXISTS ideias (
        id_ideias INTEGER primary key,
        nome_ideias VARCHAR NOT NULL,
        descricao VARCHAR NOT NULL,
        categoria VARCHAR NOT NULL,
        dificuldade VARCHAR NOT NULL
        );
    """
    cursor.execute(ideias)
    conexao.commit()

    ideias_linguagens = """
        CREATE TABLE IF NOT EXISTS ideias_linguagens (
        id_ideias_linguagens INTEGER primary key,
        id_linguagem_id INTEGER NOT NULL,
        id_ideias_id INTEGER NOT NULL,
        FOREIGN KEY (id_linguagem_id) REFERENCES linguagens (id_linguagem),
        FOREIGN KEY (id_ideias_id) REFERENCES ideias (id_ideias)
        );
    """
    cursor.execute(ideias_linguagens)
    conexao.commit()
    estudos = """
        CREATE TABLE IF NOT EXISTS estudos (
        id_estudos INTEGER primary key,
        id_bibliotecas_id INTEGER NOT NULL,
        FOREIGN KEY (id_bibliotecas_id) REFERENCES bibliotecas (id_biblioteca)

        );
    """
    cursor.execute(estudos)
    conexao.commit()