import translators


class User:
    def __init__(self, username):
        self.username = username
        self.history = []

    def edit_user(self, new_name):
        self.username = new_name

    def translate(self, text, source_lang, target_lang):
        org = translators.translate_text(
            text, "google", source_lang, target_lang)
        self.history.append(
            {"text": text, "translate_lang": f"{source_lang}-to-{target_lang}", f"{target_lang}_text": org})

    def show_history(self):
        return self.history