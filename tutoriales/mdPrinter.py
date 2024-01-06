import re

def mdToHtml(mdText):

    htmlText = mdSplit(mdText)
    htmlText = addParTag(htmlText)
    

    return "\n\n\n".join(htmlText)


# Obtiene el siguiente párrafo y el resto del texto
def nextParagraph(mdText):
    Text = mdText.strip()

    if Text == "":
        return ["", ""]

    # Busca la primera etiqueta html
    search = re.search(r"<[^\/<>]+>", Text)
    # Index de la primera etiqueta html
    if search:
        a = search.span()[0]
        # Obtiene solo el tag
        tag = re.sub(r"[<>]", "", search.group()).split(" ")[0]
    else:
        a = len(Text)

    # Si empieza con un tag html, corta usando esta
    if a == 0:
        # Index final
        b = re.search(f"</{tag}>", Text)
        if b:
            b = b.span()[1]
        else:
            b = len(Text)

        ParList = [Text[a:b], Text[b:]]

    # En caso contrario, corta con doble salto de linea
    else:    
        ParList = re.split(r"\n[\n]+", Text, 1)
        # Si la lista de de un solo elemento, agrega un string simple
        if len(ParList) == 1:
            ParList.append("")

    return ParList

# Separa el texto en párrafos. Respeta las etiquetas html
def mdSplit(mdText):
    # Lista de párrafos
    ParList = []
    # Texto a separar
    text = mdText

    # Revisa si el texto a separar es vacío
    while text != "":
        # Obtiene el primer párrafo, lo guarda y lo elimina del texto
        Par, text = nextParagraph(text)
        # Se agrega el párrafo a la lista
        ParList.append(Par)
        

    return ParList


def addParTag(ParList):
    NewParList = ParList.copy()
    for i in range(len(ParList)):
        par = ParList[i]
        tag = re.search(r"<[^\/<>]+>", par)
        title = re.search(r"[#]+", par)

        if tag and tag.span()[0] == 0:
            continue
        elif title and title.span()[0] == 0:
            n = title.span()[1]-title.span()[0]
            par = re.split(r"[#]+", par)[1].strip()
            NewParList[i] = f"<h{n}>" + par + f"</h{n}>"
        else:
            NewParList[i] = "<p>" + par + "</p>"
    return NewParList