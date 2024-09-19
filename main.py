import json

import ImageHandling
import Client

#initialise the API
client = Client.Talk()

def generate_prompt(food1, food2, food3, food4, food5):
    prompt = f"""
        could you create me a unique recipe using these 5 ingrediants.
        descripe the way the meal looks at each stage in great detail and also give a very simple to follow step by
        step guide on how to make the meal labelled using the format '1)'. also add the descriptions of the steps
        using the same format.

        I want the descriptions to be used to create a picture these meals step by step using your Dall-e engine at a later date,
        so could you try and do whats best for the Dalle engine to create. make the food anime, with saturated colours, steam, nice looking food, and sparkly.

        the 5 ingrediants are {food1}, {food2}, {food3}, {food4}, {food5}.

        I want the format to be returned as a 2 by n (where n is the number of steps) python array like so, [["step 1 instruction", "step 1 detailed desctiption of scene"], ["step 2 instruction", "step 2 detailed description of scene"], [....]]. only return whats in the array, nothing else!! also dont print any blank sapces or tabs unless it is part of the instruction.

    """
    return prompt

#generate the script using the prompt
script = client.push_prompt(generate_prompt("beef", "pasta", "cream", "courgette", "pineapple"))

#load the response into array format
res = json.loads(script)

#print(script)
print(res)

#loop over array and generate images
for i in range(len(res)):
    if (i==0):
        img_b64 = client.generate_image(res[i][1])
    else:
        prev_img_b64 = img_b64
        img_b64 = client.generate_image(scene = res[i][1], encodedimage = prev_img_b64)
    
    ImageHandling.to_png(img_b64, i)


print("length rows = ", len(res), "\nlength columns = ", len(res[0]))

