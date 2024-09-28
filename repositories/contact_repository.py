from utils.db import db;
from models.contact import Contact;
from sqlalchemy.exc import SQLAlchemyError;
from typing import List;

class ContactRepository:
    
    @staticmethod
    def get_contacts() -> List[Contact]:
        try:
            return db.session.query(Contact).all()
        except SQLAlchemyError as e:
            raise Exception("Error al conectar con la base de datos") from e
    
    @staticmethod
    def add_contact(contact: Contact) -> None:

        try:
            db.session.add(contact)    
            db.session.commit();
        except SQLAlchemyError as e:
            db.session.rollback()  # Deshacer la sesión en caso de error
            raise Exception("Error al guardar el contacto en la base de datos") from e
    
    # @staticmethod
    # def add_contact(contact: Contact) -> None:

    #     try:
    #         db.session.add(contact)    
    #         db.session.commit();
    #     except SQLAlchemyError as e:
    #         db.session.rollback()  # Deshacer la sesión en caso de error
    #         raise Exception("Error al guardar el contacto en la base de datos") from e