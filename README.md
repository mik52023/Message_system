"Message System API" 

This is for herolo assignment


Create Message:

Method: POST

Description: send Parameters to create message.

Parameters: "sender":string, "reciever":string, "subject":string, "content":text area

Link :https://message-system.herokuapp.com/Messaging_system/create_message/

response example:

{
"info": "message was sent"
}
-----------------------
Read Message:

Method: GET

Description: send user and id,receive message if found and user is reciever/sender   

Parameters: “id”:integer ,"user":string

Link :https://message-system.herokuapp.com/Messaging_system/read_message

response example:

{
    "data": {
        "sender": "test-user3",
        "reciever": "test-user2",
        "subject": "im testing this system",
        "content": "this is a test.\nthis is a test.\nthis is a test.this is a test.\nthis is a test.\nthis is a test.\nthis is a test.this is a test.this is a test.\nthis is a test.this is a test.this is a test.\nthis is a test.",
        "read": true
    }
}

------------------------------
Get Messages By User:

Method: GET

Description: send user,recieve all messages address to the user

Parameters: "user":string

Link :https://message-system.herokuapp.com/Messaging_system/get_messages_by_user/

response example:

{
    "data": [
        {
            "sender": "test-user3",
            "reciever": "test-user2",
            "subject": "im testing this system",
            "content": "this is a test.\nthis is a test.\nthis is a test.this is a test.\nthis is a test.\nthis is a test.\nthis is a test.this is a test.this is a test.\nthis is a test.this is a test.this is a test.\nthis is a test.",
            "read": false
        },
        {
            "sender": "test-user3",
            "reciever": "test-user2",
            "subject": "im testing this system",
            "content": "this is a test.\nthis is a test.\nthis is a test.this is a test.\nthis is a test.\nthis is a test.\nthis is a test.this is a test.this is a test.\nthis is a test.this is a test.this is a test.\nthis is a test.",
            "read": true
        }
    ]
}
---------------------------
Get Unread Messages By User:

Method: GET

Description:send user, recieve all unread messages address to the user

Parameters: "user":string

Link :https://message-system.herokuapp.com/Messaging_system/get_unread_messages_by_user/

response example:

{
    "data": [
        {
            "sender": "test-user3",
            "reciever": "test-user2",
            "subject": "im testing this system",
            "content": "this is a test.\nthis is a test.\nthis is a test.this is a test.\nthis is a test.\nthis is a test.\nthis is a test.this is a test.this is a test.\nthis is a test.this is a test.this is a test.\nthis is a test.",
            "read": false
        }
    ]
}
-----------------------
Delete Message

Method GET

Description:recieve id and user,Delete Message if user is sender or reciever

Parameters: "id":integer ,"user":string

Link :https://message-system.herokuapp.com/Messaging_system/

response example:
{
    "info": "message was deleted"
}





