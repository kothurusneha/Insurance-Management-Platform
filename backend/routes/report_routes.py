from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from models.customer import Customer
from models.policy import Policy
from models.claim import Claim
from models.payment import Payment

report_bp = Blueprint('report', __name__)

@report_bp.route('/api/reports/dashboard', methods=['GET'])
@jwt_required()
def dashboard():

    total_customers = Customer.query.count()
    total_policies = Policy.query.count()
    total_claims = Claim.query.count()
    total_payments = Payment.query.count()

    return jsonify({
        "total_customers": total_customers,
        "total_policies": total_policies,
        "total_claims": total_claims,
        "total_payments": total_payments
    }), 200