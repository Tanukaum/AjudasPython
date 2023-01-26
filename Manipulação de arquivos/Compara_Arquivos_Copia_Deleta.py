from datetime import datetime
import os
import shutil
from filecmp import dircmp
import time

fonte = "caminho/da/pasta/fonte"

destino = "caminho/da/pasta/destino"

#   Cria Função de Log
def cria_log(texto_pro_log):
    #cria variável do tipo datetime, com a data hora atualizada
    now = datetime.now()
    #now.strftime formata a data
    now_format = now.strftime("%d-%m-%y %H:%M:%S")
    
    #abre um arquivo chamado Erro.txt, e escreve no final dele
    with open('Erro.txt', 'a+') as f:
        f.writelines(now_format + "  " + texto_pro_log + "\n")

def check_diff_files_copy(dcmp):
    try:
        ##dcmp.left_only são arquivos presentes APENAS no diretório fonte em forma de lista
        if dcmp.left_only:
            ##Para item na quantidade de itens presentes no diretório 
            for item in range(len(dcmp.left_only)):
                ##Cria o caminho do arquivo que deve ser copiado, junta o caminho do diretório fonte, com o arquivo presente apenas na fonte
                files = os.path.join(dcmp.left,dcmp.left_only[item])
                text_log = 'Arquivo copiado de:  ' + files 
                cria_log(text_log)
                ##Verifica se o arquivo existe e copia o arquivo da fonte para a pasta destino
                if os.path.exists(files):
                    shutil.copy2(files, dcmp.right)       
                else: 
                    pass
    except Exception as e:
        print("copy",e)
        cria_log(str(e))

def check_diff_files_delete(dcmp):
    try:
        ##dcmp.right_only são arquivos presentes APENAS no diretório destino em forma de lista
        if dcmp.right_only:
            ##Para item na quantidade de itens presentes no diretório 
            for item in range(len(dcmp.right_only)):
                ##Cria o caminho do arquivo que deve ser deletado, junta o caminho do diretório, com o arquivo presente apenas no destino
                files = os.path.join(dcmp.right,dcmp.right_only[item])
                text_log = 'Arquivo copiado de:  ' + files 
                cria_log(text_log)
                ##remove o arquivo do destino se o mesmo existir
                if os.path.exists(files):
                    os.remove(files)
                else: 
                    pass
    except Exception as e:
        print("delete",e)
        cria_log(str(e))
        

##Aqui para baixo chama as funções
#   dcmp um objeto da classe dircmp
# dircmp classe que administra a comparação de diretórios, compara arquivos e pastas da fonte com o destino
#  check_diff_files(dcmp), chama a função que compara os arquivos que estão nas pastas 

#Roda a cada 10segundos
while True:
    dcmp = dircmp(fonte, destino)

    check_diff_files_copy(dcmp)
    check_diff_files_delete(dcmp)
    time.sleep(10)