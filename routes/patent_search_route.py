from flask import Flask, render_template, request, Blueprint

from helpers.patent_extraction import patentExtraction

app = Flask(__name__)

patent_search_endpoint = Blueprint("patent_search_service", __name__)
patent_search_send_endpoint = Blueprint("patent_search_send_service", __name__)
endpoint = "/"
send_endpoint = "/send"


@patent_search_endpoint.route(endpoint, methods=['GET', 'POST'])
def main():
    return render_template('patent_search.html')


@patent_search_send_endpoint.route(send_endpoint, methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        firstName = request.form['firstName']
        secondName = request.form['secondName']
        result = patentExtraction(firstName, secondName)
        return render_template('patent_search.html', success=result)
