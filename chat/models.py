from project.db import DATABASE
from datetime import datetime

class Chat(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    title = DATABASE.Column(DATABASE.String(50), nullable=False)
    word = DATABASE.Column(DATABASE.String(10), nullable=False, unique=True)
    last_message = DATABASE.Column(DATABASE.String(500), nullable=False, default="")
    created_at = DATABASE.Column(DATABASE.DateTime, nullable=False, default=datetime.utcnow)

    owner_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"), nullable=False, unique=True)
    users = DATABASE.relationship(
        "User",
        secondary= "user_chat_link",
        back_populates= "chats"
    )
    messages = DATABASE.relationship(
        "Message",
        backref="chat",
        cascade="all, delete-orphan",
        order_by="Message.created_at"
    )

class UserChatLink(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)    
    chat_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("chat.id"), nullable=False)
    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"), nullable=False)


class Message(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    text = DATABASE.Column(DATABASE.String(500), nullable=False)
    created_at = DATABASE.Column(DATABASE.DateTime, nullable=False, default=datetime.utcnow)

    chat_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("chat.id"), nullable=False)
    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"), nullable=False)
    user = DATABASE.relationship("User")


