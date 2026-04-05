import sqlite3

conn = sqlite3.connect("final.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contagem_palavras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palavra TEXT,
    quantidade INTEGER
)''')

conn.commit()

# Verificar as tabelas criadas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Exibir as tabelas criadas
print("Tabelas no banco de dados:", tabelas)

conn.close()


print("Banco de dados criado com sucesso!")



