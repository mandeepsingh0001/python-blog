# Flask Blog Application

This is a simple blog application built using Flask and SQLite. It allows users to create, view, and delete blog posts.

## Features
- View all blog posts
- Add new blog posts
- Delete blog posts

## Installation

1. Clone this repository:
   ```bash
   git clone <URL>
   cd flask-blog
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open the application in your browser:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure
```
flask-blog/
│── templates/
│   ├── index.html  # Main page to display blog posts
│   ├── add.html    # Form page to add new blog posts
│── app.py          # Main Flask application
│── requirements.txt # Dependencies
│── README.md       # Project documentation
```

## Dependencies
- Flask
- SQLite3