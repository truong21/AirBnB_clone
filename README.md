# 0x00. AirBnB clone - The console
![Image of Holberton B&B Logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

## Holberton School Airbnb Clone - Command Interpreter 
### 
This is the first of a multipart project working towards building a full web application clone of AirBnb. In this first part, the Python programming language is used to build a command interpreter for the clone's web app. This command interpreter is similar to a BASH shell but it is designed for a specific use case of managing objects related to this project. The following projects will incorporate additional sections like HTML/CSS templating, database storage, API and front-end integration.

The console can excute the following functions:
-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

## Installation and Start
In the command line run `./console.py` or `echo help | ./console.py`

Interactive Mode:
How to ask for help:
```
PROMPT~> ./console.py
(hbtn) help

Documented Commands (type help <topic>)
======================================
EOF   help   quit

(hbtn)
(hbtn)
(hbtn) quit
PROMPT~>
```
Non-Interactive Mode:
```
PROMPT~> echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
PROMPT~> cat test_help
help
PROMPT~> cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
PROMPT~>
```
## Usage
This interpreter has basic console commands such as EOF, quit, help, create, destroy, update, show, count and all.

## Command Sytax and Usage:

Command | Syntax | Output
------- | ------ | ------
help | `help *[option]*` | Lists all available commands, or displays what option does
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter
create | `create [class_name]` | Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]`| Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` | Displays all attributes of class_name.object_id
all | `all [class_name]`, `all` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` or  | Deletes all attributes of class_name.object_id
count | `count [class_name]`| Counts all the instances with class name specified


### Files
File Name | Description
--- | ---
`models/base_model.py` | Base Class with public instance attributes and methods
`models/amenity.py` | An Amenity class that inherits from BaseModel
`models/city.py` | A City class that inherits from BaseModel
`models/place.py` | A Place class that inherits from BaseModel
`models/review.py` | A Review class that inherits from BaseModel
`models/state.py` | A State class that inherits from BaseModel
`models/user.py` | A User class that inherits from BaseModel
`models/engine/file_storage.py` | A class that serializes instances to a JSON file and deserializes JSON file to instances
`tests/test_models/` | Unittests for BaseModel, User, amenity, city, place, review, state, and FileStorage

## Example Usage
```python3
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb) help quit
Quit command to exit the program
(hbnb)
(hbnb) show User
** instance id missing **
(hbnb) show User (24ed1cb3-8f8a-4081-878e-60fdce47a42d)
** no instance found **
(hbnb) show User 38f22813-2753-4d42-b37c-57a17f1e4f88
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@holbertonshool.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Holberton', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
(hbnb)
(hbnb) show Amenity
** instance id missing **
(hbnb) show Amenity 9e4faeca-d073-4b16-b4c7-92b354c0c311
[Amenity] (9e4faeca-d073-4b16-b4c7-92b354c0c311) {'created_at': datetime.datetime(2019, 2, 20, 7, 6, 32, 790316), 'updated_at': datetime.datetime(2019, 2, 20, 7, 6, 32, 790352), 'id': '9e4faeca-d073-4b16-b4c7-92b354c0c311'}
(hbnb)
(hbnb) update User f56a70ad-a3f0-4db9-8b6b-67315e473558 first_name Dave
(hbnb) show User f56a70ad-a3f0-4db9-8b6b-67315e473558
[User] (deaf744b-c904-4b56-8823-71acc18a529c) {'created_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138370), 'updated_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138489), 'id': 'deaf744b-c904-4b56-8823-71acc18a529c', 'first_name': 'Dave'}
(hbnb)
(hbnb) destroy User f56a70ad-a3f0-4db9-8b6b-67315e473558
(hbnb) show User f56a70ad-a3f0-4db9-8b6b-67315e473558
** no instance found **
(hbnb)
(hbnb) create User
22f08bfa-8b88-46f8-93e1-714c78834e0b
(hbnb) create Place
7aa8d69a-84bf-48bd-83b4-fdfe59fcc045
(hbnb) create State
e7a7169e-f663-49d2-b765-b78329dd248f
(hbnb) all
["[State] (e7a7169e-f663-49d2-b765-b78329dd248f) {'created_at': datetime.datetime(2019, 2, 20, 7, 16, 24, 310882), 'id': 'e7a7169e-f663-49d2-b765-b78329dd248f', 'updated_at': datetime.datetime(2019, 2, 20, 7, 16, 24, 310923)}", "[Place] (7aa8d69a-84bf-48bd-83b4-fdfe59fcc045) {'created_at': datetime.datetime(2019, 2, 20, 7, 16, 20, 686217), 'id': '7aa8d69a-84bf-48bd-83b4-fdfe59fcc045', 'updated_at': datetime.datetime(2019, 2, 20, 7, 16, 20, 686248)}", "[User] (22f08bfa-8b88-46f8-93e1-714c78834e0b) {'created_at': datetime.datetime(2019, 2, 20, 7, 16, 17, 45550), 'id': '22f08bfa-8b88-46f8-93e1-714c78834e0b', 'updated_at': datetime.datetime(2019, 2, 20, 7, 16, 17, 45621)}"]
```

### Authors
* Rashaad Colbert | [GitHub](https://github.com/rcolbert30) 
* Phu Truong | [GitHub](https://github.com/truong21) 
