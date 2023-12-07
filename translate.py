
from googletrans import Translator

def translate_mongolian_to_english(text):
    translator = Translator()
    translated_text = translator.translate(text, dest="en")
    return translated_text.text

def translate_english_to_mongolian(text):
    translator = Translator()
    translated_text = translator.translate(text, dest="mn")
    return translated_text.text

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Example usage:
#original_text = "Hello, how are you?"
#target_language = 'mn'  # Change this to the desired language code

#translated_text = translate_text(original_text, target_language)
#print(f"Original text: {original_text}")
#print(f"Translated text: {translated_text}")