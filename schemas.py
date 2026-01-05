from pydantic import BaseModel
 
class UserSchema(BaseModel):
     name: str
     email : str
     age : int
     password : str

class UserUpdateSchema(BaseModel):
     name: str
     email:str
     password: str
     