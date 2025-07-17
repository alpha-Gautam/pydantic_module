from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List

class address(BaseModel):
    state:str
    cit:str
    street:str
    pincode:int
    

class patient(BaseModel):
    id:UUID = Field(default=uuid4())
    name:str
    age:int
    address:address
    
    
    

patient_address = address(
    state="Uttar Pradesh",
    cit="gorakhpur",
    street="Street 123",
    pincode=273001)


patient_data = patient(
    name='albert',
    age=30,
    address=patient_address
)


print("Patient ID:", patient_data.id)
print("Patient Name:", patient_data.name)
print("Patient Age:", patient_data.age)
print("Patient Address:", patient_data.address)