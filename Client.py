from openai import OpenAI

class Talk:
    def __init__(self):
        #set the API Key from file
        API_KEY = open("API_KEY", "r").read()

        #assign the key to start using the API
        self.client = OpenAI(api_key=API_KEY)

    def push_prompt(self, prompt, model="gpt-4o-mini"):
        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return completion.choices[0].message.content

    def generate_image(self, scene="return the number 1 and nothing else", encodedimage = None):
        response = self.client.images.generate(
            prompt=scene,
            #image=encodedimage,
            n=1,
            size="1024x1024",
            response_format="b64_json"
        )
        return response.data[0].b64_json

