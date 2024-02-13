#!/usr/bin/python3
"""
The Console Module
"""

import cmd
from models import storage
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""

        return True

    def do_EOF(self, arg):
        """Exit the program on EOF."""

        print()  # Add a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on an empty line."""

        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it,
        and prints the id."""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""

        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class name missing **")
            return
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""

        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class name missing **")
            return
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name."""

        if not arg or arg in storage.classes():
            print([str(value) for value in storage.all().values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute."""
        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class name missing **")
            return
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        setattr(storage.all()[key], attribute_name, attribute_value)
        storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
