from flask import Flask, jsonify, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)

@app.route("/students")
def get_students():
    students = db.get_all_students()
    return jsonify(students), 200


@app.route("/students", methods=["POST"])
def create_student():
    student_data = request.json

    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark", 0)

    if not name or not course:
        return jsonify({"error": "name and course are required"}), 404

    student = db.insert_student(name, course, mark)
    return jsonify(student), 200


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student_data = request.json

    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark")

    student = db.update_student(student_id, name, course, mark)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    result = db.delete_student(student_id)
    if result is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(result), 200


@app.route("/stats")
def get_stats():
    students = db.get_all_students()

    if not students:
        return jsonify({"count": 0, "average": None, "min": None, "max": None}), 200

    marks = [s["mark"] for s in students if s["mark"] is not None]
    return jsonify({
        "count": len(students),
        "average": sum(marks) / len(marks),
        "min": min(marks),
        "max": max(marks)
    }), 200


@app.route("/")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)