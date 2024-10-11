# assistant.py

from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL
import json
from functions import get_current_weather

client = OpenAI(api_key=OPENAI_API_KEY)

def create_function_definitions():
    """
    Define the function schemas for the assistant to use.

    Returns:
        list: A list of function definitions.
    """
    functions = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and country code, e.g., 'San Francisco, US'",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature",
                    },
                },
                "required": ["location"],
            },
        },
    ]
    return functions

def process_user_message(messages):
    """
    Process the user's message and generate a response.

    Args:
        messages (list): The conversation history.

    Returns:
        str: The assistant's response.
    """
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        functions=create_function_definitions(),
        function_call="auto"
    )

    response_message = response.choices[0].message

    if response_message.function_call:
        # The assistant wants to call a function
        function_name = response_message.function_call.name
        arguments = json.loads(response_message.function_call.arguments)
        function_response = None

        if function_name == "get_current_weather":
            location = arguments.get("location")
            unit = arguments.get("unit", "celsius")
            function_response = get_current_weather(location, unit)

        # Add the assistant's function call and the function's response to the conversation
        messages.append(response_message)  # Assistant's message with function call
        messages.append({
            "role": "function",
            "name": function_name,
            "content": json.dumps(function_response),
        })

        # Get the final response from the assistant after function execution
        second_response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages
        )
        return second_response.choices[0].message.content
    else:
        # The assistant didn't call a function
        return response_message.content
