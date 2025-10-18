import os
import shutil
import logging
import sys


log_filename = 'org_arqs_por_tipo.log'
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


def organize_files_by_type() -> None:
    '''
    Organiza os arquivos no diretório de downloads por tipo, movendo-os para subpastas 
    com o nome de suas respectivas extensões.

    Parâmetros:
    -----------
        None
    
    Retorna:
    --------
        None    
    
    Exceções:
    ---------
        Nenhuma.
    '''
    
    base_path = os.path.expanduser('~')
    source_directory = os.path.join(base_path, 'Downloads')

    full_list = os.listdir(source_directory)
    filename_list = [filename for filename in full_list if os.path.isfile(os.path.join(source_directory, filename))]

    for filename in filename_list:
        file_extension = os.path.splitext(filename)[1][1:].lower()
        
        if file_extension:
            destination_directory = os.path.join(source_directory, file_extension)
            os.makedirs(destination_directory, exist_ok=True)
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            
            if os.path.exists(destination_path):
                logger.error(f"Erro: O arquivo '{filename}' já existe em '{destination_path}'.")
                print(f"Erro: O arquivo '{filename}' já existe em '{destination_path}'.")
            else:
                shutil.move(source_path, destination_path)
                logger.info(f"Movido '{filename}' para '{destination_path}'")
        
 
if __name__ == '__main__':
    logger.info('Iniciando o script')

    organize_files_by_type()
    
    logger.info('Finalizando o script')
    logging.shutdown()   
