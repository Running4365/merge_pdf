# -*- coding:utf-8 -*-


from PyPDF2 import PdfWriter # PyPDF2 3.0.1

input_pdf_filelist = [ 
r'D:\personal\出差-发票-报销\230726-上午-高速费.pdf', 
r'D:\personal\出差-发票-报销\230726-晚上-高速费.pdf'
]
output_pdf_filename = r'D:\personal\出差-发票-报销\合并\230726-上午晚上-高速费.pdf'

def merge_pdf(input_pdf_filelist, output_pdf_filename):
    merger = PdfWriter()
    for pdf in input_pdf_filelist:
        merger.append(pdf)
    merger.write(output_pdf_filename)
    merger.close()



