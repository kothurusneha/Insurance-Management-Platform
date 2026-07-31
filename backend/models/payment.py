from extensions import db

class Payment(db.Model):

    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    policy_id = db.Column(db.Integer, nullable=False)

    payment_date = db.Column(db.String(20))

    amount = db.Column(db.Float)

    payment_status = db.Column(db.String(20), default="Paid")

    def to_dict(self):
        return {
            "id": self.id,
            "policy_id": self.policy_id,
            "payment_date": self.payment_date,
            "amount": self.amount,
            "payment_status": self.payment_status
        }