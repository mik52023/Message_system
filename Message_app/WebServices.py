from .models import Message

class UserNotAuthorized(Exception):
    """Raised when user isnt owner or reciever"""
    pass



"recieve message params and return message instance once created"
def create_message(sender,reciever,subject,content):

    new_message=Message(sender=sender,reciever=reciever,subject=subject,content=content)
    new_message.full_clean()
    new_message.save()
    return new_message

"recieve user and message and if user autherized message is deleted"
def delete_message(user,message):
    if((message.reciever==user)or(message.sender==user)):
        message.delete()
    else:
     raise UserNotAuthorized('user not allowed')

"recieve message_id and return message instance"
def get_message(id):
    message = Message.objects.get(id=id)
    return message

"recieve message_id and return message instance and change unread message stats to read"
def read_message(id,user):
    message=get_message(id)
    if((message.sender!=user) and (message.reciever!=user)):
       raise UserNotAuthorized('user not allowed')
    if(not message.read):
        message.read=True
        message.save()

    return message

"recieve user and return all messages that the user recieved"
def get_messages_by_user(user):

    messages=Message.objects.filter(reciever=user)
    return messages

"recieve user and return all unread messages that the user recieved"
def get_unread_messages_by_user(user):
    messages = Message.objects.filter(reciever=user,read=False)
    return messages

