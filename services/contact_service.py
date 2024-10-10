from models.contact import Contact;
from schemas.contact_schema import ContactSchema;
from werkzeug.exceptions import RequestTimeout, BadRequest
from repositories.contact_repository import ContactRepository;
from sqlalchemy.exc import SQLAlchemyError
from typing import List;
from marshmallow import ValidationError;

class ContactService:
    
    @staticmethod
    def findAll() -> List[Contact]:
        return ContactRepository.get_contacts()
    
    @staticmethod
    def create(data: dict) -> Contact:
        schema = ContactSchema()
        
        try:
            existing_contact = ContactRepository.find_by_email(data['email'])
        except Exception as e:
            raise RequestTimeout(description='Error conecting to database')
        
        if existing_contact:
            raise ValueError("duplicate_email")
        
        try:
            validated_data = schema.load(data)
        except ValidationError as ve:
            raise ValueError(ve.messages)
        
        contact = Contact(fullname=data['fullname'], email=data['email'], phone=data.get('phone'))
        
        try:
            ContactRepository.add_contact(contact)
        except SQLAlchemyError as e:
            print(f"Error al guardar el contacto: {e}")
            raise RequestTimeout("Error al guardar el contacto en la base de datos") from e
        
        return contact
    
    @staticmethod
    def findOneById(id: int):
        try:
            found_contact = ContactRepository.find_by_id(id)
        except Exception as e:
            raise RequestTimeout(description="Error conecting to the database")
        return found_contact
        
    @staticmethod
    def update_contact(id, fullname, email, phone):
        
        contact = ContactRepository.find_by_id(id)
        if not contact:
            return None
        
        contact.fullname = fullname
        contact.email = email
        contact.phone = phone
        
        return ContactRepository.save(contact)
    
    @staticmethod
    def delete_contact(id: id):
        try:
            return ContactRepository.delete(id)
        except Exception as e:
            raise RequestTimeout(description="Error conecting to the database")      
    