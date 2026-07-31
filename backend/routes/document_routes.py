from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from models.document import Document

document_bp = Blueprint('document', __name__)

# Upload Document
@document_bp.route('/api/documents', methods=['POST'])
@jwt_required()
def upload_document():

    data = request.get_json()

    document = Document(
        customer_id=data['customer_id'],
        document_name=data['document_name'],
        file_path=data['file_path'],
        upload_date=data['upload_date']
    )

    db.session.add(document)
    db.session.commit()

    return jsonify({
        "message": "Document uploaded successfully",
        "document": document.to_dict()
    }), 201


# Get Documents
@document_bp.route('/api/documents', methods=['GET'])
@jwt_required()
def get_documents():

    documents = Document.query.all()

    return jsonify([
        document.to_dict()
        for document in documents
    ]), 200