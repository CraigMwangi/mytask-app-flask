# Flask To-Do App

This is a simple web-based to-do application built with Flask. The app allows users to add tasks, categorize them, set a priority level, and a deadline. Users can also mark tasks as completed or delete them.

## Features

- Add a new task with a category, priority level, and deadline.
- View all active tasks.
- View completed tasks.
- Mark tasks as completed.
- Delete tasks.

## Future Work

There are several areas where this application can be further improved:

1. **User Authentication:** The current version of the application does not support user-specific tasks. In the future, we could add user authentication and allow users to manage their individual tasks.

2. **Task Notifications:** Another useful feature could be to add notifications for upcoming or overdue tasks. This would help users to manage their tasks more efficiently.

3. **Search and Filtering:** As the number of tasks grows, it would be helpful to have search functionality and the ability to filter tasks by categories or priorities.

4. **Integration with External Calendars:** An integration with external calendars (like Google Calendar) would be a great addition to help users visualize their tasks in their preferred calendar applications.

## Getting Started

These instructions will guide you in setting up a local development instance of the project.

### Prerequisites

Make sure you have Python 3.8+ and pip installed on your system.

### Installation

1. Install ZIP:
   `mytask-app-flask.zip`

2. Navigate to the project directory:
   `cd mytask-app-flask`

3. Create a new virtual environment and activate it:
   `python -m venv env`
   For Windows:
   `.\env\Scripts\activate`
   For Mac or Linux:
   `source env/bin/activate`

4. Install the dependencies:
   `pip install -r requirements.txt`

5. Run the Flask application:
   `python main.py`

Open your browser and navigate to `http://localhost:5000` to see the application in action.

## Usage

Once the application is running:

- Navigate to `http://localhost:5000` to view the current active tasks.
- Use the 'Add Task' button to create a new task. You will be redirected to `http://localhost:5000/add` where you can enter the task details and submit.
- In the list of tasks, each task has 'Mark as Complete' and 'Delete' buttons to update the status or remove the task.
