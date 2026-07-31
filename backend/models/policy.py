from extensions import db

class Policy(db.Model):

    __tablename__ = "policies"

    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, nullable=False)

    policy_type = db.Column(db.String(100))

    policy_number = db.Column(db.String(100), unique=True)

    premium_amount = db.Column(db.Float)

    start_date = db.Column(db.String(20))

    end_date = db.Column(db.String(20))

    status = db.Column(db.String(20), default="active")

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "policy_type": self.policy_type,
            "policy_number": self.policy_number,
            "premium_amount": self.premium_amount,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status
        }