# Cálculo de Curp y Rfc en python.

#  CURP

La Clave Única de Registro de Población (CURP) es un código alfanumérico único de identidad de 18 caracteres, tanto para residentes como para ciudadanos mexicanos.

* Tu primer y segundo apellidos, así como tu nombre.
* Tu fecha de nacimiento.
* Genero.
* Entidad Federativa o lugar de nacimiento.


# RFC

El Registro Federal de Contribuyentes es una clave que se usa en México para distinguir a cada individuo o empresa obligado a pagar impuestos. A las personas u organizaciones que cuentan con su RFC se les llama contribuyentes.

1.- Para la Persona física: VECJ880326 XXX

* Las primeras dos letras (VE) son el apellido paterno más la primera vocal interna del apellido paterno.
* El tercer dígito (C) es la inicial del apellido materno. De no existir un apellido materno se utiliza una (X).
* El cuarto dígito (J) es la inicial del primer nombre.
* Los primeros dos dígitos son el año de nacimiento (88).
* Los segundos dígitos son el mes de nacimiento (03 o marzo).
* Los terceros dígitos son el día de nacimiento (26).
* Por lo tanto la persona nació el veintiséis de marzo de 1988.
* Los últimos dígitos (XXX) se le conoce como homoclave, esta la designa el SAT, dependiendo de algunos factores que realiza el SAT por medio de sistemas numéricos o alfanuméricos.

Esta homoclave la designará el SAT, revisando la petición a través de papel oficial ya designado.

# Ejemplo

from calcule import CalculeRFC, CalculeCURP

Solo cálcula RFC.
rfc = CalculeRFC(nombres='@param', paterno='@param', materno='@param', fecha='@param').data

Solo cálcula CURP.

curp = CalculeCURP(**datos).data




