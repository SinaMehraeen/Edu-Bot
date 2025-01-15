import time
from datetime import datetime
import json

# Placeholder for the Llama2 model inference function
# Replace this function with your actual call to the Llama2 model.
def llama2_model_response(user_input):
    """
    Simulates a response from the Llama2 model.
    Replace this with your actual Llama2 model's API or inference logic.
    """
    responses = {
        "What is 2 + 2?": "4",  # Example of a correct response
        "Tell me about gravity": "Gravity is the force that attracts objects toward the center of the Earth.",
    }
    return responses.get(user_input, "I'm not sure, can you clarify?")  # Default response for unknown inputs

# Class to track and calculate metrics for the chatbot interaction
class ChatMetrics:
    def __init__(self):
        """
        Initializes the metrics tracker with default values.
        """
        self.start_time = None  # Time when the session starts
        self.end_time = None  # Time when the session ends
        self.turn_count = 0  # Number of user-bot interaction turns
        self.interactions = []  # List to log each interaction
        self.correct_responses = 0  # Tracks the number of correct answers during knowledge checks
        self.knowledge_check = []  # List to log knowledge check questions and results

    def start_session(self):
        """
        Records the start time of the session.
        """
        self.start_time = time.time()

    def end_session(self):
        """
        Records the end time of the session.
        """
        self.end_time = time.time()

    def record_turn(self, user_input, bot_response):
        """
        Logs a single user-bot interaction.
        """
        self.turn_count += 1  # Increment the turn count
        self.interactions.append({
            "timestamp": datetime.now().isoformat(),  # Record the current time
            "user_input": user_input,  # Save the user's input
            "bot_response": bot_response  # Save the chatbot's response
        })

    def record_knowledge_check(self, question, user_answer, correct_answer):
        """
        Logs and evaluates a knowledge check question.
        """
        is_correct = user_answer == correct_answer  # Check if the user's answer matches the correct answer
        self.knowledge_check.append({
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct
        })
        if is_correct:  # If correct, increment the correct responses counter
            self.correct_responses += 1

    def calculate_metrics(self):
        """
        Calculates and returns the session metrics:
        - Session length in seconds
        - Turn count
        - Drop-off rate
        - Knowledge gain
        """
        session_length = self.end_time - self.start_time  # Total session time in seconds
        drop_off_rate = 1 - (self.turn_count / len(self.interactions) if self.interactions else 1)  # Proportion of unfinished interactions
        knowledge_gain = self.correct_responses / len(self.knowledge_check) if self.knowledge_check else 0  # Proportion of correct answers
        return {
            "session_length_seconds": session_length,
            "turn_count": self.turn_count,
            "drop_off_rate": drop_off_rate,
            "knowledge_gain": knowledge_gain,
            "interactions": self.interactions  # Full log of interactions
        }

# Function to simulate a chatbot session
def chat_with_model():
    """
    Runs a chatbot session, records metrics, and handles user interaction.
    """
    metrics = ChatMetrics()  # Initialize metrics tracker
    metrics.start_session()  # Start the session timer

    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")  # Get user input
        if user_input.lower() in ["exit", "quit"]:  # End session if the user types "exit" or "quit"
            print("Chatbot: Goodbye!")
            break

        bot_response = llama2_model_response(user_input)  # Get response from the model
        print(f"Chatbot: {bot_response}")  # Display the chatbot's response
        metrics.record_turn(user_input, bot_response)  # Log the interaction

        # Simulated knowledge check example (can be replaced with actual logic)
        if user_input == "What is 2 + 2?":
            user_answer = input("You (Answer the quiz): ")  # Get the user's answer to the quiz
            metrics.record_knowledge_check("What is 2 + 2?", user_answer, "4")  # Evaluate the user's answer

    metrics.end_session()  # End the session timer
    return metrics.calculate_metrics()  # Calculate and return session metrics

# Main program to run the chatbot and save metrics
if __name__ == "__main__":
    metrics_data = chat_with_model()  # Start the chatbot session

    # Save session metrics to a JSON file for analysis
    with open("chat_metrics.json", "w") as f:
        json.dump(metrics_data, f, indent=4)

    # Print session metrics for the user
    print("\nSession Metrics:")
    print(json.dumps(metrics_data, indent=4))
