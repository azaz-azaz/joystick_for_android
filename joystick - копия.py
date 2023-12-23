from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.properties import NumericProperty

class JoystickApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.label = Label(text='Joystick Position: (0, 0)')
        self.layout.add_widget(self.label)

        self.slider_x = Slider(min=-1, max=1, value=0, step=0.01)
        self.slider_y = Slider(min=-1, max=1, value=0, step=0.01)

        self.layout.add_widget(self.slider_x)
        self.layout.add_widget(self.slider_y)

        self.button_save = Button(text='Save Joystick Position')
        self.button_save.bind(on_press=self.save_position)
        self.layout.add_widget(self.button_save)

        return self.layout

    def save_position(self, instance):
        position = (self.slider_x.value, self.slider_y.value)
        self.label.text = f'Joystick Position: {position} - Saved!'

if __name__ == '__main__':
    JoystickApp().run()