from pydantic import BaseModel, Field, AnyUrl, EmailStr
from typing import Optional, List, Dict, Annotated



class patient(BaseModel):
    id: Annotated[str, Field(max_length=50, min_length=1)]  
    name: str
    age: int
    number: str
    email: Optional[str] = None
    allergies: Annotated[List[str], Field(default=None, max_length=10)]
    medical_history: Optional[Dict[str, str]] = None
    
    
def new_functions():
    ...  # Placeholder for additional functions if needed

data={
    "id": "12345",
    "name": "John Doe",
    "age": 30,
    "number": "555-1234",
    "email": "john.doe@example.com"
}

p1= patient(**data)


print(type(p1))
print(p1)