# Educational Chatbot Metrics Tracker

This repository contains a Python script designed to monitor and evaluate the engagement of an educational chatbot powered by the **Llama2 model**. The script tracks various interaction metrics to help analyze and improve chatbot performance, specifically in an educational context.

## Features

This project tracks the following metrics during a chatbot session:
1. **Session Length**: Measures the total time spent interacting with the chatbot.
2. **Turn Count**: Tracks the total number of exchanges (user input and bot response).
3. **Drop-Off Rate**: Identifies the proportion of unfinished interactions.
4. **Knowledge Gain**: Assesses how much the user learns during the session using quizzes.
5. **Accuracy of Responses**: Compares the chatbot's answers to predefined correct responses.

The session data is logged in a JSON file for further analysis.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

---

## Requirements

This script requires Python 3.7 or higher. No additional libraries are needed beyond Python's standard library.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/educational-chatbot-metrics.git
   cd educational-chatbot-metrics
