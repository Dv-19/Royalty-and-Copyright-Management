from flask import Flask, request, jsonify
import mysql.connector
import sql_connect as connect

app = Flask(__name__)

# Function to print royalty transactions by author
def print_royalty_transactions_by_author(author_id):
    try:
        # Retrieve royalty transactions associated with the author
        connect.cursor.execute("SELECT * FROM RoyaltyPayment WHERE AgreementID IN (SELECT AgreementID FROM CopyrightAgreement WHERE CreatorID = %s)", (author_id,))
        transactions = connect.cursor.fetchall()

        if transactions:
            return jsonify(transactions), 200
        else:
            return jsonify({"message": "No royalty transactions found for the author."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/view_royalty_transactions', methods=['GET'])
def view_royalty_transactions():
    author_id = request.args.get('author_id')
    if author_id is None:
        return jsonify({"error": "Author ID is required."}), 400
    else:
        return print_royalty_transactions_by_author(author_id)

if __name__ == "__main__":
    app.run(debug=True)
