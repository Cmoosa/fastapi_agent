import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from auth.auth_database import engine, Base
from auth import models

Base.metadata.create_all(bind=engine)