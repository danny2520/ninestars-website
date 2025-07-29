from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from ninestars_website import db

class ContactMessage(db.Model):
    __tablename__ = 'contact_message'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
