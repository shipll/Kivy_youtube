from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.resources import resource_add_path
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from pytube import YouTube, Playlist
import os, sys
from kivy.resources import resource_add_path, resource_find
from kivymd.app import MDApp


class PopWindows(BoxLayout):
    pass


class mydrop(DropDown):
    pass


class MyFloat(FloatLayout):
    pass


class MyFloat2(FloatLayout):
    pass


class MyFloat3(FloatLayout):
    pass


class MyFloat4(FloatLayout):
    pass


class Screen_1(Screen):
    pass


class Screen_2(Screen):
    pass


class Screen_3(Screen):
    pass

class Screen_4(Screen):
    pass

class Screen_Manager(ScreenManager):
    mylink = StringProperty()
    my_image = StringProperty('youtube.jpg')
    thumb = StringProperty('R.jpeg')

    def check(self, widget):
        try:
            self.mylink = widget.text
            YT = YouTube(self.mylink)
            try:
                print(Playlist(self.mylink))
                self.current = 'scr_4'
            except:
                self.current = 'scr_2'
            finally:
                widget.text = ''
        except:
            self.pop("wrong link")
            widget.text = ''

    def pop(self, comment):
        popup = Popup(title=f"{comment}", content=PopWindows(), size_hint=(None, None), size=(300, 300))
        popup.open()

    def start(self, widget, main, label, image_box, image):
        main.remove_widget(widget)
        thumb = YouTube(self.mylink).thumbnail_url
        title = YouTube(self.mylink).title
        image_box.remove_widget(image)
        image_box.add_widget(AsyncImage(source=thumb))
        label.text = title

    def download(self, widget, resolution, label, main, start, image_box):
        resolution.disabled = True
        widget.disabled = True
        label.text = 'Please wait\nDownloading...'
        if self.current == 'scr_2':
            yt_object = YouTube(self.mylink).streams
            res = resolution.text
            if res == 'High quality':
                down_load = yt_object.get_highest_resolution().download()
            if res == 'Low quality':
                down_load = yt_object.get_lowest_resolution().download()
            if res == 'Audio':
                down_load = yt_object.get_audio_only().download()
            self.current = 'scr_3'
        if self.current == 'scr_4':
            PL_objects = Playlist(self.mylink).videos
            if resolution.text == 'Audio':
                for v in PL_objects:
                    v.streams.get_audio_only().download()
            if resolution.text == 'High quality':
                for v in PL_objects:
                    v.streams.get_highest_resolution().download()
            if resolution.text == 'Low quality':
                for v in PL_objects:
                    v.streams.get_lowest_resolution().download()
        self.current = 'scr_3'
        resolution.disabled = False
        label.text = 'YouTube Downloador \n\n...shipll....'
        main.add_widget(start)
        image_box.clear_widgets()

    def go_back(self):
        self.current = 'scr_1'


class MyApp(App):
    Window.size = (500, 300)
    Window.clearcolor = (0, 0, 0)

    def build(self):
        return Builder.load_file('mykivy.kv')


if __name__ == '__main__':
    try:
        if hasattr(sys, '_MEIPASS'):
            resource_add_path(os.path.join(sys._MEIPASS))
        app = MyApp()
        app.run()
    except Exception as e:
        print(e)
        input("Press enter.")
