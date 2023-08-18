
import os
from merge_pdf import merge_pdf 

dest_dir = r'D:\pango\PDS_2022.2-SP3\doc'
output_pdf = r'D:\tmp_auto_clean\pangodoc.pdf'
lista = list()
for filename in os.listdir(dest_dir):
    # print(filename)
    lista.append(os.path.join(dest_dir, filename))
    
print(lista)

merge_pdf(lista, output_pdf)


