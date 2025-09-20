from flask import Flask, request, render_template, redirect, url_for
import requests
from proxy_handler import fetch_url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy', methods=['POST'])
def proxy():
    url = request.form['url']
    if not url:
        return redirect(url_for('index'))
    
    try:
        response = fetch_url(url)
        return response
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
