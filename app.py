import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
    else:
        # Default keyword
        keyword = "SSHOMP keyword here"

    api_url = f"https://marketplace-api.sshopencloud.eu/api/concept-search?q={keyword}&f=f.candidate%3Dfalse&advanced=true&order=score"
    
    response = requests.get(api_url)
    data = response.json()

    # Filter out items with vocabulary code 'sshoc-keyword'
    filtered_concepts = [i for i in data["concepts"] if i['vocabulary']['code'] != 'sshoc-keyword']

    # Render the HTML template with the filtered concepts
    return render_template('index.html', filtered_concepts=filtered_concepts)

if __name__ == '__main__':
    app.run(debug=True)

