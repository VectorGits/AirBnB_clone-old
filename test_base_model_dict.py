#!/usr/bin/python3

# import the BaseModel class from the models package for usage in the script
from models.base_model import BaseModel

# Create an instance of the BaseModel class.
my_model = BaseModel()

# Set attributes for the my_model instance.
my_model.name = "My_First_Model"
my_model.my_number = 89

# Print the 'id' attribute of my_model.
print(my_model.id)

# print the string representation of my_model using the __str__ method
print(my_model)

# print the data type of the 'created_at' attribute of my_model
print(type(my_model.created_at))
print("--")

# convert the my_model instance to a dictionary using the to_dict method
my_model_json = my_model.to_dict()

# print the dictionary representation of my_model
print(my_model_json)
print("JSON of my_model:")

# iterate through the dictionary keys,
# printing each key, its data type, and value
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print("--")

# create a new instance of the BaseModel class using the dictionary my_model_json
my_new_model = BaseModel(**my_model_json)

# print the 'id' attribute of my_new_model
print(my_new_model.id)

# print the string representation of my_new_model
print(my_new_model)

# print the data type of the 'created_at' attribute of my_new_model
print(type(my_new_model.created_at))
print("--")

# print whether my_model and my_new_model are the same instance
print(my_model is my_new_model)
