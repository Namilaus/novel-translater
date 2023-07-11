import translators as translator


def translatedText(novel_content)->str:
    text = translator.translate_html(novel_content,translator='google')
    return text


