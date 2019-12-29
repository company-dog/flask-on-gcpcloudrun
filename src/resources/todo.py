import uuid
from flask_restful import Resource, reqparse, request
from store import db

todo_ref = db.collection('todos')


class Todo(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='This field cannot be left blank!'
                        )
    parser.add_argument('completed',
                        type=bool,
                        required=True,
                        help='This field cannot be left blank!'
                        )

    @classmethod
    def find_by_id(cls, todo_id):
        todo = todo_ref.document(todo_id).get()
        return todo.to_dict()

    def get(self, todo_id):
        try:
            todo = self.find_by_id(todo_id)
            if todo is None:
                return {'msg': 'todo not found'}, 404
            else:
                return {'todo': todo}, 200
        except Exception as e:
            print(e)
            return {'msg': 'Internal Server Error'}

    def put(self, todo_id):
        try:
            if self.find_by_id(todo_id) is None:
                return {'msg': 'todo not found'}, 404
            else:
                data = Todo.parser.parse_args()
                todo_ref.document(todo_id).update(data)
                return {'msg': f'Update successful'}, 200
        except Exception as e:
            print(e)
            return {'msg': 'Internal Server Error'}

    def delete(self, todo_id):
        try:
            todo_ref.document(todo_id).delete()
            return {'msg': f'Delete Successful'}
        except Exception as e:
            print(e)
            return {'msg': 'Internal Server Error'}


class Todos(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='This field cannot be left blank!'
                        )

    def post(self):
        try:
            data = Todos.parser.parse_args()
            data['completed'] = False
            todo_id = str(uuid.uuid4())
            todo_ref.document(todo_id).set(data)
            return {'msg': 'todo created', 'todo_id': todo_id}, 201
        except Exception as e:
            print(e)
            return f"an error occured: {e}"
