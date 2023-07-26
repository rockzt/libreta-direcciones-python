import os

import file_manager

current_path = os.path.dirname(__file__)
ARTICLE_FILE_NAME = "article.json"
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
        interior,
        colonia,
        municipio,
        ciudad,
        estado,
        pais,
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
        return file_manager.read_json_file(ARTICLE_FILE_PATH)

    def save(self):
        dict_article = self.as_dict()

        try:
            file_manager.get_is_file_exist(ARTICLE_FILE_PATH)
            file_manager.update_json_file(ARTICLE_FILE_PATH, dict_article,
                                          True)

        except FileNotFoundError:
            file_manager.create_json_files(ARTICLE_FILE_PATH, [dict_article])
