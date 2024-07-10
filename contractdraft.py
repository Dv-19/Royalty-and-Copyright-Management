from flask import Flask, render_template, send_file
from jinja2 import Template
import datetime
import mysql.connector

app = Flask(__name__)

@app.route('/draft_contract/<int:author_id>/<int:publisher_id>')
def draft_contract(author_id, publisher_id):
    try:
        # Connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="bharathi",
            password="idlydosa",
            database="your_database" #replace
        )
        cursor = db.cursor()

        # Retrieve author and publisher details
        cursor.execute("SELECT * FROM Author WHERE AuthorID = %s", (author_id,))
        author_details = cursor.fetchone()

        cursor.execute("SELECT * FROM Publisher WHERE PublisherID = %s", (publisher_id,))
        publisher_details = cursor.fetchone()

# Define contract template
        contract_template = """
        Author-Publisher Contract

        This agreement is entered into on {{ date }} between {{ author_name }} (hereinafter referred to as the Author) and {{ publisher_name }} (hereinafter referred to as the Publisher).

        1. Rights Granted:
        The Author hereby grants the Publisher the exclusive right to publish, distribute, and sell the work titled "{{ work_title }}" in {{ territory }} for a period of {{ contract_duration }} years from the date of signing this agreement.

        2. Royalties:
   The Publisher agrees to pay the Author a royalty of {{ royalty_percentage }}% of net revenues generated from the sale of the work.

    3. Term:
   This agreement shall commence on {{ start_date }} and shall remain in effect until {{ end_date }}.

        4. Termination:
   Either party may terminate this agreement upon written notice to the other party in the event of a material breach.

    5. Governing Law:
   This agreement shall be governed by the laws of {{ governing_country }}.

IN WITNESS WHEREOF, the parties hereto have executed this agreement as of the date first above written.

{{ author_signature }}           {{ publisher_signature }}
Author                          Publisher
"""


        contract_content = Template(contract_template).render(
            date=datetime.date.today().strftime("%B %d, %Y"),
            author_name=author_details[1],
            publisher_name=publisher_details[1],
            work_title="Your Work Title",
            territory="Your Territory",
            contract_duration="Your Contract Duration",
            royalty_percentage="Your Royalty Percentage",
            start_date="Your Contract Start Date",
            end_date="Your Contract End Date",
            governing_country="Your Governing Country",
            author_signature="",
            publisher_signature=""
        )

        # Save the drafted contract as a PDF file
        contract_filename = "author_publisher_contract.pdf"
        with open(contract_filename, "w") as file:
            file.write(contract_content)

        # Close database connection
        cursor.close()
        db.close()

        # Return the drafted contract file as a response
        return send_file(contract_filename, as_attachment=True)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)