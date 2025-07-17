from pydantic import BaseModel, Field, AnyUrl, EmailStr, model_validator
from typing import Optional, List, Dict, Annotated



class patient(BaseModel):
    id: Annotated[str, Field(max_length=50, min_length=1)]  
    name: str    
    age: int
    number: str
    email: Optional[str] = None
    allergies: Annotated[List[str], Field(default=None, max_length=10)]
    medical_history: Optional[Dict[str, str]] = None
    contact_info: Optional[Dict[str, str]] = None  # New field for contact information
    
    
    @model_validator(mode='after')
    def validate_contact_info(cls, model):
        if (model.age< 18 or model.age>60) and  "emergency_contact" not in model.contact_info:
            raise ValueError('Emergency contact is required for patients under 18 or over 60')
        
        return model
            
    
    
    
def new_functions():
    ...  # Placeholder for additional functions if needed

data={
    "id": "12345",
    "name": "John Doe",
    "age": 10,
    "number": "555-1234",
    "email": "john.doe@example.com",
    "contact_info": {
        "emergency_contact": "Jane Doe",
        "phone": "555-5678"
    }
}

p1= patient(**data)


print(type(p1))
print(p1)