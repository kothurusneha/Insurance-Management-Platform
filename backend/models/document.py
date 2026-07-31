from extensions import db

class Document(db.Model):

    __tablename__ = "documents"

    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, nullable=False)

    document_name = db.Column(db.String(100))

    file_path = db.Column(db.String(255))

    upload_date = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "document_name": self.document_name,
            "file_path": self.file_path,
            "upload_date": self.upload_date
        }