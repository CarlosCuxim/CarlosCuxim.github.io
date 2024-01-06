from glob import glob
from pathlib import Path
from mdPrinter import mdToHtml


# Abre el archivo template.html y lo guarda
with open("template.html", "r") as templateFile:
    template = templateFile.read()

# Lista de los archivos a crear
pathList = glob("./markdown/*.md")

# Crea un html por cada archivo md
for path in pathList:
    # Solo el nombre del archivo
    fileName = Path(path).stem

    # Abre el contenido
    with open(path, "r") as contentFile:
        content = contentFile.read()

    # Cambia el formato md a html
    bodyContent = mdToHtml(content)

    # Usa la plantilla para hacer el contenido del html
    bodyContent = template.replace("<!--Qx@Content-->", bodyContent)

    # Crea y guarda el archivo html
    with open(f"./{fileName}.html", "w") as newFile:
        newFile.write(bodyContent)