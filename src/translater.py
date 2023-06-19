import translators as translator
from time import sleep

isFinish = False

def translatedText(novel_content)->str:
    text = translator.translate_html(novel_content,translator='google')
    isFinish = True
    return text


