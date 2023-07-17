import translators as translator


def translatedText(novel_content)->str:
    if novel_content is None:
        return None
    text = translator.translate_html(novel_content,translator='google')
    return text


