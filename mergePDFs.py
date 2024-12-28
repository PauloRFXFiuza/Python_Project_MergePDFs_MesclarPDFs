'''
Merge PDFs Project- By Paulo Fiuza- 12/28/2024
Projeto Mesclador de PDFs
'''
import PyPDF2 as PDF
import os

'''Create the merger
Criar o mesclador'''
merger = PDF.PdfMerger()
print(f"Merger = {merger}")

'''Create the list of archives- project Folder 
Criar Lista de Arquivos- Pasta do projeto'''
archivesList = os.listdir()
print(f"Archives List= {archivesList}")

'''Create the list of archives- Folder archives 
Criar Lista de Arquivos- Pasta Archives'''
archivesList = os.listdir("archives")
print(f"Archives List= {archivesList}")

'''Sort the list of archives- Folder archives 
Ordenar Lista de Arquivos'''
archivesList = os.listdir("archives")
archivesList.sort()
print(f"Archives List post-sort= {archivesList}")

''''''