from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Setup database connection
db = SQLAlchemy()
migrate = Migrate()
