from project.db import DATABASE

class Chat(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    title = DATABASE.Column(DATABASE.String(50), nullable=False)
    word = DATABASE.Column(DATABASE.String(10), nullable=False)
    last_message = DATABASE.Column(DATABASE.String(500), nullable=False)

    owner_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"), nullable=False)
    users = DATABASE.relationship(
        "User",
        secondary= "user_chat_link",
        back_populates= "chats"
    )

class UserChatLink(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)    
    chat_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("chat.id"), nullable=False)
    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"), nullable=False)


