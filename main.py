import os
import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Input audio file
audio_file = "audio/harvard.wav"

# Output folder and file
output_folder = "output"
output_file = os.path.join(output_folder, "transcript.txt")

try:
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the audio file
    with sr.AudioFile(audio_file) as source:
        print("Reading audio file...")
        audio_data = recognizer.record(source)

    print("Converting speech to text...")

    # Convert speech to text
    text = recognizer.recognize_google(audio_data)

    print("\n===== Transcript =====")
    print(text)

    # Save transcript to a text file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"\nTranscript saved successfully!")
    print(f"Location: {output_file}")

except FileNotFoundError:
    print("Error: Audio file not found.")

except sr.UnknownValueError:
    print("Error: Could not understand the audio.")

except sr.RequestError as e:
    print(f"Error: Could not connect to the Speech Recognition service.\n{e}")

except Exception as e:
    print(f"Unexpected Error: {e}")