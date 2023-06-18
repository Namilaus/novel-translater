from content import getContent
import translators as translator

def translatedText(url)->str:

    novel_content = getContent('https://www.69shu.com/txt/1464/6929496')

    text = translator.translate_html(novel_content,translator='google')

    return text


