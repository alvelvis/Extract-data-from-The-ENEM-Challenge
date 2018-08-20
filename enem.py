def list_dir():
    files_list = list()
    import os
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
	
    import html
    statements = html.unescape(statements)
    
    print(statements)
    arquivo2 = open('statements.txt', 'w', encoding="utf-8")
    arquivo2.write(statements)
    arquivo2.close()
    print(statements.count('\n'),'statements')
    

UnicoPortugues(r'')
SalvaStatement(r'unico.txt')
