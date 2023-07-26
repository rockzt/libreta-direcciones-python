from contacto import Contacto

contacto = Contacto("rodrigo", "zavala", "12456", "r@gmail.com", "begonias",
                    "140", "santa maria", "lazaro cardenas", "CDMX", "CDMX", "MX")
# contacto.save()

print(contacto.count_all())
contacto.get_contact_list_interval(1, 5)
