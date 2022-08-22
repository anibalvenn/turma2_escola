from typing import List
import Professora

class Turma():
    def __init__(self, idTurma, alunos:List, professora:Professora):
        self.idTurma = idTurma
        self.alunos = alunos
        self.professora = professora
    
    def showAllPeople(self):
        print('idTurma: ', self.idTurma)
        print('Professora: ', self.professora.nome)
        for i in self.alunos:
            print('Aluno: ', i.nomeAluno, 'Pai: ', i.nomePai, 'Mae: ', i.nomeMae)

    def buscarAlunoNaTurma(self, nome:str, turma):
       
            for i in turma.alunos:
                if i.nomeAluno == nome:
                    print('Aluno: ', i.nomeAluno, 'Turma:', turma.idTurma, 'Professora: ', turma.professora.nome, 'Pai: ', i.nomePai, 'Mae: ', i.nomeMae)
                    break
                else:
                    pass