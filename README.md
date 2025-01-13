# Educational Chatbot Metrics Tracker

This repository contains a Python script designed to monitor and evaluate the engagement of an educational chatbot powered by the Llama2 model. The script tracks various interaction metrics to help analyze and improve chatbot performance, specifically in an educational context.
Features

This project tracks the following metrics during a chatbot session:

    Session Length: Measures the total time spent interacting with the chatbot.
    Turn Count: Tracks the total number of exchanges (user input and bot response).
    Drop-Off Rate: Identifies the proportion of unfinished interactions.
    Knowledge Gain: Assesses how much the user learns during the session using quizzes.
    Accuracy of Responses: Compares the chatbot's answers to predefined correct responses.

The session data is logged in a JSON file for further analysis.

Requirements

This script requires Python 3.7 or higher. No additional libraries are needed beyond Python's standard library.



Customization
Replace Llama2 Model Integration

The script uses a placeholder function (llama2_model_response) to simulate Llama2 model responses. Replace this function with your actual API call or inference logic.
Adding Knowledge Checks

To add more knowledge checks:

    Modify the logic in the chat_with_model function.
    Define questions, expected answers, and user input prompts.



