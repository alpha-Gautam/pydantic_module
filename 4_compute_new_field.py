from pydantic import BaseModel, Field, AnyUrl, EmailStr, field_validator, computed_field
from typing import Optional, List, Dict, Annotated



class patient(BaseModel):
    id: Annotated[str, Field(max_length=50, min_length=1)]  
    name: str
    age: int
    number: str
    email: EmailStr
    allergies: Annotated[List[str], Field(default=None, max_length=10)]
    medical_history: Optional[Dict[str, str]] = None
    
    @computed_field
    def is_adult(self) -> bool:
        return self.age >= 18
    
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        allowed_domains = ['reck.com', 'test.com']

        domain = value.split("@")[-1]
        if domain not in allowed_domains:
            raise ValueError('Email domain is not allowed')
        return value
    

    @field_validator('age', mode='after')
    @classmethod
    def age_validator(cls, value):
        if 18 < value > 50:
            raise ValueError('Age must be between 18 and 50')
        return value






patient_data={
    "id": "12345",
    "name": "John Doe",
    "age": 30,
    "number": "555-1234",
    "email": "johndoe@reck.com"
}

p1= patient(**patient_data) 


def make_patient(data:patient):
    
    print("patient is created!...")
    print(type(data))
    print(data)
    
    return data

print(type(p1))
print(p1)

make_patient(p1)
