# system-database
System Database with Flask and HTML
This is a simple system database application built using Flask, a Python web framework, and HTML for front-end user interface. The application allows users to create, read, update, and delete system entries in a database.

Prerequisites
Python 3.x installed
Flask library installed
SQLite database installed
Setup
Clone the repository to your local machine.
bash
Copy code
git clone https://github.com/Emetegift/system-database.git
Navigate to the project directory.
bash
Copy code
cd system-database
Install the Flask library.
Copy code
pip install flask
Create a new SQLite database file named system_db.sqlite in the project directory.
Usage
Run the Flask application.
Copy code
python app.py
Open a web browser and go to http://localhost:5000 to access the system database application.
Use the user interface to perform CRUD (Create, Read, Update, Delete) operations on the system entries in the database.
You can add new system entries by filling out the form and clicking the "Add System" button.
You can view existing system entries in a tabular format, edit their details by clicking the "Edit" button, and delete entries by clicking the "Delete" button.
The changes made to the system entries will be reflected in the database.
Technologies Used
Flask: A lightweight and flexible web framework for Python.
HTML: A markup language used for creating web pages.
Files and Directory Structure
app.py: The main Flask application file that contains the routing and logic for handling requests and responses.
templates/: A directory containing HTML templates for rendering web pages.
static/: A directory containing static files such as CSS stylesheets and images.
Contributing
If you wish to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Contributions are always welcome!

License
This project is licensed under the MIT License.

Acknowledgements
Flask: https://flask.palletsprojects.com/
SQLite: https://www.sqlite.org/
HTML: https://developer.mozilla.org/en-US/docs/Learn/HTML
