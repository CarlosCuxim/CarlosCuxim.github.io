let fileName = location.search.substring(1)

let Main = document.getElementById("MainContainer")

let fileDir = "./" + fileName + ".html"



// Esta función lee un archivo dada una dirección.
function readFile(fileDir, callback){
    // Crea un objeto para hacer la petición
    let req = new XMLHttpRequest()
    // Se realiza la petición
    req.open('GET', fileDir)
    req.send()

    req.onload = () => {
        callback(req.responseText)
    }

    //return req.responseText
}

function addToMain(text) {
    Main.innerHTML = text
    MathJax.typesetPromise()

    document.querySelectorAll('code').forEach(
        (el) => {
            hljs.highlightElement(el);
        }
    );
}

readFile(fileDir, addToMain)