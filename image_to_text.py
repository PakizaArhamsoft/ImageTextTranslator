from PIL import Image
import pytesseract

def image_to_txt(image_path):
    result = pytesseract.image_to_string(Image.open(image_path))
    print(result)
    return result
