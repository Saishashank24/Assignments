# -*- coding: utf-8 -*-
"""Day-44

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18tmxOTOclj398oyqUqoXC_1hHhWjZ5Y0
"""

def simple_chatbot():
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "hello":
            print("Bot: Hi! How can I help you?")
        elif user_input.lower() == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: I'm sorry, I don't understand.")

# Run the chatbot
simple_chatbot()