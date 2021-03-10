from flask import Flask
import os

app = Flask(__name__)


def get_base_path():
    return os.path.dirname(os.path.realpath(__file__))

