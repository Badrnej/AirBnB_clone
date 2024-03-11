#!/usr/bin/python3
"""
Module containing the BaseModel class
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    Defines the BaseModel class
    """

    id_generator = uuid.uuid4

    def __init__(self):
        """
        Initializes a new instance of BaseModel
        """
        self.id = str(BaseModel.id_generator())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of BaseModel instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        obj_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        return obj_dict

# Testing
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key]))

