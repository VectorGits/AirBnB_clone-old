#!/usr/bin/python3

# import the BaseModel class from the models package for usage in the script
from models.base_model import BaseModel

# create an instance of the BaseModel class
my_model = BaseModel()

# set attributes for the my_model instance
my_model.name = "My First Model"
my_model.my_number = 89

# print the string representation of my_model using the __str__ method
print(my_model)

# call the save method, updating the 'updated_at' attribute
my_model.save()

# print the updated string representation of my_model
print(my_model)

# convert the my_model instance to a dictionary using the to_dict method
my_model_json = my_model.to_dict()

# print the dictionary representation of my_model
print(my_model_json)
print("JSON of my_model:")

# iterate through the dictionary keys, printing each key, its data type, and value
for key in my_model_json.keys():
   print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
