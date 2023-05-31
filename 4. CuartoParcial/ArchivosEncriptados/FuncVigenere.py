# Funciones de la sesión anterior

def contraVigenere(clave,alfabeto):
    
    # Compruebo si la clave es válida (todas sus letras están en el alfabeto)
    if any([letra not in alfabeto for letra in clave]): 
        print('La clave y el alfabeto son incompatibles.')
        return None
    
    # Traduzco la clave a números
    clavenum=[alfabeto.index(letra) for letra in clave]
    
    return ''.join([alfabeto[-k] for k in clavenum]) # Construyo la contraclave y la devuelvo

def cifradoVigenere(texto,clave,alfabeto):
    
    # Compruebo si la clave es válida (todas sus letras están en el alfabeto)
    if any([letra not in alfabeto for letra in clave]): 
        print('La clave y el alfabeto son incompatibles.')
        return None

    L=len(alfabeto) # longitud alfabeto
    long=len(clave) # longitud clave
    clavenum=[alfabeto.index(letra) for letra in clave] # Obtengo la versión numérica de la clave
    
    # Paso al cifrado propiamente dicho
    textocif=''
    for k in xsrange(len(texto)):
        letra=texto[k]
        if letra in alfabeto:
            letra=alfabeto[(alfabeto.index(letra)+clavenum[k%long])%L]           
        textocif+=letra
    return textocif
    
def caracteres(texto):
    lista=list(set(texto)) # Usamos set para eliminar repeticiones
    lista.sort()           # Lista ordenada, de menor a mayor
    return ''.join(lista)

def masfrecuentes(long,texto,alfabeto):
    palabra=''
    for j in xsrange(long):
        letras=texto[j::long]                        # Lista de letras en posiciones congruentes con j módulo long
        letrasUA=set(letras).intersection(alfabeto)  # Estas son las letras que se han usado y que están en el alfabeto
        pares=[(letras.count(letra),letra) for letra in letrasUA] # Cuento cuántas veces aparece cada una de las letras usadas del alfabeto
        pares.sort(reverse=true)
        palabra+=pares[0][1]
    return palabra

def contraclave_Vigenere(texto,alfabeto,palabra):
    long=len(palabra) # longitud de la clave
    palabracodif=masfrecuentes(long,texto,alfabeto) # palabra formada por la letra más frecuente de cada bloque en el texto codificadoe
    contra=[]         # lista en la que almacenaremos las letras de la contraclave
    for j in xsrange(long):
        nuevaposicion_masfrec=alfabeto.index(palabracodif[j]) # índice de la letra más frecuente en el bloque j en el texto codificado
        posicion_masfrec=alfabeto.index(palabra[j])           # índice de la letra más frecuente en el bloque j en el texto original
        contra.append(alfabeto[(-nuevaposicion_masfrec+posicion_masfrec)]) # letra de la contraclave correspondiente a la posición j 
    return ''.join(contra) #la contraclave es la concatenación de las letras en contra