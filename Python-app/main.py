from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

def init_db():
    try:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception: {e}")

@app.route('/')
def index():
    try:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts")
            posts = cursor.fetchall()
        return render_template("index.html", posts=posts)
    except sqlite3.Error as e:
        flash("Database error: Unable to fetch posts.", "danger")
        return render_template("index.html", posts=[])

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash("Title and content cannot be empty.", "warning")
            return redirect(url_for('add_post'))
        
        try:
            with sqlite3.connect("blog.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
                conn.commit()
            flash("Post added successfully!", "success")
            return redirect(url_for('index'))
        except sqlite3.Error as e:
            flash("Database error: Unable to add post.", "danger")
            return redirect(url_for('add_post'))
    
    return render_template("add.html")

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    try:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
            if cursor.rowcount == 0:
                flash("Post not found.", "warning")
            else:
                flash("Post deleted successfully!", "success")
            conn.commit()
    except sqlite3.Error as e:
        flash("Database error: Unable to delete post.", "danger")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)