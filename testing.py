import Client

#initialise the API
client = Client.Talk()

client.tts("Testing the TTS function from the ChatGPT API", voice = "alloy", number = "test", speed = 0.9)