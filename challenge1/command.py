

def hello(message):
    # When this command is used, everything after the word "hello" in the message will be sent to this function.
    # Example: "@Jam hello Ronan" -> this function receivces "Ronan" as the messsage.
    #
    # Your job is to process the message so that this function returns the correct outputs for challenge 1.
    # (for now, it just echoes back the same message)

    # Challenge 1.4
    if message == "Shane":
        message = "Everybody loves Shane!"
    elif message == "Luke":
        message = "Everybody likes Luke!"
    elif message == "Jamie":
        message = "Everybody loves Jamie"
    elif message == "Andrew":
        message = "Eveyobody loves Andrew"

    # Challenge 1.3 & 1.2
    if message == "Chuck Robbins":
        message = "Hello Cisco's favourite CEO Chuck Robbins"
    elif len(message) > 0:
        message = "Hello, " + message
    
    # # Challenge 1.1
    elif len(message) == 0:
        message = "Hello, Cisco!"

    return message
