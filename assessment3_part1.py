# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:14:44 2024

@author: rezaf
"""
from pypdf import PdfReader, PdfWriter


# Merge PDFs function
def pdfmerge(pdfs, output):
    pdfWriter = PdfWriter()
    for pdf in pdfs:
        pdfWriter.append(pdf)
    with open(output, 'wb') as f:
        pdfWriter.write(f)

# Rotate PDF function
def pdfrotate(origFileName, newFileName, rotation):
    reader = PdfReader(origFileName)
    writer = PdfWriter()
    for page in range(len(reader.pages)):
        pageObj = reader.pages[page]
        pageObj.rotate(rotation)
        writer.add_page(pageObj)
    with open(newFileName, 'wb') as newFile:
        writer.write(newFile)

# Encrypt PDF function
def pdfencrypt(inputFileName, outputFileName, password):
    reader = PdfReader(inputFileName)
    writer = PdfWriter()
    for page in range(len(reader.pages)):
        writer.add_page(reader.pages[page])
    writer.encrypt(password)
    with open(outputFileName, 'wb') as f:
        writer.write(f)

# Decrypt PDF function
def pdfdecrypt(inputFileName, outputFileName, password):
    reader = PdfReader(inputFileName)
    writer = PdfWriter()
    if reader.is_encrypted:
        reader.decrypt(password)
    for page in range(len(reader.pages)):
        writer.add_page(reader.pages[page])
    with open(outputFileName, 'wb') as f:
        writer.write(f)

def main():
    # File paths for operations
    pdfs = ['reza1.pdf', 'reza2.pdf']
    combined_output = input("Please enter a name for the merged file (you  must add .pdf at the end of the name):  ")
    rotated_output = input("Please enter a name for the rotated file (you  must add .pdf at the end of the name):  ")
    rotation = int(input("enter a number for rotating the pdf:  "))
    encrypted_output = input("Please enter a name for the encrypted file (you  must add .pdf at the end of the name):  ")
    decrypted_output = input("Please enter a name for the decrypted file (you  must add .pdf at the end of the name):  ")
    password = input("Please enter a password for your encrypted pdf file:  ")

    # Perform PDF merge
    pdfmerge(pdfs, combined_output)

    # Rotate a PDF
    pdfrotate(pdfs[0], rotated_output, rotation)

    # Encrypt a PDF
    pdfencrypt(pdfs[0], encrypted_output, password)

    # Decrypt the PDF
    pdfdecrypt(encrypted_output, decrypted_output, password)

if __name__ == "__main__":
    main()




  
