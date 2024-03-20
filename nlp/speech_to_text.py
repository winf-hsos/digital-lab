import pyaudio
import wave
import os

from openai import OpenAI
client = OpenAI()

# This function contains the code to record audio from the microphone
def record_audio(seconds, output_file="output.wav"):
    # Audio recording parameters
    FORMAT = pyaudio.paInt16 # data format
    CHANNELS = 1             # number of channels
    RATE = 44100             # sampling rate
    CHUNK = 1024             # frames per buffer
    
    audio = pyaudio.PyAudio()
    
    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    frames = []

    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
   
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    audio.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    audio_file = open("output.wav", "rb")
    return audio_file

input("Hit enter to start recording")
print("Recording for 3 seconds...")
audio_file = record_audio(3)

response = client.audio.transcriptions.create(
     model="whisper-1",
     file=audio_file
     )
        
command = response.text
print(f"Your command was: {command}")

# Delete audio file
audio_file.close()
os.remove("output.wav")