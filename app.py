# app.py
from flask import Flask, request, render_template
from lexer import lexical_analysis
from parserA import syntactic_analysis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = []
    syntax_result = ''
    if request.method == 'POST':
        code = request.form['code']
        tokens = lexical_analysis(code)
        syntax_result = syntactic_analysis(tokens)
    return render_template('index.html', tokens=tokens, syntax_result=syntax_result)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
