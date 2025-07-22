from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

@app.route('/')
def home():
    return jsonify({'message': 'AI Social Media Caption Generator Backend is running'})

if __name__ == '__main__':
    app.run(debug=True)
