from flask import Flask

from extensions import db, migrate, jwt

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sneha%40123@localhost/insurance_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'sneha_insurance_platform_super_secure_jwt_key_2026'

# Initialize Extensions
db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

# Import Models
import models.user
import models.customer
import models.policy
import models.payment
import models.claim
import models.document

# Import Routes
from routes.auth_routes import auth_bp
from routes.customer_routes import customer_bp
from routes.policy_routes import policy_bp
from routes.payment_routes import payment_bp
from routes.claim_routes import claim_bp
from routes.document_routes import document_bp
from routes.report_routes import report_bp

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(policy_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(claim_bp)
app.register_blueprint(document_bp)
app.register_blueprint(report_bp)

# Home Route
@app.route('/')
def home():
    return {
        "message": "Insurance Management Platform API is running"
    }

# Run Application
if __name__ == "__main__":
    app.run(debug=True)