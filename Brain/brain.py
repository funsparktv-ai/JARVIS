import ollama
from rich import print
import os

# Initialize Ollama for AI conversation handling
ollama_model = "llama3"  # You can use the model you want, e.g., llama2 or others

# Function for handling AI responses
def Main_Brain(text):
    try:
        # Send the user input to Ollama's model and get the response
        response = ollama.chat({
            "model": ollama_model,
            "prompt": text,
        })
        rawdog_feedback = rawdog.main(response['message'])  # Assuming response is in 'message'

        # Handle feedback from RawDogz
        if rawdog_feedback:
            print(rawdog_feedback)
            response = ollama.chat({
                "model": ollama_model,
                "prompt": rawdog_feedback,
            })

        # Modular response for advanced task handling (future integration)
        handle_automation_tasks(response['message'])
        handle_voice_output(response['message'])
        return response['message']

    except Exception as e:
        print(f"[red]Error in Main_Brain: {str(e)}[/red]")
        return "Something went wrong, please try again."


# Function to handle task automation (link with other automation scripts)
def handle_automation_tasks(response):
    if "open app" in response.lower():
        from open_App import open_application
        open_application(response)
    elif "battery status" in response.lower():
        from Battery import check_battery
        check_battery()


# Function to handle voice output (link with TTS module)
def handle_voice_output(response):
    from TextToSpeech.Fast_DF_TTS import speak
    speak(response)


# Example: Initialize Jarvis and respond to a test query
if __name__ == "__main__":
    print("[green]Jarvis is running...[/green]")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = Main_Brain(user_input)
        print(f"Jarvis: {response}")
