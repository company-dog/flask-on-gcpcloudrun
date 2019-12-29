import os
from flask import Flask, request
from flask_restful import Api, reqparse


from resources.todo import Todo, Todos

# Initialize Flask app
app = Flask(__name__)
api = Api(app)


def main():
    port = int(os.environ.get('PORT', 8080))
    api.add_resource(Todos, '/todos')
    api.add_resource(Todo, '/todo/<string:todo_id>')
    app.run(port=port, host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
