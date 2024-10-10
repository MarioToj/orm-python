from utils.db import db;
from models.contact import Contact;
from sqlalchemy.exc import SQLAlchemyError;
from werkzeug.exceptions import RequestTimeout
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
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()  # Deshacer la sesión en caso de error
            raise RequestTimeout("Error al guardar el contacto en la base de datos") from e
    
    @staticmethod    
    def find_by_email(email: str):
        try:
            return db.session.query(Contact).filter_by(email=email).first()
        except SQLAlchemyError as e:
            raise RequestTimeout(f'error al conectar con la base de datos: {str(e)}')
    
    @staticmethod    
    def find_by_id(id: int):
        try:
            contact = Contact.query.filter_by(id=id).first_or_404()
            
            return contact 
        except SQLAlchemyError as e:
            raise RequestTimeout(f'error al conectar con la base de datos: {str(e)}')
    @staticmethod   
    def save(contact):
        
        try:
            db.session.add(contact)
            db.session.commit()
            return contact
        except Exception as e:
            db.session.rollback()
            print(f'error al guardar el contacto{e}')
            return None
        
    @staticmethod    
    def delete(id: int):
        try:
            contact = Contact.query.get(id)
            if contact:
                db.session.delete(contact)
                db.session.commit()
            else:
                return "Contacto no encontrado", 404
        except SQLAlchemyError as e:
            db.session.rollback()
            raise RequestTimeout(f'error al conectar con la base de datos: {str(e)}')  