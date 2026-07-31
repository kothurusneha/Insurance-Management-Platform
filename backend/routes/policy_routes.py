from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from extensions import db
from models.policy import Policy

policy_bp = Blueprint('policy', __name__)

# Create Policy
@policy_bp.route('/api/policies', methods=['POST'])
@jwt_required()
def create_policy():

    data = request.get_json()

    existing_policy = Policy.query.filter_by(
        policy_number=data['policy_number']
    ).first()

    if existing_policy:
        return jsonify({
            "message": "Policy already exists"
        }), 400

    policy = Policy(
        customer_id=data['customer_id'],
        policy_type=data['policy_type'],
        policy_number=data['policy_number'],
        premium_amount=data['premium_amount'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        status="active"
    )

    db.session.add(policy)
    db.session.commit()

    return jsonify({
        "message": "Policy created successfully",
        "policy": policy.to_dict()
    }), 201


# Get Policies
@policy_bp.route('/api/policies', methods=['GET'])
@jwt_required()
def get_policies():

    policies = Policy.query.all()

    return jsonify([
        policy.to_dict()
        for policy in policies
    ]), 200