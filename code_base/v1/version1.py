# Import the random module: This module will help us randomly select a response from our list
import random
# Define the responses: These are the possible answers the Magic 8-Ball can give
def magic_8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
# Main function magic_8_ball():
# - use a while loop to continuously prompt the user for a question
# - the user can type a question or 'quit' to exit the loop
# - a random response is selected using random.choice(responses) and printed out
    while True:
        question = input("Ask the Magic 8-Ball a question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        response = random.choice(responses)
        print("Magic 8-Ball says: " + response)
# Run the function: This ensures that the magic_8_ball function runs when the script is executed
if __name__ == "__main__":
    magic_8_ball()