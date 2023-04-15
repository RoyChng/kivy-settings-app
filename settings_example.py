from kivy.app import App
from kivy.uix.accordion import Accordion

class SettingsLayout(Accordion):
    def checkbox_handler(self, _, is_active, value):
        if not is_active: return
        self.ids.screen_resolution_img.source = f"extra_imgs/{value}.png"
        

class SettingsApp(App):
    def build(self):
        return SettingsLayout()
    

if __name__ == "__main__":
    SettingsApp().run()