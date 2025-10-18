import os
import logging
import sys


log_filename = 'ad_pref_suf_arqs.log'
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


def add_prefix_suffix(directory_path: str, prefix: str = '', suffix: str = '') -> None:
    '''
    Adiciona um prefixo e um sufixo aos nomes de todos os arquivos em um diretório.

    Parâmetros:
    -----------
        directory_path : str (padrão='')
            Caminho para o diretório que contém os arquivos a serem renomeados.
        prefix : Opcional[str]
            Cadeia de caracteres a ser adicionada no início de cada nome de arquivo.
        suffix : Opcional[str] (padrão='')
            Cadeia de caracteres a ser adicionada ao final de cada nome de arquivo 
            antes da extensão.
   
    Retorna:
    --------
        None    
    
    Exceções:
    ---------
        Exception
            Se ocorrer um erro ao renomear arquivos.
    '''
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):  
            
            file_name, file_extension = os.path.splitext(filename)
            
            new_filename = f'{prefix}{file_name}{suffix}{file_extension}'
            new_file_path = os.path.join(directory_path, new_filename)
            try:    
                os.rename(file_path, new_file_path)
                logger.info(f"Renomeado '{filename}' para '{new_filename}'")
            except Exception as e:
                logger.error(f"Erro ao renomear o arquivo '{filename}': {e}")
                print(f"Erro ao renomear o arquivo '{filename}': {e}")
        

if __name__ == '__main__':
    logger.info('Iniciando o script')
    
    diretorio = '/caminho/para/seus/arquivos' 
    prefixo = 'novo_prefixo_'
    sufixo = '_novo_sufixo'

    add_prefix_suffix(diretorio, prefixo, sufixo)

    logger.info('Finalizando o script')
    logging.shutdown()