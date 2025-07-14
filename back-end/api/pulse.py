from flask import Blueprint, request, jsonify
from supabase_db.supabase_client import supabase

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/get_tasks", methods=["GET"])
def get_tasks():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    tasks = supabase.table("tasks").select("*").eq("user_id", user_id).execute()
    return jsonify(tasks.data), 200


@tasks_bp.route("/create_task", methods=["POST"])
def create_task():
    data = request.json
    res = supabase.table("tasks").insert(data).execute()
    return jsonify(res.data[0]), 201

@tasks_bp.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    res = supabase.table("tasks").update(data).eq("id", task_id).execute()
    return jsonify(res.data[0])

@tasks_bp.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    supabase.table("tasks").delete().eq("id", task_id).execute()
    return jsonify({"message": "Task deleted"})
