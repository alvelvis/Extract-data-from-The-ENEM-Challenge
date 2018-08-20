import html
import os

def list_dir():
    files_list = list()
    os.chdir('dataset')
    for item in os.listdir("."):
        if os.path.isfile(os.path.join(".", item)):
            if ".xml" in item:
                files_list.append(item)
                
    return files_list


def UnicoPortugues(folder):				
    files_list = sorted(list_dir())
    unico = ''
    for filename in files_list:
        if '-2' in filename:
            print(filename)
            unico = unico + '\n' + '#!' + filename + '\n'
            arq2 = open(folder + filename, 'r', encoding="utf-8")
            arq2 = arq2.read()
            arq2 = arq2.split('id="136"')[0]
            unico = unico + arq2 + '\n'

    os.chdir('../')
    arq = open(folder+'unico.txt', 'w', encoding="utf-8")
    arq.write(unico)
    arq.close()
    
    
def SalvaStatement(file):
    arquivo = open(file, 'r', encoding="utf-8")
    texto = arquivo.read()
    arquivo.close()

    sts = texto.split("<statement>")
    del sts[0]

    statements = ""
    for s in sts:
        statements += s.split("</statement>")[0] + "\n"
	
    statements = html.unescape(statements)
    statements = statements.strip()
    statements = statements.replace('  ',' ')
    statements = statements.replace(' \n','\n')
    statements = statements.replace('\n ','\n')
    arquivo2 = open('enunciados.txt', 'w', encoding="utf-8")
    arquivo2.write(statements)
    arquivo2.close()
    print(statements.count('\n'),'statements')
    

def SalvaCorretas(file):
    arquivo = open(file, 'r', encoding="utf-8")
    texto = arquivo.read()
    arquivo.close()

    cor = texto.split("<option")
    del cor[0]

    corretas = ""
    for s in cor:
        if '"Yes"' in s.split("</option>")[0]:
            corretas += s.split("</option>")[0].split(">")[1] + "\n"
	
    corretas = html.unescape(corretas)
    corretas = corretas.strip()
    corretas = corretas.replace('  ',' ')
    corretas = corretas.replace(' \n','\n')
    corretas = corretas.replace('\n ','\n')
    arquivo2 = open('corretas.txt', 'w', encoding="utf-8")
    arquivo2.write(corretas)
    arquivo2.close()
    print(corretas.count('\n'),'opções corretas')


def SalvaDistratores(file):
    arquivo = open(file, 'r', encoding="utf-8")
    texto = arquivo.read()
    arquivo.close()

    dis = texto.split("<option")
    del dis[0]

    distratores = ""
    for s in dis:
        if '"No"' in s.split("</option>")[0]:
            distratores += s.split("</option>")[0].split(">")[1] + "\n"
	
    distratores = html.unescape(distratores)
    distratores = distratores.strip()
    distratores = distratores.replace('  ',' ')
    distratores = distratores.replace(' \n','\n')
    distratores = distratores.replace('\n ','\n')
    arquivo2 = open('distratores.txt', 'w', encoding="utf-8")
    arquivo2.write(distratores)
    arquivo2.close()
    print(distratores.count('\n'),'distratores')


UnicoPortugues(r'')
SalvaStatement(r'unico.txt')
SalvaCorretas(r'unico.txt')
SalvaDistratores(r'unico.txt')