from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api/v1')

# Health check
@api.route('/health')
def health():
    return jsonify({"status": "ok"})

# In-memory list of todos (used for Week 01 testing)
todos = [
    {
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }
]

# GET /todos - list all todos
@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# GET /todos/<id> - get specific todo
@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

# POST /todos - create a new todo
@api.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(new_todo), 201

# PUT /todos/<id> - update a todo
@api.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    updated_data = request.get_json()
    for todo in todos:
        if todo['id'] == todo_id:
            todo.update(updated_data)
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

# DELETE /todos/<id> - delete a todo
@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return jsonify({"message": "Todo deleted"})
    return jsonify({"error": "Todo not found"}), 404
