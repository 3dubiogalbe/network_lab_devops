import sqlite3

conn = sqlite3.connect("final.db")
cursor = conn.cursor()

# dados para inserir
dados = [
    ("urso", 120),
    ("tigre", 98),
    ("gato", 75)
]

# inserindo os dados
cursor.executemany(
    "INSERT INTO contagem_palavras (palavra, quantidade) VALUES (?, ?)",
    dados
)

conn.commit()
conn.close()   

print("Dados inseridos com sucesso!")