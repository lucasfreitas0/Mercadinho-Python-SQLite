# 🛒 Mercadinho — Gerenciador de Produtos

Projeto desenvolvido em **Python e SQLite** com o objetivo de praticar programação, consultas SQL e manipulação de bancos de dados relacionais.

O sistema permite cadastrar produtos, verificar registros duplicados e consultar informações armazenadas no banco de dados.

## 🚀 Tecnologias utilizadas

- **Python** — lógica da aplicação.
- **SQLite** — armazenamento dos dados.
- **sqlite3** — biblioteca Python para conexão e operações com o banco de dados.
- **Git e GitHub** — controle de versão e publicação do projeto.

## 📋 Funcionalidades

- [x] Conexão com o banco de dados SQLite.
- [x] Cadastro de produtos.
- [x] Verificação de produtos duplicados pelo nome.
- [ ] Listagem de todos os produtos.
- [ ] Busca de produtos por nome ou categoria.
- [ ] Alteração de preços e categorias.
- [ ] Exclusão de produtos.
- [ ] Ordenação por preço.
- [ ] Relatórios de preços e categorias.

## 📁 Estrutura do projeto

```text
mercadinho/
├── main.py
├── banco.py
├── inserir.py
├── consultar.py
├── mercadinho.db
└── README.md
```

- `main.py`: menu principal e controle do programa.
- `banco.py`: gerenciamento da conexão com o banco de dados.
- `inserir.py`: cadastro e verificação de produtos duplicados.
- `consultar.py`: consultas e pesquisas de produtos.
- `mercadinho.db`: arquivo do banco de dados SQLite, criado ou utilizado pela aplicação.

## ⚙️ Como executar

### 1. Instale o Python

É necessário ter o Python 3 instalado. Você pode verificar a instalação executando:

```bash
python3 --version
```

### 2. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd mercadinho
```

### 3. Execute o programa

```bash
python3 main.py
```

**Observação:** o projeto utiliza `sqlite3`, que já faz parte da biblioteca padrão do Python na maioria das instalações, sem necessidade de instalar um pacote adicional.

## 🗄️ Banco de dados

O projeto utiliza SQLite para armazenar os produtos.

Cada produto possui os seguintes campos:

| Campo       | Descrição                      |
| ----------- | ------------------------------ |
| `id`        | Identificador único do produto |
| `nome`      | Nome do produto                |
| `categoria` | Categoria do produto           |
| `preco`     | Preço do produto               |

As operações de banco de dados utilizam comandos SQL como `INSERT`, `SELECT` e, futuramente, `UPDATE` e `DELETE`.

Os valores informados pelo usuário são enviados por parâmetros SQL, uma prática importante para reduzir o risco de SQL Injection.

## 🎯 Objetivos de aprendizagem

- Praticar funções e modularização em Python.
- Aprender a conectar uma aplicação a um banco de dados.
- Utilizar comandos SQL para manipular registros.
- Trabalhar com consultas parametrizadas.
- Organizar um projeto em múltiplos arquivos.
- Desenvolver boas práticas de programação.

## 🔮 Próximas melhorias

- Implementar um menu interativo com repetição até o usuário escolher sair.
- Adicionar validação de entradas e preços.
- Implementar as operações de consulta, atualização e exclusão.
- Criar relatórios com funções de agregação SQL, como `COUNT`, `AVG`, `MIN` e `MAX`.

## 📚 Status do projeto

🚧 Em desenvolvimento — projeto de estudo para praticar Python e SQL.

## 👨‍💻 Autor

Desenvolvido como projeto pessoal de aprendizagem em programação.
