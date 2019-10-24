from random import choices, randint
from PIL import ImageDraw, Image
from PIL import ImageFont
import os
from tqdm.auto import tqdm


class PictureGenerator:
    spacing = 10

    def __init__(self, char_set, char_probs=None):
        self.char_set = list(char_set)
        self.char_probs = char_probs
        self.char_size = dict()

    def create_dataset(self, n_pics, size, font_types, path=''):
        for _ in tqdm(range(n_pics)):
            font = font_types[randint(0, len(font_types) - 1)]
            self.create_pic(size, font, os.path.join(path, '{}.png'.format(_)))

    def create_pic(self, size, font, path):
        text = self.generate_text((size[0] - 10, size[1] - 10), font)
        img_font = ImageFont.truetype(font, encoding='UTF-8')
        img = Image.new('RGB', (200, 200), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((5, 5), text, (0, 0, 0), font=img_font)
        img.save(path)

    def generate_text(self, size, font):
        height = 0
        text = []
        while height < size[1]:
            line = self.generate_line(size[0], font)
            height = self.get_size(text + line, font)[1]
            text.extend(line)
        lines = ''.join(text).split('\n')
        while height > size[1]:
            lines.pop()
            height = self.get_size(lines, font)[1]
        return ''.join(text)

    def generate_line(self, line_length, font):
        length = 0
        line = []
        while length < line_length:
            word = self.generate_word()
            length = self.get_size(line + word, font)[0]
            line.extend(word)
        while length > line_length:
            line.pop()
            length = self.get_size(line, font)[0]
        line.append('\n')
        return line

    def generate_word(self):
        word_length = randint(0, 15)
        word = choices(self.char_set, weights=self.char_probs, k=word_length)
        word.append(' ')
        return word

    def get_size(self, text, font):
        img_font = ImageFont.truetype(font, encoding='UTF-8')
        img = Image.new('RGB', (200, 200), color=(255, 0, 255))
        d = ImageDraw.Draw(img)
        return d.textsize(''.join(text), img_font)


if __name__ == '__main__':
    char_set = set('йцукенгшщзхъфывапролджэячсмитьбю.ё1234567890-=+.,\/":ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМТЬБЮЮЮЁ')
    pic_gen = PictureGenerator(char_set)
    pic_gen.create_dataset(10, (200, 200), ['arial'], path = r'D:\Users\mkuznetsova\Desktop\dataset')
