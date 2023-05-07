import os
from typing import List, Dict, Optional

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = os.environ.get("MODEL", "gpt-3.5-turbo")
TEMPERATURE = os.environ.get("TEMPERATURE", 0.5)
SYSTEM_ROLE = os.environ.get("SYSTEM_ROLE", "You are a helpful assistant.")


def main(messages: Optional[List[Dict[str, str]]] = None) -> None:
    """
    Interactively send questions to the ChatGPT model and display its
    responses.

    Args:
        messages (Optional[List[Dict[str, str]]]): A list of message
        dictionaries, where each dictionary contains a 'role'
        (either "system" or "user")and 'content' (the message text).
        Leave empty to start a new conversation.
        Defaults to None.

    Returns:
        None
    """

    if not messages:
        messages = [
            {
                "role": "system",
                "content": SYSTEM_ROLE,
            }
        ]

    messages.append(
        {
            "role": "user",
            "content": input("Question: ")
        },
    )

    response = openai.ChatCompletion.create(
        model=MODEL, messages=messages, temperature=float(TEMPERATURE)
    )

    messages.append(response.choices[0].message)
    print(f"Answer: {response.choices[0].message.content}")
    main(messages)

    return


if __name__ == "__main__":
    main()
