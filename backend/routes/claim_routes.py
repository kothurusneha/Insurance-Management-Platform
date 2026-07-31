from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from extensions import db
from models.claim import Claim

claim_bp = Blueprint('claim', __name__)

# Create Claim
@claim_bp.route('/api/claims', methods=['POST'])
@jwt_required()
def create_claim():

    data = request.get_json()

    claim = Claim(
        policy_id=data['policy_id'],
        claim_amount=data['claim_amount'],
        claim_reason=data['claim_reason'],
        claim_date=data['claim_date'],
        claim_status=data.get('claim_status', 'Pending')
    )

    db.session.add(claim)
    db.session.commit()

    return jsonify({
        "message": "Claim submitted successfully",
        "claim": claim.to_dict()
    }), 201


# Get All Claims
@claim_bp.route('/api/claims', methods=['GET'])
@jwt_required()
def get_claims():

    claims = Claim.query.all()

    return jsonify([
        claim.to_dict()
        for claim in claims
    ]), 200