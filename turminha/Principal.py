from Professora import Professora # tava dando um problema de importação bizarro aqui
from Aluno import Aluno
from Turma import Turma

# criando professoras
profa1 = Professora('profa1')
profa2 = Professora('profa2')

# criando alunos
alu1 = Aluno('alu1', 'pai1', 'mae1')
alu2 = Aluno('alu2', 'pai2', 'mae2')
alu3 = Aluno('alu3', 'pai3', 'mae3')
alu4 = Aluno('alu4', 'pai4', 'mae4')

# criando uma turma específica com uma professora:
turma1 = Turma(1, [alu1, alu2], profa1)
turma2 = Turma(2, [alu3, alu4], profa2)

#lista de Turmas
listTurmas = [turma1, turma2]

#cadastrar uma criança e inseri-la em uma turma:
alu5 = Aluno('alu5', 'pai5', 'mae5')
turma1.alunos.append(alu3)

#buscar uma turma e apresentar todas as pessoas que a compõem
listTurmas[0].showAllPeople()

#criação do método de buscar aluno na turma
def buscarAluno(nome:str, listTurmas):
    print('buscando alino de nome: ', nome)
    for turma in listTurmas:
        turma1.buscarAlunoNaTurma(nome, turma)
#buscar uma criança e apresentar suas informações de matrícula
#buscar informações de aluno de nome 'alu4'
buscarAluno('alu4', listTurmas)

