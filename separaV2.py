import os
import PyPDF2
import shutil

input = 'C:\\Users\\gab36\\OneDrive\\Documentos\\Development\\tratapdfAFD\\AFD_CGU_AUDITORIA_0015'
tratado = 'C:\\Users\\gab36\\OneDrive\\Documentos\\Development\\tratapdfAFD\\AFD_CGU_AUDITORIA_0015_TRATADO\\'

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
            print(f'Arquivo {ext} separado em {num_parts} partes! Movidos para a pasta de tratados.')
    else:
        shutil.copy2(input, tratado)
        print(f'Arquivo {ext} é menor que 120mb! Movido para a pasta de tratados.')


for a in os.listdir(input):
    trata_arq(input + f'\\{a}')