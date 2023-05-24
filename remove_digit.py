import os


folder_path = 'C:\\Users\\gab36\\OneDrive\\Documentos\\Development\\tratapdfAFD\\teste'


def remove_digit(caminho):
    files = os.listdir(caminho)

    for file_name in files:
        if file_name.lower().endswith('.pdf'):
            new_file_name = file_name[:-8] + '.pdf'
            
            original_file_path = os.path.join(caminho, file_name)
            new_file_path = os.path.join(caminho, new_file_name)

            os.rename(original_file_path, new_file_path)

            print(f"Renamed: {file_name} -> {new_file_name}")

def delete_native(pasta):
    c = 0
    for filename in os.listdir(pasta):
        if filename.lower().endswith('.pdf'):
            # Get the last 3 characters of the file name
            last_three_chars = filename[-7:-4]  # Excluding the '.pdf' extension
            if last_three_chars != '(1)':
                file_path = os.path.join(pasta, filename)
                
                os.remove(file_path)
                # print(f"Deleted file: {filename}")
                c += 1
    print(F'TOTAL DE {c} ARQUIVOS DELETADOS!')
