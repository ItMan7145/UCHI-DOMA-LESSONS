# программисты - ленивые люди
from deep_translator import GoogleTranslator


class MyFileAnalyzer:
    def __init__(self, text):
        self.text = text

    def get_letter_count(self):
        letter_count = 0
        for i in self.text:
            if i.isalpha():
                letter_count += 1
        return letter_count

    def get_words_count(self):
        words_count = 0
        wo_spaces = self.text.split()

        for i in wo_spaces:
            has_alpha = False
            for j in i:
                if j.isalpha():
                    has_alpha = True
                    break
            if has_alpha: words_count += 1
            # words_count += 1 if has_alpha else None

        return words_count

    def get_line_count(self):
        return len(self.text.split('\n'))

    def get_deep_translation(self):
        translator = GoogleTranslator(source="auto", target="russian")
        return translator.translate(text=self.text)


with open('file1.txt', 'r') as file:
    text = file.read()
    print(text)
    analyzer = MyFileAnalyzer(text)

    print(analyzer.get_letter_count())
    print(analyzer.get_words_count())
    print(analyzer.get_line_count())
    print(analyzer.get_deep_translation())
