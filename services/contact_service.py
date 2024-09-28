from models.contact import Contact;
from schemas.contact_schema import ContactSchema;
from repositories.contact_repository import ContactRepository;
from sqlalchemy.exc import SQLAlchemyError
from typing import List;
from marshmallow import ValidationError;

class ContactService:
    
    @staticmethod
    def findAll() -> List[Contact]:
        return ContactRepository.get_contacts();
    
    @staticmethod
    def create(data: dict) -> Contact:
        schema = ContactSchema()
        try:
            validated_data = schema.load(data)
        except ValidationError as ve:
            raise ValueError(ve.messages)
        
        contact = Contact(fullname=data['fullname'], email=data['email'], phone=data.get('phone'))
        
        try:
            ContactRepository.add_contact(contact)
        except SQLAlchemyError as e:
            print(f"Error al guardar el contacto: {e}")
            raise Exception("Error al guardar el contacto en la base de datos") from e
        
        return contact;