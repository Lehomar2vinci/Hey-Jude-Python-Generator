import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class HeyJudeApp(App):
    couplets = [
        "Make it better",
        "Take a sad song and make it better",
        "Remember to let her into your heart",
        "Then you can start to make it better"
    ]

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.title = "Hey Jude"

        label = Label(text=self.title, font_size='30sp', size_hint=(1, 0.2))
        layout.add_widget(label)

        button = Button(text="Afficher les couplets", font_size='20sp', size_hint=(1, 0.2))
        button.bind(on_release=self.afficher_couplets)
        layout.add_widget(button)

        self.couplets_label = Label(text="", font_size='20sp', size_hint=(1, 0.6))
        layout.add_widget(self.couplets_label)

        return layout

    def afficher_couplets(self, *args):
        random.shuffle(self.couplets)
        couplets_text = "\n".join(self.couplets)
        self.couplets_label.text = couplets_text + "\nBetter better better better better waaaaaa"

if __name__ == '__main__':
    HeyJudeApp().run()
