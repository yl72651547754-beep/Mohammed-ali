# main.py
from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text='مرحباً بالعالم', font_size='40sp')

if __name__ == '__main__':
    HelloApp().run()