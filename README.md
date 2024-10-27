# PROYECTO DESVIACION ESTANDAR
## DESCRIPCION
Desarrolla una herramienta para que los usuarios puedan calcular la media y la desviación estándar de una lista de valores numéricos.Pensada para manejar tanto conjuntos de datos simples como más complejos, 
esta aplicación ofrece un análisis rápido y preciso mediante clases especializadas que gestionan distintos casos.

La aplicación está diseñada con robustez, incorporando manejo de excepciones para situaciones como:

-Listas vacías, que devuelven un valor None en lugar de un error.
-Entradas con elementos no numéricos, que generan un mensaje de error específico.
-Conjuntos de elementos de valor cero, para los cuales se muestra un mensaje especial ("Cero").
## INTEGRANTES
| Apellidos y nombres| ROL |
|--------------------|-----|
|Espinoza Zarate Juan Carlos| Desarrollador |
|Vega Carhuallanqui Tatiana| Desarrollador |
## Como ejecutar el codigo 
### Ejecutar las pruebas unitarias:
Las pruebas se encuentran en tests/PruebaOperaciones.py.
Para ejecutarlas, abre una terminal en la raíz del proyecto y usa el siguiente comando:python -m unittest tests/PruebaOperaciones.py o sino puedes poner click derecho donde esta/PruebaOperaciones.py y escoges la opcion "Run"
Esto correrá todas las pruebas definidas, incluyendo casos para listas vacías, listas de un solo elemento, listas con elementos no numéricos y listas con valores positivos y negativos.
### Descripción de los Resultados Esperados:
La media y la desviación estándar se calculan considerando:
-Si la lista está vacía, devuelve None.
-Si contiene solo ceros, devuelve "Cero".
-Si tiene un solo elemento, la desviación estándar es 0.
-Para listas con elementos positivos y negativos, se calcula la media y luego la desviación estándar en función de los valores absolutos.
