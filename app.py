from flask import Flask, render_template, request
from patent_extraction import patentExtractiion
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('patent_search.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        firstName = request.form['firstName']
        secondName = request.form['secondName']
        result = patentExtractiion(firstName , secondName)
        return render_template('patent_search.html', success=result)

if __name__ == ' __main__':
    app.debug = True
    app.run()