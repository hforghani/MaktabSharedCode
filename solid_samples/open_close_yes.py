import abc

import translators


class AbstractTranslator(abc.ABC):
    @abc.abstractmethod
    def translate(self, text:str , source_lang:str, target_lang:str) -> str:
        pass


class GoogleTranslator(AbstractTranslator):
    def translate(self, text, source_lang, target_lang):
        return translators.translate_text(
            text, "google", source_lang, target_lang)


class OpenAITranslator(AbstractTranslator):
    def translate(self, text:str , source_lang:str, target_lang:str) -> str:
        return openai.translate(test, source_lang, target_lang)


class User:
    def __init__(self, username):
        self.username = username
        self.history = []

    def edit_user(self, new_name):
        self.username = new_name

    def translate(self, text, source_lang, target_lang, translator: AbstractTranslator):
        res = translator.translate(text, source_lang, target_lang)
        self.history.append(
            {"text": text, "translate_lang": f"{source_lang}-to-{target_lang}", f"{target_lang}_text": res})

    def show_history(self):
        return self.history
