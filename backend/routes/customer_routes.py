from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from extensions import db
from models.customer import Customer

customer_bp = Blueprint('customer', __name__)

# Create Customer
@customer_bp.route('/api/customers', methods=['POST'])
@jwt_required()
def create_customer():

    data = request.get_json()

    existing_customer = Customer.query.filter_by(email=data['email']).first()

    if existing_customer:
        return jsonify({
            "message": "Customer already exists"
        }), 400

    customer = Customer(
        name=data['name'],
        dob=data['dob'],
        phone=data['phone'],
        address=data['address'],
        email=data['email']
    )

    db.session.add(customer)
    db.session.commit()

    return jsonify({
        "message": "Customer created successfully",
        "customer": customer.to_dict()
    }), 201


# Get All Customers
@customer_bp.route('/api/customers', methods=['GET'])
@jwt_required()
def get_customers():

    customers = Customer.query.all()

    return jsonify([
        customer.to_dict()
        for customer in customers
    ]), 200