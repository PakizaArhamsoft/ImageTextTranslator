# pip install googletrans==4.0.0rc1
import imp
from googletrans import Translator
import image_to_text
translator = Translator(service_urls=['translate.google.com'])
def translate_txt(data):
    print('detected lang: ',translator.detect(data).lang)

    res = translator.translate(data, dest='ur')
    print("Translate into Urdu: ",res.text)
    return res.text

result = image_to_text.image_to_txt('sample1.png')
result = translate_txt(result)
