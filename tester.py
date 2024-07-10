from flask import Flask, render_template, jsonify
import mysql.connector
import sql_connect as connect

app = Flask(__name__)

# Function to create an author
def create_author(name, nationality):
    try:
        sql = "INSERT INTO Author (Name, Nationality) VALUES (%s, %s)"
        values = (name, nationality)
        connect.cursor.execute(sql, values)
        connect.db_connection.commit()
        return jsonify({"message": "Author created successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to read authors
def read_authors():
    try:
        connect.cursor.execute("SELECT * FROM Author")
        authors = connect.cursor.fetchall()
        return jsonify(authors), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define similar functions for other tables (e.g., publishers, publications, copyright agreements, etc.)

@app.route('/create_author/<name>/<nationality>')
def create_author_route(name, nationality):
    return create_author(name, nationality)

@app.route('/read_authors')
def read_authors_route():
    return read_authors()

if __name__ == "__main__":
    app.run(debug=True)
