from .models import Chat
from ariadne import convert_kwargs_to_snake_case


def resolve_chats(obj, info):
    try:
        chats = [chat.to_dict() for chat in Chat.query.all()]
        payload = {
            "success": True,
            "chats": chats
        }
    except Exception as Error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_chat(obj, info, chat_id):
    try:
        chat = Chat.query.get(chat_id)
        payload = {
            "success": True,
            "chat": chat.to_dict()
        }

    except AttributeError:  # chat not found
        payload = {
            "success": False,
            "errors": [f"Chat matching id {chat_id} not found"]
        }

    return payload
