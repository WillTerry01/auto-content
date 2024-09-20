import Client

#initialise the API
client = Client.Talk()

client.tts("have you been a good little boy for mommy?", voice = "alloy", number = "test", speed = 0.9)