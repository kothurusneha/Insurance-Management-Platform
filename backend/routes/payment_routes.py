from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from extensions import db
from models.payment import Payment

payment_bp = Blueprint('payment', __name__)

# Create Payment
@payment_bp.route('/api/payments', methods=['POST'])
@jwt_required()
def create_payment():

    data = request.get_json()

    payment = Payment(
        policy_id=data['policy_id'],
        payment_date=data['payment_date'],
        amount=data['amount'],
        payment_status=data.get('payment_status', 'Paid')
    )

    db.session.add(payment)
    db.session.commit()

    return jsonify({
        "message": "Payment added successfully",
        "payment": payment.to_dict()
    }), 201


# Get All Payments
@payment_bp.route('/api/payments', methods=['GET'])
@jwt_required()
def get_payments():

    payments = Payment.query.all()

    return jsonify([
        payment.to_dict()
        for payment in payments
    ]), 200