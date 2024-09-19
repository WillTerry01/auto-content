import base64
import binascii

#converting the image from base64 to png
def to_png(b64_img, n):
    try:
        image = base64.b64decode(b64_img, validate=True)
        file_to_save = f"my_image{n}.png"
        with open(file_to_save, "wb") as f:
            f.write(image)
    except binascii.Error as e:
        print(e)

#converting the image from png to base64
def to_b64(image_name):
    with open(f"{image_name}.png", "rb") as f:
        base64_string = base64.b64encode(f.read())
    return base64_string