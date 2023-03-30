# Ejercicios propuestos módulos 5

## Funciones 

Transforme los ejercicios del módulo 3 en funciones.

Deberán tener una entrada de parametros/arguemntos y un retorno donde apliquen.

## Funciones Lambda

### Básicos:
1. Crea una función lambda que convierta una cadena en mayúsculas.
2. Crea una función lambda que calcule el área de un triángulo con base y altura dadas.
3. Crea una función lambda que elimine todos los elementos repetidos en una lista.

### Medios:
1. Crea una función lambda que calcule la media de un conjunto de números.
2. Crea una función lambda que encuentre la cadena más larga en una lista de cadenas.
3. Crea una función lambda que ordene una lista de diccionarios por el valor de una clave específica.

### Avanzados:
1. Crea una función lambda que devuelva una lista de los elementos que se repiten en dos listas.

2. Crea una función lambda que encuentre el número más común en una lista de números.
3. Crea una función lambda que tome una lista de diccionarios y devuelva una lista de valores únicos en una clave dada

### Funciones recursivas

Pase los algoritmos recursivos del curso de Fundamentos de programación a python.

### Asyncrónico

1. Crear un programa que use `asyncio` para hacer solicitudes a varios sitios web al mismo tiempo.

2. Escribir un programa que use `asyncio` para leer datos de un archivo grande de forma asíncrona y realizar algún tipo de procesamiento en los datos leídos.

3. Crear un programa que use `asyncio` para leer y escribir datos a una base de datos en segundo plano mientras se realiza algún otro procesamiento en el hilo principal del programa.

### Multihilo

1. **Suma de listas en paralelo**: Se pide que implementes una función que tome una lista de números y calcule la suma de los mismos utilizando múltiples hilos. 

   Cada hilo debe calcular la suma de una parte de la lista y luego los resultados deben ser combinados para obtener la suma total.

2. **Descarga de archivos en paralelo**: Se pide que implementes una función que tome una lista de URLs y descargue los archivos asociados a esas URLs utilizando múltiples hilos. Cada hilo debe descargar un archivo y guardar el resultado en un archivo local.

   Puede usar las siguientes url donde podrá descargar información:

   1. [https://www.gutenberg.org](https://www.gutenberg.org/ebooks/search/?query=adventure&submit_search=Go!): Este sitio web ofrece una gran cantidad de libros gratuitos en formato de texto plano que puedes descargar utilizando Python. Puedes utilizar múltiples hilos para descargar varios libros de forma simultánea.

3. **Monitoreo de directorios en paralelo**: Se pide que implementes una función que monitoree uno o varios directorios en el sistema de archivos y que notifique cuando se cree, modifique o borre un archivo en dichos directorios. 

   Para hacer esto de forma eficiente, se pueden utilizar múltiples hilos para monitorear diferentes directorios de forma paralela.

