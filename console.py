#!/usr/bin/python3
"""Command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """ The Command processor """

    prompt = "(hbnb)"
    list_classes = ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'State', 'Review']
    list_command = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """ Parses the command input """
        if '.' in arg and '(' in arg and ')' in arg:
        cls = arg.split('.')
        cnd = cls[1].split('(')
        args = cnd[1].split(')')
        if cls[0] in HBNBCommand.list_classes and cnd[0] in HBNBCommand.list_command:
            arg = cnd[0] + ' ' + cls[0] + ' ' + arg[0]
        return arg
  
    def help_help(self):
        """ The help command description """
        print("Provide description of a given command")
  
    def emptyline(self):
        """ do nothing on empty line """
        pass
  
    def do_count(self, class_name):
        """ Counts number of instances of a class """
        count = 0
        all_objects = storage.all()
        for k, v in all_objects.items():
        clas_s = k.split('.)'
            if clas_s[0] == class_name:
                count = count + 1
            print(count)
  
    def do_create(self, type_model):
    """ Creates an instance according to a given class """
        if not type_model:
            print("*** Class name missing ***")
        elif type_model not in HBNBCommand.list_classes:
            print("*** Class doesn't exist ***")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'City':City, 'Amenity': Amenity, 'State': State, 'Review': Review}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Show string representation of an instance passed """
        if not arg:
            print("*** Class name missing ***")
            return
        args = arg.split(' ')

        if args[0].not in HBNBCommand.list_classes:
            print("*** Class doesn't exist ***")
        elif len(args) == 1:
            print("*** instance id missing ***")
        else:
            all_objects = storage.all()
            for key, value in all_objects.items():
                object_name = value.__class__.__name__
                object_id = value.id
                if object_name == args[0] and object_id == args[1].strip("*"):
                    print(value)
                    return
            print("*** no instance found ***")

    def do_destroy(self, arg):
        """ Delete an instance passed """
        if not arg:
            print(" *** Class name missing *** ")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.list_classes:
            print("*** Class doesn't exist *** """)
        elif len(args) == 1:
            print(" *** Instance id missing ***")
        else:
            all_objs = storage.all()
            for key, value in all_objects.items():
                object_name = value.__class__.__name__
                object_id = value.id
                if object_name == args[0] and object_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    reurn
                print("*** No instance found ***")
        
    def do_all(self, arg):
        """ Prints string reprentation of all instances of a given class """
        if not arg:
            print("*** Class name missing ***")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.list_classes:
            print("*** Class doesn't exist ***")
        else:
            all_objects = storage.all()
            list_instances = []
            for key, value in all_objects.items():
                object_name = value.__class__.__name__
                if object_name == args[0]:
                    list_instances += [value.__str__]
                print(list_instances)

    def do_update(self, arg):
        """ Update an instance based on the class name and id """
        if not arg:
            print("*** Class name missing ***")
            return
        a = ""
        for argv in arg.split(','):
            a = a + argv
        args = shlex.split(a)
        if args[0] not in HBNBCommand.list_classes:
            print(" *** Class doesn't exist *** ")
        elif len(args) == 1:
            print(" *** instance id missing ***")
        else:
            all_objects = storage.all()
            for key, object in all_objects.items():
                object_name = object.__class__.__name__
                object_id = object.id
                if object_name == args[0] and object_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("*** attribute name missing*** ")
                    elif len(args) == 3:
                        print(" *** Value missing *** ")
                    else:
                        setattr(object, args[2], args[3])
                        storage.save()
                print(" *** No instance found ***")

    def do_quit(self, line):
        """ Quit command to exit intrepeter """
        return True
  
    def do_EOF(self, line):
        """ EOF command to exit intepreter """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
