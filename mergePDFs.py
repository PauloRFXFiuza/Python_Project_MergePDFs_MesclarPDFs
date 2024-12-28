'''
Merge PDFs Project- By Paulo Fiuza- 12/28/2024
'''
import PyPDF2 as PDF
import os

'''Create the merger'''
merger = PDF.PdfMerger()
print(f"Merger = {merger}")

'''Create the list of archives- project Folder '''
archivesList = os.listdir()
print(f"Archives List= {archivesList}")

'''Create the list of archives- Folder archives'''
archivesList = os.listdir("archives")
print(f"Archives List= {archivesList}")