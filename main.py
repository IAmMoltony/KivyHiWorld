import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

kivy.require('2.2.1')

class AppWidget(Widget):
    def __init__(self, **kwargs):
        super(AppWidget, self).__init__(**kwargs)
        button = Button(text='Click me :3', font_size='24px', background_color=(0, 1, 0, 1), color=(0, 1, 0, 1), size=(130, 48), size_hint=(0.2, 0.2), pos=(250, 200))
        button.bind(on_press=self.callback)
        self.add_widget(button)

    def callback(self, instance):
        layout = GridLayout(cols=1, padding=20)
        popup_text = Label(text='Hi, world!')
        popup_close_button = Button(text='OK', size_hint=(0.001, 0.6))
        layout.add_widget(popup_text)
        layout.add_widget(popup_close_button)
        popup = Popup(title='Look im a popup', content=layout, size_hint=(None, None), size=(256, 256))
        popup_close_button.bind(on_press=popup.dismiss)
        popup.open()

class HiWorldApp(App):
    def build(self):
        return AppWidget()

HiWorldApp().run()
