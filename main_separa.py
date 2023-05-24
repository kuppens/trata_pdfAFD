import os
import PyPDF2
import shutil
from remove_digit import delete_native,remove_digit
pasta = '15'


input = f'C:\\Users\\gab36\\OneDrive\\Documentos\\Development\\tratapdfAFD\\AFD_CGU_AUDITORIA_00{pasta}'
tratado = f'C:\\Users\\gab36\\OneDrive\\Documentos\\Development\\tratapdfAFD\\AFD_CGU_AUDITORIA_00{pasta}_TRATADO\\'
fa = 0

delete_native(input)
remove_digit(input)

def trata_arq(input):
    pdf_size = os.path.getsize(input)
    part_size = 120 * 1024 * 1024
    num_parts = pdf_size // part_size + (pdf_size % part_size != 0)
    basename, ext = os.path.split(input)

    if pdf_size > part_size:
        with open(input, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            for i in range(num_parts):
                # Determine the range of pages to include in this part
                start_page = i * len(pdf_reader.pages) // num_parts
                end_page = (i + 1) * len(pdf_reader.pages) // num_parts
                # Create a new PDF writer object for this part
                pdf_writer = PyPDF2.PdfWriter()
                # Add the pages to the new PDF writer
                for j in range(start_page, end_page):
                    pdf_writer.add_page(pdf_reader.pages[j])
                # Write the new PDF file
                separated_filename = f'{ext[:-4]}SEP{i + 1}.pdf'
                part_path = f'{tratado}{separated_filename}'
                with open(part_path, 'wb') as part_file:
                    pdf_writer.write(part_file)
            print(f'Arquivo {ext} separado em {num_parts} partes!')
    else:
        shutil.copy2(input, tratado)
        print(f'Arquivo {ext} < 120mb!')

def is_ocr_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        if '/Font' in reader.pages[0].keys():
            print(f'FALSO: {file_path}!!!!!')
            fa += 1

for a in os.listdir(input):
    is_ocr_pdf(input + f'\\{a}')
    trata_arq(input + f'\\{a}')

if fa > 0:
    print('ATENÇÃO! Há um ou mais arquivos sem OCR atribuído!')
else:
    print('SUCESSO! Todos os arquivos estão no devido formato OCR.')

print(f'FINALIZADO COM ÊXITO! Total de {len(os.listdir(input))} arquivos processados. Resultou em {len(os.listdir(tratado))} arquivos tratados!')

