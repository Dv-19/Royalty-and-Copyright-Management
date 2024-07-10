from flask import Flask, render_template
from viewroyalty import get_royalty_transactions

app = Flask(__name__)

@app.route('/view-royalty')
def view_royalty():
    royalty_transactions = get_royalty_transactions()  # Replace with your function to get royalty transactions
    return render_template('view_royalty.html', royalty_transactions=royalty_transactions)

if __name__ == '__main__':
    app.run(debug=True)
