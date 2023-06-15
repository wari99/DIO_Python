from flask import Flask, jsonify
import pandas as pd

#pip install flask
#pip install pandas
#pip install openpyxl

app = Flask(__name__)

universidades = pd.read_excel('universidades.xlsx')
dados = universidades.to_json(orient='records')
@app.route('/')

def home():
    return '''<h1>Universidades.xlsx</h1>
            <h3>Para visualizar adicione "/input" no final dessa url</h3>'''

@app.route('/input/')

def input():
    return jsonify(dados)

app.run()
