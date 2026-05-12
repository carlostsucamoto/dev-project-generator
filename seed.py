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

    # Bibliotecas
    bibliotecas = [
        # Java (id=1)
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Spring Boot', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Spring Security', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Spring Cloud', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('JPA', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('JDBC', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Thymeleaf', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('iText', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('RabbitMQ', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Kafka', 0, 1)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('JWT', 0, 1)",
        # Python (id=2)
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Pandas', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Dash', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Plotly', 0, 2)",
        # JavaScript (id=5)
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('React', 0, 5)",
        # TypeScript (id=6)
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('TypeScript', 0, 6)",
    ]

    for biblioteca in bibliotecas:
        cursor.execute(biblioteca)
    conexao.commit()

if __name__ == "__main__":
    banco()