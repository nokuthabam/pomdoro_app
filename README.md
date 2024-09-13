# Productivity Application

## Table of Contents
1. [Project Description](#project-description)
2. [Key Features](#key-features)
3. [Project Structure](#project-structure)
4. [Application Installation](#application-installation)
5. [Usage](#usage)
6. [Continuous Integration: CircleCI Badge](#continuous-integration-circleci-badge)
7. [Code Coverage: CodeCov Badge](#code-coverage-codecov-badge)
8. [Project Author](#project-author)
9. [License](#license)

## Project Description:
A dynamic web application that allows users
The Productivity Application is designed to help users stay focused and organized by combining two essential tools: a music-enhanced Pomodoro timer and a personal journal. The Pomodoro timer allows users to manage their work and break intervals using the Pomodoro technique, while listening to lofi or chill music to create a calming work environment. The application also includes a journal feature where users can write, format, and track their thoughts or tasks, making it a holistic tool for improving focus and productivity.

### Key Features:
- **Pomodoro Timer:** A focus timer that helps users divide their work into intervals, with customizable focus and break times.
- **Music Integration:** Plays a selection of background music during focus sessions to enhance concentration.
- **Journal:** Allows users to create, format, and save journal entries, helping them document tasks, ideas, or reflections.
- **Dark and Light Modes:** Includes a switch between dark and light themes for a personalized user experience.

## Project Structure

The project is organized into the following directories:

- `pomodoro/`: Contains Django project settings and configurations.
- `journal/`: The Django app for the journal.
- `focus_timer/`: The django app for the pomodoro timer.
- `static/`: Houses static files such as CSS, music, and images.

## Application Installation
To run this project on your local system, follow these steps:

1. Clone the repository from GitHub:
   ```bash
   https://github.com/nokuthabam/pomdoro_app.git

2. Install project dependencies:
   - ```pip install -r requirements.txt```

3. Installing Django and creating a virtual environment:
   - ```mkvirtualenv my_django```
   - ```workon my_django```
   - ```pip install django```


3. Navigate to the project directory:
   - ```cd pomdoro_app```

3. Apply database migrations:
   - ```python manage.py migrate```

4. Create a superuser to manage the Django admin panel:
   - ```python manage.py createsuperuser```

5. Start the development server:
   - ```python manage.py runserver```

6. Access the website at http://127.0.0.1:8000/

## Usage
    - Visit http://127.0.0.1:8000/ to access the login page
   - Click register to create your account and access the journal and focus timer.


## Continuous Integration: CircleCI Badge
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/nokuthabam/pomdoro_app/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/nokuthabam/pomdoro_app/tree/main)

### Code Coverage: CodeCov Badge
[![codecov](https://codecov.io/gh/nokuthabam/pomdoro_app/branch/main/graph/badge.svg?token=YQJ2UTPIY7)](https://codecov.io/gh/nokuthabam/pomdoro_app)

## Project Author
Nokuthaba Moyo

## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/nokuthabam/pomdoro_app/blob/main/LICENSE) for more information.
