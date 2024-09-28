from marshmallow import Schema, fields, validates, ValidationError;

class ContactSchema(Schema):
    fullname = fields.String(
        required=True, 
        validate=lambda x: 3 <= len(x) <= 96,
        error_messages={
            'required': 'El nombre es obligatorio.',
            'validator_failed': 'El nombre debe tener entre 3 y 96 caracteres.'
        }
    )
    email = fields.Email(
        required=True, 
        error_messages={
            "required": "El correo es obligatorio.",
            "invalid": "El formato del correo electrónico no es válido."
        }
    )
    phone = fields.String(
        required=False, 
        validate=lambda x: len(x) <= 15,
        error_messages={
            'validator_failed': 'El teléfono no debe tener más de 15 caracteres.'
        }
    )
