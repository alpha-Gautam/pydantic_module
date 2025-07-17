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
    
    
patient_address={"state":"Uttar Pradesh","cit":"gorakhpur","street":"Street 123","pincode":273001}

patient_address = address(**patient_address)

patient_data ={"name":'albert',"age":30,"address":patient_address}


patient1 = patient(**patient_data)

# print("Patient ID:", patient1.id)
# print("Patient Name:", patient1.name)
# print("Patient Age:", patient1.age)
# print("Patient Address:", patient1.address)

print(patient1)
print(type(patient1))

print("=================")

# we also control how the data is serialized
#  patient1.model_dump(include=["address"]) returns a dictionary representation of the model
# patient1.model_dump(exclude=["address"]) excludes the address field

# there in exclude_unset=True, which will exclude fields that are not set (i.e., have default values) from the output
print(patient1.model_dump())
print(type(patient1.model_dump()))

print("=================")

# patient1.model_dump_json() returns a JSON string representation of the model
# patient1.model_dump_json(include=["address"]) returns a JSON string with only the address field
# patient1.model_dump_json(exclude=["address"]) excludes the address field in the JSON output   
# there is also an option to exclude_unset=True, which will exclude fields in the JSON output

print(patient1.model_dump_json())
print(type(patient1.model_dump_json()))

print("=================")

