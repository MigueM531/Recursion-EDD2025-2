# Recursion-EDD2025-2
Práctica I: Recursividad

Para esta práctica como colección de datos pueden utilizar lista simple

---
## RESTRICCIONES TECNICAS
- No se puede utilizar iteracciones for/while.
- Debe dar solución al menos 2 puntos utilizando tail recursión ó recursión de cola
- Todos los puntos se deben solucionar utilizando recursividad, sin funciones existentes que
realicen toda la operación.

---

Eres el desarrollador de un sistema para administrar una tienda de souvenirs turísticos. El
sistema debe almacenar y procesar la información de los productos y permitir consultas y
cálculos usando únicamente recursividad.


### Atributos del producto:

Cada producto tendrá:
- **Código:** Identificador único (texto).
- **Nombre:** Nombre del producto.
- **Categoría:** Ej. artesanías, ropa, accesorios, imanes.
- **Precio:** Precio en moneda local.
Los productos deberán estar precargados y organizados alfabéticamente por nombre para
facilitar la búsqueda recursiva.

---
### Operaciones a implementar
---
Todas las operaciones deben implementarse únicamente con recursión:
1. Búsqueda de un producto por nombre
- a. Usar búsqueda binaria recursiva (aprovechando el orden alfabético).
- b. Retornar todos los datos del producto si existe.
2. Cálculo del precio total de todos los productos
- a. Recorrer recursivamente y acumular el precio total.
3. Cálculo del precio promedio por categoría
- a. Recorrer recursivamente, contar productos por categoría y sumar precios
para luego calcular el promedio.
4. Ordenamiento recursivo por precio
- a. Implementar QuickSort o MergeSort recursivo.
- b. Poder ordenar de menor a mayor o viceversa.
5. Búsqueda de productos dentro de un rango de precios
- a. Retornar una nueva lista recursiva con los productos que cumplen el rango.
6. Generar recomendaciones de compra
- a. A partir de un producto, recomendar otros de la misma categoría
(recorriendo la lista recursivamente).

#
## Entrega y sustentación:

- La fecha de entrega y sustentación es el 21 de agosto durante clase (grupo martes y
jueves) ó 22 de agosto durante clase (grupo miércoles y viernes).

- TODOS SIN EXCEPCIÓN DEBEN ASISTIR ESTE DIA, SI NO LA NOTA DE LA
SUSTENTACIÓN PRACTICA SERÁ 0 (DE 2 PUNTOS POSIBLES)

- ADICIONAL SI EL ESTUDIANTE NO SE PRESENTA EN LA FECHA DE SUSTENTACIÓN
ORAL, LA NOTA SERA DE 0 (DE 2 PUNTOS POSIBLES)
- La práctica debe ser enviada a más tardar el 20/21 de agosto (dependiendo del
grupo).

- Se pueden hacer solos o en parejas, teniendo en cuenta La sustentación será
práctica y oral, y se hará de forma individual.
La implementación valdrá un 20%
La sustentación práctica un 40%. --> se realizará de 6:10 am a 6:40 am en la fecha de
entrega

- Los cambios de la sustentación solo se permiten en los equipos de cómputo del
salón.

- Los cambios de la sustentación practica únicamente se permiten sobre
visualstudio, es decir no se permite el uso de COLAB u otra herramienta en nube.

- De 6 am a 6:10 se tendrá tiempo para descargar la práctica y ejecutarla en el
equipo de la U.

La sustentación oral un 40%. --> de 6:40 am en adelante acorde a la programación.
Entregas y sustentación oral después de la fecha de entrega, la nota será sobre el 50%,
máximo 2.5