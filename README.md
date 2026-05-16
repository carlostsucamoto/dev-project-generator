# Dev Project Generator 🎲

Gerador de ideias de projetos para desenvolvedores. Sorteia projetos e desafios com base em filtros de categoria e dificuldade, além de sugerir bibliotecas para estudo.

## 🚀 Funcionalidades

- Sortear ideias de projetos por categoria e dificuldade
- Sugestão de linguagem para cada projeto sorteado
- Dashboard com gráficos de distribuição por dificuldade e categoria
- Tabela com todas as ideias cadastradas
- Aba de estudos com bibliotecas para aprender
- Formulário para adicionar novas ideias

## 🛠️ Tecnologias

- Python
- SQLite3
- Dash
- Plotly

## 📁 Estrutura do projeto

dev-project-generator/
├── app.py          # configuração da conexão principal
├── database.py     # criação das tabelas
├── queries.py      # funções de consulta ao banco
├── seed.py         # população inicial do banco
├── ui.py           # interface visual (Dash)
└── README.md

## ⚙️ Como executar

1. Clone o repositório
git clone https://github.com/seu-usuario/dev-project-generator
cd dev-project-generator

2. Instale as dependências
pip install dash plotly

3. Popule o banco de dados
python seed.py

4. Inicie a aplicação
python ui.py

5. Acesse no navegador: http://localhost:8050

## 💡 Ideias futuras

- Checklist de projetos realizados
- Filtro de ideias por linguagem
- Integração da tabela ideias_linguagens