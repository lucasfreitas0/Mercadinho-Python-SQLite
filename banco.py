# ARQUIVO IMPORTANTE PARA A CONEXÃO DE TODOS OS ARQUIVOS COM O BANCO DE DADOS

import sqlite3

def conectar(): # CRIA UMA FUNÇÃO PARA QUE OS OUTROS ARQUIVOS POSSAM IMPORTAR 

    conexao = sqlite3.connect("mercadinho.db")
    
    cursor = conexao.cursor()

    # CRIA A TABELA mercadinho SE NÃO EXISTIR, JÁ ADICIONANDO OS PARÂMETROS INICIAIS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mercadinho(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL)
    """)
    cursor.close() 
    
    return conexao
