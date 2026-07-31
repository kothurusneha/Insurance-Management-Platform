from extensions import db

class Customer(db.Model):

    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    dob = db.Column(db.String(20))

    phone = db.Column(db.String(20))

    address = db.Column(db.Text)

    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "dob": self.dob,
            "phone": self.phone,
            "address": self.address,
            "email": self.email
        }