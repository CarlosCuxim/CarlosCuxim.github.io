# Creación de nuevos comandos en $\rm\LaTeX$


En algunas ocasiones se requiere reutilizar una misma pieza de código en un documento y aunque en $\rm\LaTeX$ es relativamente fácil conservar el formato original solo copiando y pegando el código a mano, esto puede inducir muchas equivocaciones.

Por ejemplo, supongamos que en nuestro documento necesitamos utilizar bastantes veces una matriz simétrica de $2 \times 2$, aunque el código es relativamente corto, si se necesita muchas veces lo mejor es crear un comando tal que cree automáticamente el código deseado.

En $\rm\LaTeX$ hay diversas formas de crear comandos, aquí mencionaré únicamente el más básico: `\newcommand`. Este comando tiene la siguiente estructura:


<qx-ds-code>
\newcommand{nombre}[núm. de entradas][valor default]{expansión}
</qx-ds-code>

Para entender su funcionamiento consideremos el siguiente ejemplo. Supongamos que debemos crear un comando que genere un conjunto de $n$ vectores de la forma $\{\mathbf{x}_1, \ldots, \mathbf{x}_n \}$. Para esto podemos crear un comando llamado `\vectores` que cree automáticamente la ecuación, para ello debemos escribir en algún lugar del documento (usualmente en el preámbulo) el siguiente comando:

<qx-ds-code>
\newcommand{\vectores}{\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}}
</qx-ds-code>

El funcionamiento del comando es simple, este le dice a $\rm\LaTeX$ que cuando se use el comando `\vectores` este se sustituirá exactamente como `\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}`.

<qx-example-table>
    Sea $\vectores$ un conjunto de vectores de $\mathbb{R}^n$.
----------
    Sea $\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$ un conjunto de vectores de $\mathbb{R}^n$.
</qx-example-table>

Ahora, supongamos que deseamos modificar la variable de los vectores, es decir que en vez de $\mathbf{x}$ sea $\mathbf{y}$ o $\mathbf{z}$, no necesitamos crear un comando para cada uno, sino que podemos hacer que nuestro comando tome una entrada. Para esto hay que colocar un número del 1 al 9 en `núm. de entradas`, cada una de las entradas será accesible mediante el `#`, por ejemplo, si necesitamos la información en la entrada 1 usamos `#1`, `#2` para la entrada 2 y así consecutivamente. En nuestro caso el código necesario sería:

<qx-ds-code>
\newcommand{\vectores}[1]{\{\mathbf{#1}_1, \ldots, \mathbf{#1}_n\}}
</qx-ds-code>

De esta forma si usamos
`\vectores{x}`
este se expandirá en $\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$
pero con
`\vectores{y}`
este se expandirá en $\{\mathbf{y}_1, \ldots, \mathbf{y}_n\}$.

<qx-example-table>
    Con x: $\vectores{x}$.
    Con y: $\vectores{y}$.
----------
    Con x: $\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$.
    Con y: $\{\mathbf{y}_1, \ldots, \mathbf{y}_n\}$.
</qx-example-table>

Ahora, supongamos que el tamaño del conjunto no siempre es del mismo tamaño, sino que a veces necesitamos de 10 vectores o 15, pero en raras ocasiones. Es posible también especificar un parámetro por defecto, es decir, un valor que siempre se use a menos que se especifique lo contrario, para ello en `valor default`
hay que colocar que valor será usado a menos que se especifique lo contrario. Al momento de escribir el comando el parámetro opcional siempre será el primero, y se colocará entre corchetes. Por ejemplo, consideremos el siguiente código:

<qx-ds-code>
\newcommand{\vectores}[2][n]{\{\mathbf{#2}_{#1}, \ldots, \mathbf{#2}_{#1}\}}
</qx-ds-code>

Para poder usar el comando podemos usar `\vectores{x}` y se usará como primer parámetro `n`, pero con `\vectores[5]{z}` se usará como primer parámetro el número `5`.

<qx-example-table>
    Con x y el valor default: $\vectores{x}$.
    Con z y el primer parámetro 5: $\vectores[5]{z}$.
----------
    Con x y el valor default:
    $\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$.
    Con z y el primer parámetro 5:
    $\{\mathbf{z}_1, \ldots, \mathbf{z}_5\}$.
</qx-example-table>


Para concluir solo quiero mencionar que los comandos de $\rm\LaTeX$ son bastante útiles si se saben usar correctamente, un ejemplo de su uso es para definir formas más cortas de comandos largos como `\R` para `\mathbb{R}` o `\diff` para `\frac{d}{dx}`, lo cual permite que el código sea más legible y sencillo.