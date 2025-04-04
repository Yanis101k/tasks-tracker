Tasks Tracker

The source code for this project is available on GitHub: https://github.com/Yanis101k/tasks-tracker

 Identification : 
  - Name : Kaced Yanis 
  - P Number : P482285
  - Course Code : IY499

 Declaration of Own Work

  I confirm that this assignment is my own work.
  Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.
 
 Introduction : 
  This code represents a simple implementation of a task tracking web application using HTML, CSS, JavaScript, and a Python backend.
  The app allows users to register, log in, and manage their personal tasks with features like task creation, editing, deletion, and live searching. 
  Tasks are stored in a local JSON file , and i addded a custom desktop entry icon in my computer .
 
 Installation

  To run the application, ensure you have Python installed, and then install the required dependencies from the requirements.txt file using the following command:
  pip install -r requirements.txt
 
 How to use : 
  1 - Navigate to index.html to access the homepage.
  2 - Register a new account.
  3 - Log in with your credentials.
  4 - Add, edit, delete, or search tasks.
 
 Runing the application
 
 1 - open your terminal and change the directory to the root of project (tasks-tracker/) run this command :
  python3 backend/app.py
 2 - Then open your browser and go to :
  http://localhost:8000

 Application features : 

   - User registration and login

   - Task creation, editing, deletion

   - Live search by task title

   - Responsive UI with modern styling
 
 Libraries Used

 The following libraries are used in this project:

  - Python Standard Library (http.server, os, json)

  - JavaScript (Vanilla)

  - CSS (custom responsive design)
 
  - html ( structure website content ) 

 Project Structure

  backend/: Contains the Python server and logic

  frontend/: Contains HTML, CSS, JS for the user interface

  data/: Stores tasks and users in JSON files

  tests/: Contains test cases for backend logic

 Unit Tests

  The project includes test cases for user and task models, as well as authentication logic.

  To run the unit tests, navigate to the project directory and run:

  python -m unittest discover tests

  This will run all the test cases defined in the test files in the tests/ folder.
