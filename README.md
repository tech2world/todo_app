# Flask To-Do App

<!-- ![App Screenshot](screenshot.png) -->

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Author](#author)
<!-- - [License](#license) -->

## Introduction

The Flask To-Do App is a simple yet powerful task management tool built using the Flask web framework and SQLAlchemy. This application allows users to create, update, complete, and delete tasks, making it an ideal choice for organizing and tracking tasks in a straightforward manner.

The app provides an intuitive user interface for managing tasks and displays their creation dates, ensuring that users can prioritize their work efficiently. The project demonstrates the use of Flask's routing, templates, forms, and database integration to create a seamless task management experience.

## Features

- Create tasks with descriptions.
- Display tasks along with their creation dates.
- Update task content.
- Mark tasks as completed.
- Delete tasks.
- Responsive web design for various screen sizes.
- Form validation to prevent empty task content.
- Organized project structure and clean codebase.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/flask-todo-app.git
   cd flask-todo-app
   ```

2. Create a virtual environment (recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```sh
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Run the app:
   ```sh
   python app.py
   ```

## Usage

1. Access the app by visiting `http://127.0.0.1:5000/` in your web browser.
2. Create a new task by entering its description and clicking "Add Task."
3. View, update, complete, and delete tasks using the provided links.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`
3. Make your changes and commit them: `git commit -am 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Create a pull request.

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->

## Author
- GitHub: [@tech2world](https://github.com/tech2world)
