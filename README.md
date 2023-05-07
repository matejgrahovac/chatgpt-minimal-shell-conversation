# Minimal ChatGPT Python Script

This Python script allows you to interactively send questions to the ChatGPT model and display its responses in the shell.

## Prerequisites

- Python 3.6 or higher
- An OpenAI API key
- Operating Systems: Windows, macOS, or Linux

## Getting an OpenAI API Key

To obtain an OpenAI API key, sign up for an account at [OpenAI](https://platform.openai.com/). Once you have an account, you can find your API key in the [API Keys section](https://platform.openai.com/account/api-keys/) of your account dashboard.

## Installation

1. Clone the repository or download the script.

2. Create a virtual environment using `venv`:

   ```
   python3 -m venv .venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```
     .venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     .venv/bin/activate
     ```

4. Install the required packages using the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

5. Make a copy of `.env-template` named `.env` in the same directory as the script and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

   Optionally, you can also set the following variables in the `.env` file:

   - `MODEL`: The model to use (default: "gpt-3.5-turbo", you can also use "gpt-4" if available)
   - `TEMPERATURE`: The temperature for the model's response (default: 0.5)
   - `SYSTEM_ROLE`: The system role message (default: "You are a helpful assistant.")

## Usage

Run the script:

```
python main.py
```

You will be prompted to enter a question. The script will then send the question to the ChatGPT model and display its response. You can continue asking questions interactively.

Example:

```
Question: What is the capital of France?
Answer: The capital of France is Paris.
```

End the script with ctrl + c (windows, linux) or control + c (mac).
