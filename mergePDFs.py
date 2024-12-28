'''
Merge PDFs 
'''
import PyPDF2 as PDF
import os

merger = PDF.PdfMerger()
print(f"Merger = {merger}")

archivesList = os.listdir()
print(f"Archives List= {archivesList}")

archivesList = os.listdir("archives")
print(f"Archives List= {archivesList}") 