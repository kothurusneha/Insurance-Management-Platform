from extensions import db

class Claim(db.Model):

    __tablename__ = "claims"

    id = db.Column(db.Integer, primary_key=True)

    policy_id = db.Column(db.Integer, nullable=False)

    claim_amount = db.Column(db.Float)

    claim_reason = db.Column(db.Text)

    claim_date = db.Column(db.String(20))

    claim_status = db.Column(db.String(20), default="Pending")

    def to_dict(self):
        return {
            "id": self.id,
            "policy_id": self.policy_id,
            "claim_amount": self.claim_amount,
            "claim_reason": self.claim_reason,
            "claim_date": self.claim_date,
            "claim_status": self.claim_status
        }