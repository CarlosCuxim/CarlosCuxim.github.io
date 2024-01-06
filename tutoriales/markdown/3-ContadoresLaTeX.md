# Los contadores de $\rm\LaTeX$


Uno de los aspectos más útiles de $\rm\LaTeX$ es que no solo es programa de composición de texto, sino que también es un lenguaje de programación en sí mismo. De este modo se pueden hacer operaciones aritméticas dentro del sistema y usarlos dentro del documentos.

  

Para esto $\rm\LaTeX$ cuenta con un tipo especial de variable, los *contadores*. Estos pueden ser considerados como variables de tipo entero. Estas variables son ampliamente usadas dentro del sistema, para la numeración de páginas, secciones, ecuaciones, teoremas, entre otros.

  

Para crear un nuevo contador basta con usar el comando
`\newcounter` en algún lugar
del documento (usualmente el preámbulo), este tiene la
siguiente estructura:

  
<qx-ds-code>
\newcounter{nombre del contador}[contador existente]
</qx-ds-code>


El funcionamiento es sencillo, `nombre del contador` indica el nombre con el cual vamos a identificar al contador. Ahora, el parámetro opcional `contador existente` sirve para subordinar el contador con uno ya existente, de modo que el nuevo contador se reinicie cuando el contador asociado se actualice. Además de crear el contador, el comando
`\newcounter` también nos crea un comando llamado `\thenombredelcontador` el cual nos permite usar el valor del contador en el documento.

  

Veamos un ejemplo. Supongamos que quiero crear un nuevo contador con el nombre `MiContador` tal que se reinicie cada vez que se cambie la sección, más adelante comentaré los nombres de los contadores más comunes, basta saber que el contador asociado con el nombre de la sección es `section`. De este modo el comando necesario sería:

  
<qx-ds-code>
\newcounter{MiContador}[section]
</qx-ds-code>
  

Esto nos crea el contador `MiContador` el cual se reinicia cada cambio de sección y el comando `\theMiContador` para poder usar el comando en el texto. Por default el valor de un nuevo contador es 0.


<qx-example-table>
Valor default de un contador: \theMiContador.
----------
Valor default de un contador: 0.
</qx-example-table>
  

Ahora, con el contador creado, existen varios comandos para
poder modificar su valor numérico. Los comandos más básicos
son:


<qx-list>
- `\setcounter{nombre del contador}{número entero}`

Este comando cambia el valor actual del contador `nombre del contador` y le asigna el valor `número entero`. Aunque `número entero` puede ser negativo, por limitaciones de los contadores el valor de `nombre del contador` no puede ser mayor a $2^{31}-1$ ni menor a $1-2^{31}$. Además, si un contador está subordinado por `nombre del contador` este comando no reiniciará el contador subordinado.


- `\addtocounter{nombre del contador}{número entero}`

Este comando permite sumar el valor `número entero` al valor actual del contador `nombre del contador`. De igual forma `número entero` puede ser negativo, pero la suma no puede ser mayor a $2^{31}-1$ o menor a $1 - 2^{31}$. Este comando tampoco reinicia los contadores subordinados.


- `\stepcounter{nombre del contador}`

    <p>
        Este comando incrementa en uno el valor del contador `nombre del contador`. Este comando si reinicia los contadores subordinados.
    </p>


- `\refstepcounter{nombre del contador}`

Este comando realiza exactamente lo mismo que el anterior. La única diferencia es permite guardar el valor de `nombre del contador` para que sea usado con `\label` y `\ref`.
</qx-list>

<qx-example-table>
\newcounter{A}
\newcounter{B}[A]
        
%&nbsp;B&nbsp;=&nbsp;8
\setcounter{B}{8}
Valor de A y B: (\theA, \theB).

%&nbsp;A&nbsp;=&nbsp;5
\setcounter{A}{5}
Valor de A y B: (\theA, \theB).

%&nbsp;A&nbsp;+=&nbsp;5
\addtocounter{A}{5}
Valor de A y B: (\theA, \theB).

%&nbsp;A&nbsp;+=&nbsp;1; B&nbsp;=&nbsp;0
\stepcounter{A}
Valor de A y B: (\theA, \theB).

%&nbsp;B&nbsp;=&nbsp;7
\setcounter{B}{7}
Valor de A y B: (\theA, \theB).

%&nbsp;A&nbsp;+=&nbsp;1; B&nbsp;=&nbsp;0
\refstepcounter{A}
Valor de A y B: (\theA, \theB).
----------
    Valor de A y B: (0,8).
    <br/>
    Valor de A y B: (5,8).
    <br/>
    Valor de A y B: (10,8).
    <br/>
    Valor de A y B: (11,0).
    <br/>
    Valor de A y B: (11,7).
    <br/>
    Valor de A y B: (12,0).
</qx-example-table>

<qx-example-table>
\newcounter{A}

\refstepcounter{A} %&nbsp;A&nbsp;=&nbsp;1
\label{A1}
Etiqueta actual: \ref{A1}.

\stepcounter{A} %&nbsp;A&nbsp;=&nbsp;2
\label{A2}
Etiqueta actual: \ref{A2}.

\refstepcounter{A} %&nbsp;A&nbsp;=&nbsp;3
\label{A3}
Etiqueta actual:{A3}.
----------
    Etiqueta actual: 1.
    <br/>
    Etiqueta actual: 1.
    <br/>
    Etiqueta actual: 3.
</qx-example-table>

<qx-example-table>
% 2^31&nbsp;-&nbsp;1 = 2147483647
\newcounter{A}

\setcounter{A}{2147483648}
\theA.

\setcounter{A}{-2147483648}
\theA.
----------
    2147483647.
    <br>
    -2147483647.
</qx-code-table>

  
Además de poder hacer operaciones con los contadores,
$\rm\LaTeX$ también permite modificar el formato en el que
son representados. De este modo es posible hacer que el
valor del contador se exprese en letras, números romanos o
símbolos. Esto es posible usando los siguientes comandos:

<qx-list>
- `\arabic{nombre del contador}`

Escribe el valor del contador `nombre del contador` con números arábigos, es decir: 1, 2, 3...


- `\value{nombre del contador}`

Escribe el valor del contador `nombre del contador` como valor entero. Sirve para comandos que requieran un número entero como entrada, como en `\addtocounter`.


- `\alph{nombre del contador}`

Escribe el valor del contador `nombre del contador` con letras minúsculas, es decir: a, b, c... El valor del contador debe estar entre 1 y 27.


- `\Alph{nombre del contador}`

Escribe el valor del contador `nombre del contador` con letras mayúsculas, es decir: A, B, C... El valor del contador debe estar entre 1 y 27.


- `\roman{nombre del contador}`

Escribe el valor del contador `nombre del contador` con números romanos en minúsculas, es decir: i, ii, iii... En el caso que el paquete `babel` sea cargado con la opción `spanish` entonces los números romanos estarán en versalitas, es decir: <span style="font-variant: small-caps;">i, ii, iii...</span>


- `\Roman{nombre del contador}`

Escribe el valor del contador `nombre del contador` con números romanos en mayúsculas, es decir: I, II, III...


- `\fnsymbol{nombre del contador}`

Escribe el valor del contador `nombre del contador` con símbolos, es decir: *, †, ‡... El valor deberá estar entre 1 y 9. En el caso que el paquete `babel` sea cargado con la opción `spanish` entonces los símbolos serán remplazados con asteriscos, es decir: *, **, ***... El valor deberá estar entre 1  y 6.
</qx-list>

<qx-example-table>
\newcounter{A}
\newcounter{B}

% A&nbsp;=&nbsp;1; B&nbsp;=&nbsp;2
\setcounter{A}{1}
\setcounter{B}{2}
% A&nbsp;+=&nbsp;B
\addtocounter{A}{\value{B}}

\arabic{A},
\alph{A},
\Alph{A},
\roman{A},
\Roman{A},
\fnsymbol{A}.
----------
    3, c, C, iii, III, ‡.
</qx-example-table>

  

Aunque los comandos mencionados anteriormente son útiles, en la práctica son poco usados. El uso real que se les da es para modificar el comando `\thenombredelcontador`. Para modificar este comando se puede usar  `\def` o `\renewcommand`, yo recomiendo este ultimo. De igual manera, usualmente no se aumenta el valor del contador a mano, sino que se crean comandos especiales que lo realicen automáticamente. Por ejemplo supongamos que queremos un comando que imprima la palabra problema y su número en formato de letra y además que se reinicie el contador cada sección, el codigo necesario sería:


<qx-example-table>
\newcounter{prb}[section]
\renewcommand{\theprb}{\alph{prb})}
\newcommand{\Problema}[1]{\refstepcounter{prb}\paragraph{Problema \theprb}}

\Problema $3x = 9$.

\Problema $2x = 10$.
----------
    <b>Problema a)</b> &nbsp;&nbsp;&nbsp; $3x = 9$. <br/><br/>
    <b>Problema b)</b> &nbsp;&nbsp;&nbsp; $2x = 10$.
</qx-example-table>

  

Una nota importante es que no solo los comandos creados por el usuario pueden ser modificados sino que también es posible modificar los contadores ya predefinidos por $\rm\LaTeX$, únicamente hay que saber cuales son sus nombres. En sí es relativamente simple saber cuales son, usualmente es el mismo nombre que el del comando. Por ejemplo el contador asociado con la sección es `section`, para la subsección `subsection`, para los capítulos es `chapter`. En el caso de entornos creados con `\newtheorem` es el mismo nombre del entorno, el numero de página está asociado con `page`. Un caso particular son de las listas enumeradas. Estas depende del nivel, es decir `enumi` para el primer nivel `enumii` para el segundo, `enumiii` para el tercero y  `enumiv` para el cuarto nivel. En el caso de ecuaciones el nombre del contador es `equation`. De esta forma si por ejemplo queremos cambiar como se expresan las secciones, basta con modificar el comando `\thesection`, y lo mismo para cualquier otro contador.



Para concluir, solo quiero mencionar que, aunque los contadores son una poderosa herramienta, no siempre es necesario definirlos. Usualmente los recomiendo si vas a necesitar enumerar una gran cantidad de cosas, o si se requiere un nuevo entorno que se deba numerar, en caso contrario, tal vez sería más sencillo simplemente enumerarlo a mano. A veces menos es mejor.