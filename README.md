# network_lab_devops
Esse é um projeto realizado pela universidade Anhembi Morumbi, que relaciona os conceitos de sistemas distribuídos e computação pararela, com um algoritimo desenvolvido em Python, para realizar o processamento, análise e contagem de dados.

 // Projeto acadêmico de computação paralela. //

Objetivo:
Implementar uma solução paralela para um projeto contendo uma grande quantidade de dados a serem analisados, e neste caso foram utilizadas palavras como os dados, e para o processamento / computação a ser realizado paralelamente, assim possibilitando melhorias de desempenho, foram utilizadas as técnologias abaixo:

Visual Studio Code (como plataforma de desenvolvimento)
Python (linguagem utilizada)
Multiprocessing / MPI (tecnologia para o procesamento paralelo)

// Sobre o MPI //

Microsoft MPI (MS-MPI) é a implementação da Microsoft do padrão Message Passing Interface, projetado para desenvolver e rodar aplicações paralelas em plataformas Windows. É amplamente utilizado em ambientes de Computação de Alto Desempenho (HPC), incluindo clusters e sistemas distribuidos.

// Execução do código //

Para realizar a execução do código _"main.py_", é necessário primeiramente executar o arquivo _gerador_dados.py_ para poder 
ter o documento contendo os dados a serem analisados.

Após isso, realize o comando: mpiexec -n 4 py main.py e os dados seram processados.

Obs:. Para gerar uma maior quantidade de processos, é apenas necessário alterar o número entre o -n "valor" py...



