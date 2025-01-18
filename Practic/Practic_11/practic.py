from PIL import Image
from PIL import ImageDraw,ImageFont


# im = Image.open("dog.jpg")
#
# """ узнаем какого формата, размера и какую систему цвета используют """
# print(im.format, im.size, im.mode)
#
# """ выведем изображение на экран """
# im.show()
#
# """ уменьшим нашу картинку """
# out = im.resize((128, 128))
# out.show()
#
# """ выведем и сохраним для дальнейшей работы высоту и длину изображения """
# w, h = im.size
# print(w, h)
#
# ### теперь можно менять размеры более точно, например уменьшать в 2 раза
# out = im.resize((w//3, h//3))
# out.show()

### --------------------------------
# """ создадим функцию, которая будет делать все вышеизложенное"""
# def new_photo(name):
#     image = Image.open(name)
#     w, h = image.size
#     return image.resize((w // 4, h // 4))
#
# im = new_photo('dog.jpg')
# ###im.show()
#
# ### --- вставим в первый рисунок другой, для этого уберем верхний вывод на экран
# im_2 = new_photo('summer.png')
#
# w, h = im.size
#
# im.paste(im_2, (w-300, h-280))
#
# ### ------------------
# """ вставим текст """
# draw = ImageDraw.Draw(im)
# font = ImageFont.truetype('appetite-italic.ttf', 50)
# draw.text((100, 600), "Привет мир!!!", font=font, fill = 'red')
#
# im.show()

### ---------------------------------------------------
""" создали класс PostMaker """
class PostMaker:
    def __init__(self, name_photo):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        # self.image = self.image.resize((self.w // 2, self.h // 2)) # будет применяться, если нужно будет уменьшить размеры


    def paste(self, name_photo):
        paste_image = Image.open(name_photo)
        self.image.paste(paste_image, (200, 1200))


    def upgrade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("appetite-italic.ttf", 250)
        draw.text((150, 100), text, font=font, fill='red')
        self.image.show()


image = PostMaker('dog.jpg')
image.paste("summer.png")
image.upgrade("Привет, котенок!!!")