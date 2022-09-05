from datetime import datetime
import os
import shutil
from filecmp import dircmp

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


###Função que compara pastas recursivamente
def check_diff_dirs(dcmp):
    #Tenta realizar os passos dentro do try quando algo da errado chama o except
    try:
        ##Para item na quantidade de itens presentes no diretórios comuns
        for itens in range(len(dcmp.common_dirs)):
            fonte = os.path.join(dcmp.left , dcmp.common_dirs[itens])
            destino = os.path.join(dcmp.right , dcmp.common_dirs[itens])
            dcmp_interno = dircmp(fonte, destino)
            check_diff_dirs(dcmp_interno) #chama Recursivo
    except Exception as e:
        cria_log(str(e))        