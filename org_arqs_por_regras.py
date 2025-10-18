import os
import shutil
import logging
import sys
from pathlib import Path


log_filename = 'org_arqs_por_regras.log'
log_directory = 'logs'

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_filepath = os.path.join(log_directory, log_filename)

logging.basicConfig(
    filename=log_filepath, 
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='w'
)

script_name = os.path.basename(sys.argv[0])

logger = logging.getLogger(script_name)


def select_directory(extension: str, rules: dict) -> str:
    '''
    Seleciona o diretório de destino para um arquivo com base em sua extensão.

    Parâmetros:
    -----------
        extension : str 
            A extensão do arquivo.
        rules : dict
            Um dicionário onde as chaves são os nomes dos diretórios de destino e 
            os valores são listas de extensões de arquivo associadas a cada diretório.

    Retorna:
    --------
        str 
            O nome do diretório de destino para o arquivo. Se a extensão não for 
            encontrada em nenhuma das regras, retorna 'Outros'.
    
    Exceções:
    ---------
        Nenhuma.
    '''

    for directory, extensions in rules.items():
        if extension in extensions:
            return directory
    return 'Outros' 


def organize_files_rules(source_directory: str, destination_directory: str, rules: dict) -> None:

    '''
    Organiza arquivos de um diretório de origem para um diretório de destino com 
    base em regras predefinidas. Todas as ações e possíveis erros são registrados 
    em um arquivo de log.

    Parâmetros:
    -----------
        source_directory : str
            Caminho do diretório de origem.
        destination_directory : str 
            Caminho do diretório de destino.
        rules : dict 
            Dicionário de regras, onde a chave é o nome da subpasta de destino e 
            o valor é uma lista de extensões de arquivo associadas a essa subpasta.
        
    Retorna:
    --------
        None    
    
    Exceções:
    ---------
        shutil.Error 
            Se ocorrer um erro durante movimentação de um arquivo usando o 
            módulo shutil.
    '''
    
    Path(destination_directory).mkdir(parents=True, exist_ok=True)

    for filename in os.listdir(source_directory):
        source_path = os. path.join(source_directory, filename)
        
        if os.path.isfile(source_path):

            file_extension = os.path.splitext(filename)[1].lower()
            directory = select_directory(file_extension, rules)
            destination_path = os.path.join(destination_directory, directory)
            Path(destination_path).mkdir(exist_ok=True) 
            
            try:    
                shutil.move(source_path, destination_path)
                logger.info(f"Movido '{filename}' para '{os.path.join(destination_path)}'")
            except shutil.Error as e:
                logger.error(f"Erro ao mover o arquivo '{filename}': {e}")
                print(f"Erro ao mover o arquivo '{filename}': {e}")
    

if __name__ == '__main__':
    logger.info('Iniciando o script')

    dir1 = 'Downloads'
    dir2 = '0__Inbox'
        
    diretorio_base = os.path.expanduser('~')
    diretorio_origem = os.path.join(diretorio_base, dir1)
    diretorio_destino =  os.path.join(diretorio_origem, dir2)

    regras = {
            'Documentos': ['.docx', '.xlsx', '.pptx', '.pdf', '.txt', '.csv', '.log'],
            'Audios': ['.mp3', '.wav'],
            'Videos': ['.mp4', '.avi', '.mkv'],
            'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico'],
            'Compactados': ['.zip', '.rar', '.7z'],
            'Programas': ['.exe', '.msi'],
            'Scripts': ['.ps1', '.py', '.bat', '.sh']
    }

    organize_files_rules(diretorio_origem, diretorio_destino, regras)

    logger.info('Finalizando o script')
    logging.shutdown()  