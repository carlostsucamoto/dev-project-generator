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
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('os', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('NumPy', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('OpenPyXL', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Flask', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('BeautifulSoup', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Selenium', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('shutil', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('pathlib', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('PyQt5', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Tkinter', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Requests', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('schedule', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Pillow', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('Streamlit', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('FastAPI', 0, 2)",
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('SQLite3', 0, 2)",
        # JavaScript (id=5)
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('React', 0, 5)",
        # TypeScript (id=6)
        "INSERT INTO bibliotecas (nome_biblioteca, domina, id_linguagem_id) VALUES ('TypeScript', 0, 6)",
    ]
    for biblioteca in bibliotecas:
        cursor.execute(biblioteca)
    conexao.commit()

    # Ideias
    ideias = [
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Calculadora com interface gráfica', 'Crie uma calculadora funcional com interface visual usando PyQt5 ou Tkinter, praticando eventos e componentes gráficos.', 'projeto', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Conversor de moedas e temperatura', 'Desenvolva um conversor que transforma valores entre moedas e unidades de temperatura, consumindo APIs externas.', 'projeto', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('To-do list com console', 'Construa uma lista de tarefas no terminal com opções de adicionar, remover e listar tarefas, salvando em arquivo.', 'projeto', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Gerador de senhas', 'Crie um gerador de senhas seguras com opções de tamanho e tipos de caracteres, com interface gráfica ou console.', 'projeto', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Renomeador de arquivos em massa', 'Automatize a renomeação de múltiplos arquivos em uma pasta com regras personalizadas usando os e pathlib.', 'projeto', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Gerador automático de relatórios', 'Gere relatórios em PDF ou Excel automaticamente a partir de dados em CSV, usando Pandas e OpenPyXL.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Sistema de backup automático', 'Desenvolva um sistema que copia arquivos importantes para uma pasta de backup automaticamente usando schedule e shutil.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('App de controle de água', 'Crie um app para registrar e acompanhar o consumo diário de água, com alertas e histórico visual.', 'projeto', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('App de treinos com histórico', 'Desenvolva um app para registrar treinos diários, acompanhar evolução e visualizar histórico em gráficos.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Chatbot no terminal', 'Construa um chatbot interativo no terminal que responde perguntas usando lógica condicional ou APIs externas.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Analisador de vídeos do YouTube', 'Crie uma ferramenta que busca e analisa métricas de vídeos do YouTube usando a API oficial do Google.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Sistema de cadastro de alunos', 'Desenvolva um sistema completo de cadastro de alunos com banco de dados, listagem e busca por nome ou matrícula.', 'projeto', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Sistema de biblioteca com empréstimos', 'Construa um sistema para gerenciar livros, usuários e controle de empréstimos com prazo de devolução.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('API REST para loja de produtos', 'Crie uma API completa para gerenciar produtos, categorias e pedidos de uma loja virtual.', 'projeto', 'avançado')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Sistema de votação simples', 'Desenvolva um sistema de votação com cadastro de candidatos, registro de votos e apuração de resultados.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Gerador de PDF de currículo', 'Crie uma ferramenta que gera currículos em PDF a partir de um formulário com dados pessoais e profissionais.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('App de delivery com status', 'Simule um app de delivery com cadastro de pedidos, atualização de status e histórico de entregas.', 'projeto', 'avançado')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Editor visual de currículos', 'Desenvolva um editor onde o usuário preenche seus dados e visualiza o currículo formatado em tempo real.', 'projeto', 'avançado')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Kanban pessoal', 'Crie um quadro Kanban para organizar tarefas em colunas como A fazer, Em andamento e Concluído.', 'projeto', 'intermediario')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Formulário com validação', 'Construa um formulário com campos de nome, email e senha com validação em tempo real e feedback visual.', 'desafio', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Previsão do tempo', 'Desenvolva uma página que exibe a previsão do tempo de qualquer cidade consumindo uma API meteorológica.', 'projeto', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Landing page responsiva', 'Crie uma landing page moderna e responsiva que funcione bem em desktop e celular.', 'desafio', 'iniciante')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Controle de tarefas com autenticação', 'Desenvolva um sistema de tarefas com login, cadastro de usuários e tarefas privadas por conta.', 'projeto', 'avançado')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Plataforma de adoção de pets', 'Crie uma plataforma completa com cadastro de animais, filtros de busca e autenticação de usuários.', 'projeto', 'avançado')",
        "INSERT INTO ideias (nome_ideias, descricao, categoria, dificuldade) VALUES ('Site pessoal com React e TypeScript', 'Refaça seu site pessoal usando React e TypeScript, com seções de portfólio, sobre e contato.', 'projeto', 'intermediario')",
    ]
    for ideia in ideias:
        cursor.execute(ideia)
    conexao.commit()

    # Estudos - todas as bibliotecas Python (id=2)
    cursor.execute("SELECT id_biblioteca FROM bibliotecas WHERE id_linguagem_id = 2")
    bibliotecas_python = cursor.fetchall()
    for biblioteca in bibliotecas_python:
        cursor.execute(f"INSERT INTO estudos (id_bibliotecas_id) VALUES ({biblioteca[0]})")
    conexao.commit()

if __name__ == "__main__":
    banco()