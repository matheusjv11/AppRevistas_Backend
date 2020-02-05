from Revistas.models import Autores, Artigos,Categoria,Edicoes,Revista,Palavras_chave, Usuario
import requests
import json
import xmltodict


from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

#------------- VARIAVEIS DE DADOS DO OAI-PMH --------------------

"""
titulo_artigo_br
titulo_artigo_en
autores
descricao_artigo_br
descricao_artigo_en
identifier_artigo
identifier_edicao
issn
data_lancamento
palavras_chaves
revista_br
revista_en
nome_revista 
sobre_edicao 
edicao 
nome_revista_en
sobre_edicao_en
edicao_en

"""

#----------------------------------------------------------------

#-------AVISOS-------"

"""
- Se reiniciar o banco de dados do zero, colocar uma tupla 'Not found' em : Revista e Categoria.
Todos os dados dessa tupla tem que ser 'Not found'. A função post() no final do código faz essa ação.
"""
#----------------------------------------------------------------

def salvar(titulo_artigo_br,titulo_artigo_en,autores,descricao_artigo_br,descricao_artigo_en
                    ,identifier_artigo,identifier_edicao,issn_revista,data_lancamento_edicao,palavras_chaves,revista_br
                    ,revista_en,nome_revista ,sobre_edicao ,edicao,nome_revista_en,sobre_edicao_en,edicao_en,link_pdf_artigo,
                    identifier_categoria, nome_da_categoria):

    #Essa função salva as variaveis de entrada no banco de dados
    
    

    tem_artigo = Artigos.objects.filter(identifier__startswith=identifier_artigo)
    #print(tem_artigo)

    if tem_artigo :
        return
    else:
        
        #Povoando tabela de revistas
        tem_revista = Revista.objects.filter(issn__startswith=issn_revista)

        if tem_revista:
            pass
        else:
            if type(issn_revista) is str:
                if len(issn_revista)<16:
                    nova_revista = Revista(issn=issn_revista, nome_revista_portugues=nome_revista, nome_revista_english=nome_revista_en)
                    nova_revista.save()
    
        
        
        #Povoando tabela de edição
        tem_edicao = Edicoes.objects.filter(identifier__startswith=identifier_edicao)
        

        if tem_edicao:
            pass
        else:


            
            #No caso de não conter o identifier da edição, vai verificar se existe outra edição com a mesma data de lançamento
            verificar_revista = Revista.objects.get(issn =issn_revista) 
            edicao_sem_identifier = Edicoes.objects.filter(edicao_portugues=edicao,revista=verificar_revista).first()
            
            

            if edicao_sem_identifier:
                     

                if edicao_sem_identifier.revista_id == verificar_revista.id :
                    
                    identifier_edicao = edicao_sem_identifier.identifier
                    
                else:
                    if len(identifier_edicao) < 5:
                        identifier_edicao = 'Not found'

                    revista_to_edicao =  Revista.objects.get(issn =issn_revista) 

                    nova_edicao = Edicoes(edicao_portugues=edicao, edicao_english=edicao_en,data_lancamento=data_lancamento_edicao,
                    revista = revista_to_edicao,identifier=identifier_edicao)
                    nova_edicao.save()

            else:  
                #Para colocar uma FK, é preciso pesquisa o seu id na tabela sql, a pesquisa pode ser feita
                #pesquisando por o nome de alguma coluna, e assim, puxa o id
                if len(identifier_edicao) < 5:
                    identifier_edicao = 'Not found'

                revista_to_edicao =  Revista.objects.get(issn =issn_revista) 

                nova_edicao = Edicoes(edicao_portugues=edicao, edicao_english=edicao_en,data_lancamento=data_lancamento_edicao,
                revista = revista_to_edicao,identifier=identifier_edicao)
                nova_edicao.save()

            #print(nova_edicao.revista.issn)
        
        #Povoando tabela de categoria
        tem_categoria = Categoria.objects.filter(identifier__startswith=identifier_categoria).first()

        if tem_categoria:
            pass
        else:
            revista_to_categoria =  Revista.objects.get(issn = issn_revista)
            nova_categoria = Categoria(nome_categoria=nome_da_categoria, revista = revista_to_categoria, identifier = identifier_categoria)
            
            nova_categoria.save()

        #Povoando a tabela de artigos

        try:
            edicao_to_artigo = Edicoes.objects.get(identifier=identifier_edicao)

            if identifier_edicao == 'Not found':
                revista_to_except = Revista.objects.get(issn = issn_revista)
                edicao_to_artigo = Edicoes.objects.get(edicao_portugues=edicao,revista=revista_to_except)

            
        except:
            #passar a data de lancamento e o id da revista
            revista_to_except = Revista.objects.get(issn = issn_revista)
            edicao_to_artigo = Edicoes.objects.filter(data_lancamento=data_lancamento_edicao,revista=revista_to_except).first()
        
        try:
            categoria_to_artigo = Categoria.objects.get(identifier=identifier_categoria)
        except:
            categoria_to_artigo = Categoria.objects.get(identifier='Not found')

        novo_artigo = Artigos(titulo_portugues=titulo_artigo_br, titulo_english= titulo_artigo_en,descricao_portugues=descricao_artigo_br,descricao_english= descricao_artigo_en,
                              identifier = identifier_artigo, link_pdf = link_pdf_artigo, edicao = edicao_to_artigo, categoria = categoria_to_artigo)
        novo_artigo.save()
        
        
        
        #Povoando tabela de autores
        for a in range(len(autores)):

            tem_autor = Autores.objects.filter(nome_autor=autores[a])
            
            if tem_autor:
                
                autor_to_artigo = Autores.objects.get(nome_autor=autores[a])
                
                novo_artigo.autores.add(autor_to_artigo)
                continue

            novo_autor = Autores(nome_autor=autores[a])
            novo_autor.save()
            novo_artigo.autores.add(novo_autor)

        #Povoando tabela de palavras-chave
        for s in range(len(palavras_chaves)):

            tem_palavra_chave = Palavras_chave.objects.filter(assunto=palavras_chaves[s])

            if tem_palavra_chave:

                palavra_chave_to_artigo = Palavras_chave.objects.get(assunto=palavras_chaves[s])
                novo_artigo.palavras_chave.add(palavra_chave_to_artigo)
                continue

            nova_palavra = Palavras_chave(assunto=palavras_chaves[s])
            nova_palavra.save()
            novo_artigo.palavras_chave.add(nova_palavra)



def revista_escolhida(id):
    #Essa função retorna as url's da Revista que terá seus dados recolhidos no OAI-PMH pela função 'run'

    site_inicial = ""
    proximo_site = ""
    site_categorias = ""

    if id == 1:
        #Revista Observatorio
        site_inicial = 'https://sistemas.uft.edu.br/periodicos/index.php/observatorio/oai?verb=ListRecords&metadataPrefix=oai_dc'
        proximo_site = 'https://sistemas.uft.edu.br/periodicos/index.php/observatorio/oai?verb=ListRecords&resumptionToken='
        site_categorias  = 'https://sistemas.uft.edu.br/periodicos/index.php/observatorio/oai?verb=ListSets'
    
    elif id == 2:
        
        #Revista Desafios
        site_inicial = 'https://sistemas.uft.edu.br/periodicos/index.php/desafios/oai?verb=ListRecords&metadataPrefix=oai_dc'
        proximo_site = 'https://sistemas.uft.edu.br/periodicos/index.php/desafios/oai?verb=ListRecords&resumptionToken='
        site_categorias  = 'https://sistemas.uft.edu.br/periodicos/index.php/desafios/oai?verb=ListSets'
 
    
    elif id == 3:

        #Revista Campo
        site_inicial = 'https://sistemas.uft.edu.br/periodicos/index.php/campo/oai?verb=ListRecords&metadataPrefix=oai_dc'
        proximo_site = 'https://sistemas.uft.edu.br/periodicos/index.php/campo/oai?verb=ListRecords&resumptionToken='
        site_categorias  = 'https://sistemas.uft.edu.br/periodicos/index.php/campo/oai?verb=ListSets'
 
    
    elif id < 1 or id > 3:
        
        print("Id de revista invalido")
        quit()




    return site_inicial,proximo_site,site_categorias     

def run(revista_OAI):

    
    site_inicial, proximo_site, site_categorias = revista_escolhida(revista_OAI)
    site = site_inicial
    req_categorias = requests.get(site_categorias)
    xml_categorias = xmltodict.parse(req_categorias.text)
    string_categorias = json.dumps(xml_categorias)
    json_categorias = json.loads(string_categorias)
    
    
#--------Recolhimento das informações das categorias--------#
    dicionario_categorias  = json_categorias['OAI-PMH']['ListSets']['set']
    categorias = {}

    for b in range(len(dicionario_categorias)):

            setName = dicionario_categorias[b]['setName']
            nome_categoria = setName.split('/')[0]
            identifier_categoria = dicionario_categorias[b]['setSpec']

            categorias[identifier_categoria] = nome_categoria
#--------Fim Recolhimento das informações das categorias--------#

#--------Recolhimento das informações dos artigos-------#   
    while True:

        req = requests.get(site)
        #req = requests.get('https://sistemas.uft.edu.br/periodicos/index.php/observatorio/oai?verb=ListRecords&resumptionToken=b319b5d558d22f3973f967052f0ffbf1')
        # O xml é na verdade uma dicionario ordenado
        xml = xmltodict.parse(req.text)
        # O dicionario é na verdade uma string
        dicionario = json.dumps(xml)
        dicionario2 = json.loads(dicionario)

        lista = dicionario2['OAI-PMH']['ListRecords']['record']
        #print(lista)

        
        for x in range(len(lista)): 

            print(lista[x]['header']['identifier'])

            if '@status' in lista[x]['header']:
                print(lista[x])
                if lista[x]['header']['@status'] == 'deleted':
                    print("Deletado")
                    continue
                else:
                    print(lista[x])
                    print(lista[x]['header']['@status'])

            titulo_artigo = lista[x]['metadata']['oai_dc:dc']['dc:title']

            if type(titulo_artigo) is list:

                for s in range(len(titulo_artigo)):
                        
                        if titulo_artigo[s]['@xml:lang'] == 'pt-BR':

                            titulo_artigo_br = titulo_artigo[s]['#text']

                        if titulo_artigo[s]['@xml:lang'] == 'en-US':

                            titulo_artigo_en = titulo_artigo[s]['#text']
            else:
        
                    titulo_artigo_br = titulo_artigo['#text']
                    titulo_artigo_en = 'Not found'
            
            if 'dc:creator' in lista[x]['metadata']['oai_dc:dc'].keys():
                autores = lista[x]['metadata']['oai_dc:dc']['dc:creator']
            else:
                autores = "Not found"
                
            if 'dc:description' in lista[x]['metadata']['oai_dc:dc']:
                descricao_artigo = lista[x]['metadata']['oai_dc:dc']['dc:description']
            else:
                descricao_artigo = "Not found"
            

            if type(descricao_artigo) is list:
                for z in range(len(descricao_artigo)):
                    
                    if descricao_artigo[z]['@xml:lang'] == 'pt-BR':

                        descricao_artigo_br = descricao_artigo[z]['#text']

                    if descricao_artigo[z]['@xml:lang'] == 'en-US':

                        descricao_artigo_en = descricao_artigo[z]['#text']
                    
            else:
                try:
                    descricao_artigo_br = descricao_artigo['#text']
                except:
                     descricao_artigo_br = 'Not found'

                descricao_artigo_en = 'Not found'

            revista = lista[x]['metadata']['oai_dc:dc']['dc:source']
            identifier_artigo = lista[x]['header']['identifier']
            identifier_edicao = lista[x]['metadata']['oai_dc:dc']['dc:source'][len(lista[x]['metadata']['oai_dc:dc']['dc:source'])-1]
            issn = lista[x]['metadata']['oai_dc:dc']['dc:source'][len(lista[x]['metadata']['oai_dc:dc']['dc:source'])-2]
            
            if len(identifier_edicao) < 14:
                issn = identifier_edicao
                identifier_edicao_IfErro = lista[x]['metadata']['oai_dc:dc']['dc:identifier'][len(lista[x]['metadata']['oai_dc:dc']['dc:identifier'])-1]
                identifier_edicao_IfErro = identifier_edicao_IfErro.split('p')[0]
                identifier_edicao = identifier_edicao_IfErro

            data_lancamento = lista[x]['metadata']['oai_dc:dc']['dc:date']
            
            palavras_chaves = ""

            if 'dc:subject' in lista[x]['metadata']['oai_dc:dc']:
                
                palavras = lista[x]['metadata']['oai_dc:dc']['dc:subject']

                if type(palavras) is list:
                        
                    for c in range(len(palavras)):

                        if palavras[c]['@xml:lang'] == 'pt-BR' or palavras[c]['@xml:lang'] == 'en-US' :
                            palavras_chaves += palavras[c]['#text']
                            palavras_chaves +=';'

                  
                else:
                   pass

                    
            
            if type(revista) is list:
                z=0
                for v in range(len(revista)):
                    try:
                        language = revista[v]['@xml:lang']
                        
                        if language == 'pt-BR':
                                revista_br = revista[v]['#text']
                                z+=1
                        if language == 'en-US':
                                revista_en = revista[v]['#text']
                                z+=1
                        if z == 2:
                            break
                    except:                        
                        revista_br = revista[0]['#text']
                        revista_en = 'Not found'
                            
            else:
                revista_br = revista['#text']
                revista_en = 'Not found'

            

            nome_revista = revista_br.split(';')[0]
            sobre_edicao = revista_br.split(';')[1]
            edicao = sobre_edicao.split(':')[0]

            if revista_en == 'Not found':
                nome_revista_en = 'Not found'
                sobre_edicao_en = 'Not found'
            else:
                nome_revista_en = revista_en.split(';')[0]
                sobre_edicao_en = revista_en.split(';')[1]

            edicao_en = sobre_edicao_en.split(':')[0]

            if 'dc:relation' in lista[x]['metadata']['oai_dc:dc']:

                is_string = lista[x]['metadata']['oai_dc:dc']['dc:relation']

                if type(is_string) is str:
                    link_pdf = is_string.split(';')[0]
                else:

                    link_pdf = lista[x]['metadata']['oai_dc:dc']['dc:relation'][0]

                    if 'sistemas' in link_pdf: 
                        pass
                    else:
                        link_pdf = lista[x]['metadata']['oai_dc:dc']['dc:relation'][1]
            else:
                link_pdf = 'Not found'

            identifier_categoria = lista[x]['header']['setSpec'][0]

            if identifier_categoria in categorias:
                categoria_artigo = categorias[identifier_categoria]
            else:
                categoria_artigo = 'Not found'
            
            
            if type(autores) is str:
                autores = autores.split(';')

            if type(palavras_chaves) is str:   
                palavras_chaves = palavras_chaves.split(';')
            
            
            
            
            salvar(titulo_artigo_br,titulo_artigo_en,autores,descricao_artigo_br,descricao_artigo_en
                    ,identifier_artigo,identifier_edicao,issn,data_lancamento,palavras_chaves,revista_br
                    ,revista_en,nome_revista ,sobre_edicao ,edicao,nome_revista_en,sobre_edicao_en,edicao_en,link_pdf,
                    identifier_categoria,categoria_artigo)

            

       
       #Parte do código que chama a proxima pagina de artigos

        if '#text' in dicionario2['OAI-PMH']['ListRecords']['resumptionToken']:
            resumption_token = dicionario2['OAI-PMH']['ListRecords']['resumptionToken']['#text']
            site = proximo_site+resumption_token    
        else:
            resumption_token = 'Final'
            
            break                                                                         

#--------Fim Recolhimento das informações dos artigos-------#
def post():

   revista_to_categoria =  Revista(issn=0, nome_revista_portugues='Not found', nome_revista_english='Not found')
   revista_to_categoria.save()
   nova_categoria = Categoria(nome_categoria='Not found', revista = revista_to_categoria, identifier = 'Not found')
   nova_categoria.save()
