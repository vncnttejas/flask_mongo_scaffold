from flask import Blueprint

app = Blueprint('famers', __name__)


@app.route('/', methods=['POST'])
def create_famer():
    return 'creating famer'


@app.route('/', methods=['GET'])
def get_famers(id):
    return 'fetching all famers'


@app.route('/<id>', methods=['GET'])
def get_famer(id):
    return f'getting famer by id: {id}'


@app.route('/<id>', methods=['UPDATE'])
def update_famer(id):
    return f'updating famer by id: {id}'


@app.route('/<id>', methods=['DELETE'])
def delete_famer(id):
    return f'deleting famer by id: {id}'
