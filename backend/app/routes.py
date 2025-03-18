from flask import Blueprint, jsonify, request

# Create a Blueprint for the routes
main_bp = Blueprint("main", __name__)

@main_bp.route("/api/complete", methods=["POST"])
def complete():
    str = request.json
    # MACHINE LEARNING SHIT --> complete the sentence that was sent
    
    return jsonify({"completed_text": str})