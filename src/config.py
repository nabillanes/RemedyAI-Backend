import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database settings
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./quiz_app.db")

# CORS settings
ALLOWED_ORIGINS = ["*"]  # Configure as needed for production
