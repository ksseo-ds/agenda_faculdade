#main.py

from classes_novas import *
import pandas as pd
import openpyxl
'''
caminho_agenda = 'Agenda_Ciencia de Dados_1s2024.xlsx'
df = pd.read_excel(caminho_agenda)
adf.columns
df


evento1 = Evento("Engenharia", "Cálculo", False, "Normal", "Av1", "2024-03-22")
evento2 = Evento("Engenharia", "Cálculo", False, "Normal", "Av2", "2024-03-24")
evento3 = Evento("Ciencia", "Banco de Dados", False, "Normal", "Av1", "2024-03-24")

'''


materia = Materia('Ciencia de Dados','calculo', False)
materia1 = Materia('Ciencia de Dados','teste', False)
materia2 = Materia('Ciencia de Dados','calculo', False)
materia3 = Materia('Engenharia', 'requisitos', True)

lista_materias = Materia.materias
lista_faculdades = Faculdade.cursos


for i in lista_materias:
    print(i)
print('--------------')
for i in lista_faculdades:
    print(i.faculdade, i.materia, i.dependencia)
print('--------------')
for i in lista_faculdades:
    print(str(i))
