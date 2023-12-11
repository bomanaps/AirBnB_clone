# AirBnB_clone

![815046647d23428a14ca](https://github.com/bomanaps/AirBnB_clone/assets/105924200/fc22d0ce-a9c9-425b-9567-683864249b23)

# AIRBnB_clone
This project is the first in a series that will recreate AIRBnB from the ground up, starting with a console.


### Description :page_with_curl:
The goal of this four-part project is to construct a basic clone of the AIRBnB app. This is the first phase. Using the Cmd Python module, a simple console was built in the first phase of the project to handle all of the objects. It was capable of implementing the methods create, show, update, all, and destroy for the classes and subclasses that were already in place.

### Environment: :computer:
Python 3 was used to create the console in UBUNTU 20.04LTS. Check out the documentation and further details at (https://www.python.org/). :link:

### Requirements :clipboard:
Python 3 proficiency, familiarity with a command-line interpreter, Ubuntu 14.04 machine, and Pep8 style corrector knowledge are required.

### File and Directories :arrow_down:
    models - contains all the classes.
    tests - contain all unit tests
    console.py - entry point for our command interpreter
    models/base_model.py - base class for models.
    models/engine - contains all storage classes

  
### File description. :arrow_down:
AUTHORS Contains info about authors of the project 

    ->base_model.py Defines BaseModel class (parent class)
    ->methods user.py Defines subclass User 
    ->amenity.py Defines subclass Amenity 
    ->city.py Defines subclass City 
    ->place.py Defines subclass Place 
    ->review.py Defines subclass Review 
    ->state.py Defines subclass State 
    ->file_storage.py Creates new instance of class serializes and deserializes data
    ->console.py creates object, retrieves object from file, does operations on objects, updates       
      attributes of object and destroys object

    ->test_base_model.py unit tests for base_model 
    ->test_user.py unit tests for user 
    ->test_amenity.py unit tests for amenity 
    ->test_city.py unit tests for city 
    ->test_place.py unit tests for place 
    ->test_review.py unit tests for review 
    ->test_state.py unit tests for state 
    ->test_file_storage.pyunittests for file_storage 
    ->test_console.py unit tests for console

### Usage  :arrow_forward:
Method Summary: 
  Produce generates a given class display object. prints an instance's string representation depending 
  its class name and id. prints every instance's string representation, whether or not the class name has
  changed. adds or modifies attributes to an instance, updating it according to the class name and id
  (saving the change into the JSON file) demolish saves the modification to the JSON file and deletes an     instance based on the class name and id. total Obtain the quantity of a class help instance. prints        details on a particular command quit or EOF
  
            -> Get out of the program. 
                Example No. 1: git:(feature) ➜ AirBnB_clone



### Authors :stars:
`Kevin Kipkoech` :star:
`Mercy Boma`:star: