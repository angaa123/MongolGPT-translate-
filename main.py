import translate
import gpt
user_text= ""
while user_text != "out":
    user_text = input("user :")
    gptInput =  translate.translate_mongolian_to_english(user_text)
    gptOut = gpt.gpt_model(gptInput)
    mongolGptOut =  translate.translate_english_to_mongolian(gptOut)
    print(mongolGptOut)