import os

import files_management

current_path = os.path.dirname(__file__)
ARTICLE_FILE_NAME = "contactos.json"
ARTICLE_FILE_PATH = current_path + f"/{ARTICLE_FILE_NAME}"


class Contacto:

    def __init__(
        self,
        nombre,
        apellido,
        telefono,
        email,
        calle,
        exterior,
        colonia,
        municipio,
        ciudad,
        estado,
        pais,
        interior="",
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.calle = calle
        self.exterior = exterior
        self.interior = interior
        self.colonia = colonia
        self.municipio = municipio
        self.ciudad = ciudad
        self.estado = estado
        self.pais = pais

    def as_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "email": self.email,
            "calle": self.calle,
            "exterior": self.exterior,
            "interior": self.interior,
            "colonia": self.colonia,
            "municipio": self.municipio,
            "ciudad": self.ciudad,
            "estado": self.estado,
            "pais": self.pais,
        }

    def get_all(self):
        return files_management.read(ARTICLE_FILE_PATH)

    def count_all(self):
        contacts = files_management.read(ARTICLE_FILE_PATH)
        iterations = 0
        for contact in contacts:
            iterations += 1
        return iterations

    def save(self):
        dict_contacto = self.as_dict()
        try:
            files_management.update(ARTICLE_FILE_PATH, dict_contacto)
        except FileNotFoundError:
            files_management.create(ARTICLE_FILE_PATH, dict_contacto)

    def get_contact_list_interval(self, *args):
        start = args[0]
        end = args[1]
        contacts = files_management.read(ARTICLE_FILE_PATH)
        contact_list = []
        for contact in contacts[start - 1:end]:
            contact_list.append(contact)
        print(contact_list)

    def consultar(self, name):
        contacts = files_management.read(ARTICLE_FILE_PATH)
        nombres = []
        contacto = []

        for user in contacts:
            if user.get('nombre') == name:
                nombres.append(user.get('nombre'))
                contacto.append(user)

        if name not in nombres:
            raise ValueError(f"{name} does not exist!!")
        return contacto

        
    def delet(self, name):
        try:
            contacto = self.consultar(name)
            files_management.delet_entity(ARTICLE_FILE_PATH, contacto)
            print(f"El contacto: {name} a sido ELIMINADO")
            '''
            for user in contacts:
                #list_name_user.append(user.get('nombre'))
                if user.get('nombre') == name:
                    contacto = user
                    print(contacto)
                    files_management.delet_entity(ARTICLE_FILE_PATH,contacto)
                    print(f"El contacto: {contacto} a sido ELIMINADO")
                else:
                    raise ValueError(f"{name} does not exist!!")
            '''

        except FileNotFoundError as e:
            raise ValueError (f"File not found", e)
            '''
            if not name in list_name_user:
                print('El contacto no existe')
            if list_name_user == []:
                print('Tu libreta esta vacia')
            '''

        
    def delete_file(self):
        try:
            files_management.delete_file(ARTICLE_FILE_PATH)
        except FileNotFoundError as error:
            print("Could not delete -> ", error)
