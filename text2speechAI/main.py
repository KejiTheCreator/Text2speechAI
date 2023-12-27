import gtts

def text2speech(text):
  # Create a gTTS object
  tts = gtts.gTTS(text=text, lang='en')

  # Save the audio file
  tts.save('audio.mp3')

  # Play the audio file

# Test the text2speech function
text2speech('Hello, world!')
