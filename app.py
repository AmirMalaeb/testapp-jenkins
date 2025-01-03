from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple in-memory storage for tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        tasks.append(task)
        return jsonify({"message": "Task added successfully"}), 201
    return jsonify({"error": "Invalid task"}), 400

if __name__ == '__main__':
    app.run(debug=True)