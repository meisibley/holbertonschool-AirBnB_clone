# AirBnB Clone - The Console

## Project description
- This project is the first step to building a web AirBnB clone application. It consists of a custom command line interface for data management, and the base classes for the storage of this data. 
- The goal of the project is to deploy on server a simple copy of the [AirBnB website](airbnb.com).
## Command interpreter
- The Console.py is a command interpreter that manages all other AirBnB objects.
- Console manages objects via the command interpreter, to create, update, and destroy those objects, also store and persist the objects to a file (JSON file)
### How to start it
You can use either interactive way `$ ./console.py` or non-interactive way `$ echo "help" | ./console.py` to start a session. A prompt `(hbnb)` will appear and you can type commandsand followed by a new line. The prompt is in an infinite loop until `quit` or `EOF` to exit the loop. 
### How to use it
Below is a brief commands list:
|method/command|description|example|
|--------------|-----------|-------|
|create <class> |Creates a new instance of BaseModel, save it to the JSON file and print the id|$ create BaseModel|
|show <class>|Prints the string representation of an instance based on the class name and id.|$ show BaseModel 1234-1234-1234|
|destroy|Deletes an instance based on the class name and id, and save the change into the JSON file)|$ destroy BaseModel 1234-1234-1234|
|all|Prints all string representation of all instances based or not on the class name.|$ all BaseModel|
|update|Updates an instance based on the class name and id by adding or updating attribute, and save the change into the JSON file).|$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"|
|help|List all available commands|(hbnb) help|
|quit|Exit the console|(hbnb) quit|
|EOF|Exit the console|(hbnb) ^C|
### examples
