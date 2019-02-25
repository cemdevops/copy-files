import shutil
import os
import os.path

def process(line, output_dir_path, duplicateFiles, lostFiles):
    """
    Function to copy a file to new location
    :param line:
    :return:
    """

    filename = line.split("/")[-1]

    if os.path.isfile(line):
        if os.path.isfile(os.path.join(output_dir_path, filename)):
            # duplicate files
            with open(duplicateFiles, 'a') as duplicates:
                duplicates.write(line+'\n')
        else:
            shutil.copy(line, output_dir_path)
    else:
        #files doesn't exist
        with open(lostFiles, 'a') as losts:
            losts.write(line+'\n')


#filesNamesList = "data/teste.txt"
#filesNamesList = "data/dados.txt"
#filesNamesList = "data/mapoteca.txt"
#filesNamesList = "data/artigos.txt"
#filesNamesList = "data/dissertacoes-teses-monografias.txt"
#filesNamesList = "data/livros.txt"
filesNamesList = "data/publicacoes.txt"
#filesNamesList = "data/mapoteca-eleitoral.txt"
output_dir_path = "/home/mariela/backups-site/publicacoes-tmp/"
# reports
duplicateFiles_path = "reports/duplicate-files.txt"
lostFiles_path = "reports/lost-files.txt"

# Read text file
with open(filesNamesList) as f:
    for line_temp in f:
        line = line_temp.replace('\n', '')
        process(line, output_dir_path, duplicateFiles_path, lostFiles_path)