from flask import Blueprint, jsonify, request

# Create a Blueprint for the routes
main_bp = Blueprint("main", __name__)

@main_bp.route("/api/complete", methods=["POST"])
def complete():
    str = request.json
    # MACHINE LEARNING SHIT --> complete the sentence that was sent
    
    return jsonify({"completed_text": ""})

# Example POST route
@main_bp.route("/api/data", methods=["POST"])
def receive_data():
    data = request.json  # Get JSON data from frontend
    return jsonify({"received": data}), 201  # Return response with status code 201
