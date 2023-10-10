# AirBnB Clone - The Console

## Project description
- This project is the first step to building a web AirBnB clone application. It consists of a custom command line interface for data management, and the base classes for the storage of this data. 
- The goal of the project is to deploy on server a simple copy of the [AirBnB website](airbnb.com).
## Command interpreter
- The Console.py is a command interpreter that manages all other AirBnB objects.
- Console manages objects via the command interpreter, to create, update, and destroy those objects, also store and persist the objects to a file (JSON file)
### How to start it
You can use either interactive way `$ ./console.py` or non-interactive way `$ echo "help" | ./console.py` to start a session. A prompt `(hbnb)` will appear and you can type commandsand followed by a new line. The prompt is in an infinite loop until `quit` to exit the loop. 
### How to use it
- Pycodestyle was taken into accout and implemented for all files
- FileStorage class is in charge of managing the storage through a JSON file (`file.json`), those instances are created, updated or deleted, all this through a FileStorage instance called `storage`.
- Console is used to manage the storage of class instances (`file.json`), the console can be used and executed in two ways, interactive and non-interactive mode:
`Interactive mode:`
'''
$ ./console.py
(hbnb) help

Documented  commands  (type help <topic>):
==========================================
EOF  all  create  destroy  help  quit  show  update 

(hbnb)
(hbnb)
(hbnb) quit
$
'''
`Non-Interactive mode:`
'''
$ echo "help" | ./console.py
(hbnb)

Documented  commands  (type help <topic>):
==========================================
EOF  all  create  destroy  help  quit  show  update 
(hbnb)
$
$ cat test\_help
help
$
$ cat test\_help | ./console.py
(hbnb)

Documented  commands  (type help <topic>):
==========================================
EOF  all  create  destroy  help  quit  show  update 
(hbnb)
'''
- Below is a brief commands list:
|method/command|description|example|
|--------------|-----------|-------|
|create <class> |Creates a new instance of BaseModel, save it to the JSON file and print the id|$ create BaseModel|
|show <class>|Prints the string representation of an instance based on the class name and id.|$ show BaseModel 1234-1234-1234|
|destroy|Deletes an instance based on the class name and id, and save the change into the JSON file)|$ destroy BaseModel 1234-1234-1234|
|all|Prints all string representation of all instances based or not on the class name.|$ all BaseModel|
|update|Updates an instance based on the class name and id by adding or updating attribute, and save the change into the JSON file).|$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"|
|help|List all available commands|(hbnb) help or help quit|
|quit or EOF|Exit the console|(hbnb) quit|
|EOF|Exit the console||
### tests
All tests are in tests/test\_models directory. They are developed and implemented for all the classes of the project using `unittest` in a different test environment, in order not to bother the JSON storage working file `file.json`, which will be deleted at the end of the tests.

To test the classes in the project:
'''
python3 -m unittest discover tests
'''
To test a specitic model:
'''
python3 -m unittest tests/test\_models/test\_base\_model
'''
### examples
'''
$ ./console.py 
(hbnb) create BaseModel
ae8bed8f-eff4-4e49-851c-d94214bda95d
(hbnb) update BaseModel ae8bed8f-eff4-4e49-851c-d94214bda95d user\_name "Bob"
(hbnb) show BaseModel ae8bed8f-eff4-4e49-851c-d94214bda95d
[BaseModel] (ae8bed8f-eff4-4e49-851c-d94214bda95d) {'id': 'ae8bed8f-eff4-4e49-851c-d94214bda95d', 'created\_at': datetime.datetime(2023, 10, 10, 6, 33, 19, 767337), 'updated\_at': datetime.datetime(2023, 10, 10, 6, 33, 19, 767348), 'user\_name': 'Bob'}
(hbnb)
'''

'''
$ ./console.py 
(hbnb) create User
a7095b86-014e-4a34-b140-86711a10243a
(hbnb) destroy BaseModel ae8bed8f-eff4-4e49-851c-d94214bda95d
(hbnb) destroy User a7095b86-014e-4a34-b140-86711a10243a
(hbnb) all
[]
'''
