# Fundamentos Filosóficos de la Inteligencia Artificial

En el capítulo 26 de AIMA, Russell y Norvig ponen en consideración el estado de la discusión acerca de qué es _pensar_ y si las máquinas pueden o no hacerlo.

Al respecto, se distinguen dos hipótesis fundamentales, denominadas __Inteligencia Artificial Débil__ e __Inteligencia Artificial Fuerte__,
cuya diferencia radica en que la primera sostiene que las máquinas pueden actuar _como_ si fueran inteligentes y la segunda sostiene que al actuar de ese modo, las máquinas
están de hecho pensando y no sólo simulando.

## Hipótesis de Inteligencia Artificial Débil

La Inteligencia Artificial como área de investigación fue fundada sobre la idea de que la __Inteligencia Artificial Débil__ es posible. No obstante, la pregunta que corresponde
desde un punto de vista filosófico es si _las máquinas pueden pensar_.

__Edsger Dijkstra__ sostiene al respecto que esa pregunta tiene más que ver con la definición que cada lenguaje pueda asignar al término _pensar_ que con el diseño o capacidades de las
máquinas que construyamos para cumplir esa tarea.

Para __Alan Turing__ la pregunta debería ser si las máquinas pueden pasar un test de comportamiento inteligente, logrando que su conducta no sea discernible de la de un humano.
Esto está basado fundamentalmente en la creencia de Turing sobre una serie de cosas que las máquinas no serían capaces de hacer a priori, tal como __juzgar lo correcto de lo incorrecto__
o __ser amable__.

Otro de los argumentos elaborados por Turing sostiene que la conducta humana es muy compleja para ser capturada por cualquier serie de reglas, y dado que las computadoras no pueden
sino seguir una serie de reglas no pueden generar comportamiento tan inteligente como el de los humanos. Esto se conoce como el __problema de calificación__ en IA.

La principal crítica a esta posición surge de __Hubert Dreyfus__ quien señala que la experticia humana incluye el conocimiento de ciertas reglas de forma holística, sin incurrir
en la pregunta de cómo estas reglas se establecen en la mente humana. Su crítica continúa proponiendo un proceso de cinco etapas para la adquisición de experticia, comenzando con
el procesamiento basado en reglas y finalizando con la capacidad de seleccionar respuestas correctas de forma instantánea. Estas mismas críticas más que impedir han contribuido al
desarrollo de la AI, particularmente en redes neuronales.

## Hipótesis de Inteligencia Artificial Fuerte

Suponiendo que una máquina logra pasar el Test de Turing, es decir de comportarse de forma suficientemente inteligente como para engañar a un humano, cabría preguntarse si está de
hecho pensando o sólo simulando pensar.

Asuntos como la consciencia, las emociones o la intencionalidad entran dentro de esta discusión. Turing sostiene que no podemos tener siquiera evidencia de los estados mentales internos
de otros seres humanos, por lo que sería colocar más alta la vara para máquinas que para personas.

Profundizando en este sentido, cabe preguntarse cómo se genera __la mente__ dentro del cuerpo físico de los humanos. El filósofo francés __René Descartes__ propuso la teoría dualista:
La actividad mental de Pensar (un proceso sin extensión espacial o propiedades materiales) y los procesos físicos de un cuerpo deben existir en reinos separados; llegando a especular
que la glándula pineal es el punto donde ambos reinos interactúan.

En contraposición, el __monismo__ o __fisicalismo__ sostiene que mente y cuerpo no son reinos separados y que los estados mentales son también estados físicos y viceversa. Esta 
teoría permite la posibilidad de AI Fuerte.

Si sus teorías son correctas entonces se podría deducir el estado mental de una persona por la correcta descripción del estado físico de su cerebro.  Como respuesta a esta premisa
se sostiene el ejercicio mental del _cerebro en una cubeta_.

El __funcionalismo__ por otro lado opina que un estado mental es cualquier condición causal intermedia entre un input y un output. En consecuencia, dos sistemas isomórficos tendrían
los mismos estados mentales suponiendo mismo input. Esto lleva a preguntarse si, de ser posible un completo reemplazo de neuronas en un ser humano por su equivalente electrónico, la 
consciencia del individuo se mantendría.

__John Searle__ sostiene el naturalismo biológico, según el cual los estados mentales son características emergentes causadas por los procesos físicos de bajo nivel en las neuronas.
Por lo tanto no cabría sólo reemplazar las neuronas por un mecanismo electrónico con equivalente comportamiento input-output sino que debería ser un programa que corra en una arquitectura
con el mismo poder causal de las neuronas. _La habitación china_ es su forma de demostrar su tesis. El punto conflictivo en este caso es si el entendimiento es una propiedad del sistema
en su conjunto o de alguna de sus partes. 

Norvig y Russell señalan como uno de los asuntos más complicados de debatir el que respecta a la __consciencia__. Introducen el término _Qualia_ para referirse a la naturaleza
intrínseca de las experiencias e indican el desafío que este concepto implica para el funcionalismo: diferentes qualias pueden estar involucradas en procesos causales isomórficos.
Aunque pudiésemos aislar el funcionamiento de determinadas neuronas, no existe razonamiento actualmente aceptado que permita derivar que la entidad dueña de esas neuronas esté teniendo
una determinada experiencia subjetiva.

Los autores coinciden con Turing que esta brecha explicativa no afecta el desarrollo de la IA: el interés es crear programas que se _comporten_ de forma inteligente, no hacerlos
conscientes.

## Eticidad y Riesgos del Desarrollo de Inteligencia Artificial

Respecto a la pregunta de si _debemos_ desarrollar Inteligencia Artificial, la respuesta es concisa: Si los riesgos o efectos colaterales de este desarrollo son negativos, entonces
los investigadores en este área deben redirigir sus esfuerzos. Señalan 6 puntos que ponen en consideración:

* Pérdida de puestos de trabajo por la automatización: frente al problema de que la expansión de la AI puede desplazar a miles de trabajadores, los autores señalan que hasta ahora
se han creado más puestos de trabajo más interesantes y mejor remunerados que los que se han destruido. Agregan que podríamos terminar en un futuro donde el desempleo es alto pero donde
incluso los desempleados sirven como capataces de cuadrillas de trabajadores robóticos.

* La gente puede tener mucho (o muy poco) tiempo de ocio: A pesar de que las predicciones apuntaban a que los avances tecnológicos llevarían a menos horas de trabajo, las industrias
de conocimiento intensivo, al estar operando 24 horas al día obliga a sus trabajadores a trabajar más horas para mantenerse al corriente. En la economía industrial clásica, donde las
recompensas son proporcionales al tiempo invertido, trabajar un 10% más puede significar un 10% más de ingresos. En cambio en las economías de la información se establece una suerte
de sociedad donde _"El ganador se lleva todo"_: trabajar un 10% de más puede significar un 100% más de ingresos. Esta presión hacia el individuo de trabajar más puede ser paliada por 
la incorporación de Inteligencia Artificial.

* La gente puede perder su sentido de ser únicos: Si bien la investigación en Inteligencia Artificial puede hacer posible la idea de que el ser humano es apenas un autómata, lo cierto
es que muchos cambios de paradigma han asestado golpes al sentido de unicidad del ser humano, como la revolución copernicana o la teoría de selección natural de Darwin.

* Los sistemas de Inteligencia Artificial pueden ser usados para fines indeseables: __G. H. Hardy__ señaló en 1940 que _la ciencia se dice útil cuando su desarrollo tiende a acentuar las
inequidades existentes en la distribución de la riqueza, o si más directamente promueve la destrucción de la vida humana._ Cierto es que los desarrollos en IA permiten esto, desde sistemas
militares autónomos hasta tecnología automática de vigilancia social. __David Brin__ sostiene que la pérdida de privacidad es inevitable, y que la forma de combatir la asimetría de
poder entre el Estado y el Individuo es hacer la vigilancia accesible a todos los ciudadanos.

* El uso de sistemas de IA puede resultar en una pérdida de responsabilidad: La pregunta es quién es responsable por las acciones o decisiones de una Inteligencia Artificial.
Puesto que por el momento ninguna IA ha adquirido personalidad jurídica y de que es improbable que ello suceda, es deseable que la ley se adapte a los nuevos desarrollos.

* El éxito de la IA puede significar el fin de la especie humana: Casi cualquier tecnología tiene el potencial para causar daño en las manos incorrectas, pero la IA introduce el problema
de que el mundo podría ser dominado por la tecnología misma. Es un tema recurrente en la Ciencia Ficción, y los autores abordan los principales tres riesgos que conlleva. Se
detienen en particular en lo que se ha denominado _la singularidad tecnológica_, donde de ser posible crear una inteligencia superhumana la era humana habría terminado.
De ser posible la inteligencia superhumana, debemos estar seguros de haber diseñado a sus predecesores en una forma donde no amenacen nuestra existencia. Las tres leyes de la robótica
de __Isaac Asimov__ son el primer ejemplo de ello. __Yudkowsky__ señala que el desafío de diseñar Inteligencias Artificiales Amistosas es definir un mecanismo para sistemas de IA
que evolucionen dentro de un sistema de controles y balances y de proveerles funciones de utilidad que permanezcan amistosas frente a los cambios. __Omohundro__ advierte que las
estructuras sociales que causan que los individuos compensen el costo de sus externalizaciones negativas deberá transitar un largo trecho antes de establecer un futuro estable y
positivo. 

#Opinión Personal

Desde mi punto de vista, el debate entre las dos hipótesis expresado reviste particular interés puesto que implica la búsqueda por la correcta definición de lo que
nos identifica como seres humanos, __la capacidad de pensar__, y los intentos por reproducir artificialmente esta habilidad.

En los primeros capítulos de AIMA, Russell y Norvig realizan un recorrido por los aportes de distintas ciencias respecto a qué es y cómo actúa el ser humano; y
por supuesto que es un debate aún vigente y, al mismo tiempo que este debate alimenta las investigaciones en IA, se pueden retroalimentar de ellas.

Los algoritmos de aprendizaje automático, por ejemplo, nos muestran una excelente abstracción de cómo el cerebro humano adquiere experiencia y establece una serie de reglas a
partir de una vasta serie de datos, que comenzamos a coleccionar desde que nacemos y que nos sirven para entender el mundo que nos rodea. Además, la necesidad de asegurar nuestra
supervivencia, y la de aquellos que nos rodean, nos lleva a desarrollar estrategias de adaptación al medio y comunicarlas a través del lenguaje. Este acto de comunicación es, al mismo
tiempo, datos que los demás coleccionarán y guardarán en su _dataset_ para fortalecer sus propios modelos de supervivencia.

Quizás nunca logremos develar cuál es el origen de la consciencia -  entendida como autopercepción, idea de la propia finitud, etcétera - pero sí podemos analizar funcionalmente
cuáles son las manifestaciones de esta conciencia e intentar reproducirla. Creo que en este ejercicio se podrán seguir esbozando nuevas ideas sobre cuál es la naturaleza del
individuo y las sociedades.

Respecto de la eticidad de desarrollar Inteligencia Artificial, y atento a la reflexión de Hardy que los autores citan en este capítulo, opino que el dilema no es si desarrollar AI
o no; sino para qué se hace y quiénes se benefician de este desarrollo. En los últimos quince años, las empresas que más han crecido en todo el mundo son aquellas que han sabido
minar grandes cantidades de datos y procesarlos mediante el uso de AI, para comprender mejor la conducta de los consumidores. Hay ejemplos también de la utilización de esta 
tecnología con fines de ingeniería social y sus resultados lejos están de ser socialmente aceptables.

Quizás no necesitemos programar las Leyes de Asimov en los algoritmos de AI que construyamos, sino en la consciencia de los desarrolladores para que la producción de su conocimiento
no sea una herramienta de control social ni causa de mayores inequidades.