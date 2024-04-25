from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RotuloApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        self.lab1 = Label(
            text='senai', color=[1, 0, 0, 1],
            font_size=40, bold=True
        )
        
        self.lab2 = Label(
            text='sesi', color=[0, 1, 0, 1],
            font_size=40, italic=True
        )

        self.lab3 = Label(
            text='enem', color=[0, 0, 1, 1],
            font_size=40, font_name='arial',
            underline=True
        )
        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3)
        return layout

if __name__ == '__main__':
    RotuloApp().run()