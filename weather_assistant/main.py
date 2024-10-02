# main.py

from assistant import process_user_message

def main():
    print("Welcome to the Weather Assistant!")
    print("You can ask me about the current weather in any city.")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    messages = [
        {"role": "system", "content": "You are a helpful assistant that provides weather information."},
    ]

    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Assistant: Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        assistant_response = process_user_message(messages)
        print(f"Assistant: {assistant_response}")

        messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    main()
