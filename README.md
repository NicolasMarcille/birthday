# Birthday Game Application

A simple web application built with FastAPI and React that allows users to enter a "Super Card Key" and see if they've won a prize.

## Features

- FastAPI backend with RESTful API
- React frontend with modern UI
- Simple game logic that checks if the entered key matches a secret value
- Responsive design that works on mobile and desktop

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

### FastAPI Version

To run the FastAPI version of the application:

```bash
python app.py
```

This will start the server at http://localhost:8000

### Gradio Version (Alternative)

This repository also includes a Gradio version of the application:

```bash
python gradio_app.py
```

This will start the Gradio interface at http://localhost:7860

## How to Play

1. Open the application in your web browser
2. Enter the secret key "coop_supercard_rules" in the input field
3. Click "Submit" to see if you've won
4. Try different keys to see different results

## Project Structure

- `app.py` - FastAPI application
- `gradio_app.py` - Alternative Gradio implementation
- `static/` - Frontend files
  - `index.html` - HTML template
  - `app.js` - React application
  - `styles.css` - CSS styles

## Technologies Used

- FastAPI - Backend framework
- React - Frontend library
- Pydantic - Data validation
- Uvicorn - ASGI server
- Gradio - Alternative UI framework
