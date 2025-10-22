import tamil_unicode_map
from collections import deque
import csv

class Mapper(object):
    def __init__(self, charmap):
        self.codepoint_to_english = {}
        self.codepoint_to_category = {}
        self.codepoint_to_char = {}
        self.populate_map(charmap)
        self.categories = {
             'consonants': 'consonants',
             'pulli': 'pulli',
             'dependent_vowels_two_part': 'vowels',
             'dependent_vowels_left': 'vowels',
             'various_signs': 'vowels',
             'independent_vowels': 'vowels',
             'dependent_vowels_right': 'vowels'
        }

    def populate_map(self, charmap):
        for category in charmap:
            codepoints = charmap[category]
            for codepoint in codepoints:
                self.codepoint_to_char[codepoint] = codepoints[codepoint][0]
                in_english = codepoints[codepoint][1]
                if isinstance(in_english, tuple):
                    self.codepoint_to_english[codepoint] = in_english[0]
                else:
                    self.codepoint_to_english[codepoint] = in_english
                self.codepoint_to_category[codepoint] = category

    def in_english(self, c):
        return self.codepoint_to_english.get(c, '')

    def char_type(self, c):
        sub_type = self.codepoint_to_category.get(c, '')
        parent_type = self.categories.get(sub_type, '')
        return parent_type, sub_type

class TamilTransliterator(object):
    def __init__(self, charmap):
        self.mapper = Mapper(charmap)

    def to_english(self, text):
        text = self.preprocess(text)
        text = deque(text)
        output = deque()
        l = len(text)

        while text:
            c = text.popleft()
            in_english = self.mapper.in_english(c)
            parent_type, sub_type = self.mapper.char_type(c)
     
            if parent_type == 'pulli':
                output.pop() 
            elif parent_type == 'vowels' and sub_type != 'independent_vowels':
                output.pop()
                output.extend(deque(in_english))
            else:
                output.extend(deque(in_english))
        return u''.join(output)  

    def preprocess(self, text):
        if isinstance(text, str):
            return text
        elif isinstance(text, bytes):
            return text.decode('utf-8')


    def transliterate(self, text):
        words = text.split()
        transliterated_words = [self.to_english(w) for w in words]
        return u' '.join(transliterated_words).lower()

if __name__ == "__main__":
    t = TamilTransliterator(tamil_unicode_map.charmap)
    with open('input.txt', 'r', encoding='utf-8') as f_input, open('output.csv', 'w', newline='', encoding='utf-8') as f_output:
        csv_writer = csv.writer(f_output)
        csv_writer.writerow(['Tamil Text', 'English Transliteration'])
        for line in f_input:
            text = line.strip()
            transliteration = t.transliterate(text)
            csv_writer.writerow([text, transliteration])

    print("Transliteration completed. Output saved to output.csv")