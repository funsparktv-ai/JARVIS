import os
import requests  # pip install requests
from playsound import playsound  # pip install playsound==1.2.2
from typing import Union


# Function to generate audio using a text-to-speech API
def generate_audio(message: str, voice: str = "Matthew") -> Union[bytes, None] :
    url: str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{message}}}"

    headers = {
        'User-Agent' : ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36')
    }

    try :
        # Send request to the API and retrieve the audio content
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # Raise exception for any HTTP errors
        return response.content
    except requests.RequestException as e :
        print(f"Error fetching audio from API: {e}")
        return None


# Function to play the generated speech audio and clean up the temporary file
def speak(message: str, voice: str = "Matthew", folder: str = ".", extension: str = ".mp3") -> None :
    try :
        # Generate the audio content
        result_content = generate_audio(message, voice)
        if result_content is None :
            print("Failed to generate audio.")
            return

        # Create the file path for saving the audio
        file_name = f"{voice}_{hash(message)}{extension}"
        file_path = os.path.join(folder, file_name)

        # Write the audio content to a temporary file
        with open(file_path, "wb") as audio_file :
            audio_file.write(result_content)

        # Play the audio
        playsound(file_path)

    except Exception as e :
        print(f"An error occurred during TTS processing: {e}")

    finally :
        # Ensure the file is deleted after playing the audio
        if os.path.exists(file_path) :
            os.remove(file_path)

