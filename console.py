#!/usr/bin/python3
"""Command interpreter"""
""" Import the necessary file required """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex

class HBNBCommand(cmd.Cmd):
  """ The Command processor """
  prompt = "(hbnb)"
  l_classes = ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'State', 'Review']
  l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

  def precmd(self, arg):
    """ Parses the command input """
    if '.' in arg and '(' in arg and ')' in arg:
      cls = arg.split('.')
      cnd = cls[1].split('(')
      args = cnd[1].split(')')
      if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
        arg = cnd[0] + ' ' + cls[0] + ' ' + arg[0]
      return arg
  
  def help_help(self):
    """ The help command description """
    print("Provide description of a given command")
  
  def emptyline(self):
    """ do nothing empty line """
    pass
  
  def do_count(self, cls_name):
    """ Counts number of instances """
  
  def do_create(self, type_model):
    """ Creates an instance according to a given class """
  
  def do_show(self, arg):
    """ Show string representaion of an instance passed """
  
  def do_destroy(self, arg):
    """ Delete an instance passed """
  
  def do_all(self, arg):
    """ Prints string reprentation of all instances of a given class """
  
  def do_update(self, arg):
    """ Update an instance based on the class name and id """
  
  def do_quit(self, line):
    """ Quit command to exit intrepeter """
    return True
  
  def do_EOF(self, line):
    """ EOF command to exit intepreter """
    return True



