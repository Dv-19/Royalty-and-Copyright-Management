from flask import Flask, render_template, request
from tester import add_author_to_db

app = Flask(__name__)

@app.route('/add-author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        # Process form submission and add author to the database
        author_name = request.form['author_name']
        nationality = request.form['nationality']
        add_author_to_db(author_name, nationality)  # Replace with your function to add author to the database
    return render_template('add_author.html')

if __name__ == '__main__':
    app.run(debug=True)
