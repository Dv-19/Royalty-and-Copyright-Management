from flask import Flask, render_template
from contractdraft import generate_contract_draft

app = Flask(__name__)

@app.route('/contract-draft')
def contract_draft():
    contract_draft_content = generate_contract_draft()  # Replace with your function to generate contract draft
    return render_template('contract_draft.html', contract_draft=contract_draft_content)

if __name__ == '__main__':
    app.run(debug=True)
