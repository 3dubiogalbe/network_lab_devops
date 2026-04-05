print("Projeto - Sistemas distribuidos / paralelos - MPI")


from mpi4py import MPI
from collections import Counter

# O código abaixo é um exemplo de como usar o MPI para contar a frequência de palavras em 
# um arquivo de texto.

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Processo 0 lê o arquivo e divide as palavras em partes iguais para os processos
if rank == 0:
    # Gerar o arquivo de texto com palavras aleatórias
    with open("texto.txt", "r") as arquivo:
        palavras = arquivo.read().split()

        # Divide as palavras em partes iguais para os processos
        partes = [palavras[i::size] for i in range(size)]
else:
    partes = None

# Distribui as partes para os processos
dados_locais = comm.scatter(partes, root=0)

# Cada processo conta as palavras em sua parte local
contador_local = Counter(dados_locais)  

# Envia os contadores locais para o processo 0'
contagens = comm.gather(contador_local, root=0)

# Processo 0 combina os contadores locais para obter a contagem total
if rank == 0:
    contador_total = Counter()
    for contagem in contagens:
        contador_total.update(contagem)
        
    # Imprime a contagem total de palavras
    print("Contagem total de palavras:")
    for palavra, contagem in contador_total.items():
        print(f"{palavra}, {contagem}")