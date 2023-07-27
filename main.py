from contacto import Contacto

contacto = Contacto(
    "isai",
    "rivera",
    "55555",
    "r@gmail.com",
    "begonias",
    "140",
    "santa maria",
    "lazaro cardenas",
    "CDMX",
    "CDMX",
    "MX",
)


#GUARDAR UN CONTACTO (en un archivo .json)
contacto.save() 
#Consultar un contacto (por nombre y numero o solo nombre.)
contacto.consult('marce')
#Consultar el numero total de contactos
print(contacto.count_all())
#Eliminar un contacto (por nombre y numero o solo nombre)
contacto.delet('isai','55555')
#Consultar el numero total de contactos
print(contacto.get_all())
#BONUS Consultar un numero definido de contactos
contacto.get_contact_list_interval(1, 5)

