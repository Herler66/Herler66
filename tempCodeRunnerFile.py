# python -m pip install --upgrade pip wheel setuptools
# python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
# python -m pip install kivy.deps.gstreamer
# python -m pip install kivy.deps.angle
# python -m pip install pygame
# python -m pip install kivy

#1
# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# class MyApp(App):
#     def build(self):
#         return Label(text = "tech with tim")
# if __name__ == "__main__":
#     MyApp().run()



#2
# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button


# class MyGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.cols = 1

#         self.inside = GridLayout()
#         self.inside.cols = 2

#         self.inside.add_widget(Label(text="First Name: "))
#         self.name = TextInput(multiline=False)
#         self.inside.add_widget(self.name)

#         self.inside.add_widget(Label(text="Last Name: "))
#         self.lastName = TextInput(multiline=False)
#         self.inside.add_widget(self.lastName)

#         self.inside.add_widget(Label(text="Email: "))
#         self.email = TextInput(multiline=False)
#         self.inside.add_widget(self.email)

#         self.add_widget(self.inside)

#         self.submit = Button(text="Submit", font_size=40)
#         self.submit.bind(on_press=self.pressed)
#         self.add_widget(self.submit)

#     def pressed(self, instance):
#         name = self.name.text
#         last = self.lastName.text
#         email = self.email.text

#         print("Name:", name, "Last Name:", last, "Email:", email)
#         self.name.text = ""
#         self.lastName.text = ""
#         self.email.text = ""

# class MyApp(App):
#     def build(self):
#         return MyGrid()


# if __name__ == "__main__":
#     MyApp().run()



#3
# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty


# class MyGrid(Widget):
#     name = ObjectProperty(None)
#     email = ObjectProperty(None)

#     def btn(self):
#         print("Name:", self.name.text, "email:", self.email.text)
#         self.name.text = ""
#         self.email.text = ""

# class MyApp(App):
#     def build(self):
#         return MyGrid()


# if __name__ == "__main__":
#     MyApp().run()
# <MyGrid>:

#     name: name
#     email: email

#     GridLayout:
#         cols:1
#         size: root.width - 200, root.height -200
#         pos: 100, 100

#         GridLayout:
#             cols:2

#             Label:
#                 text: "Name: "

#             TextInput:
#                 id: name
#                 multiline:False

#             Label:
#                 text: "Email: "

#             TextInput:
#                 id: email
#                 multiline:False

#         Button:
#             text:"Submit"
#             on_press: root.btn()




#4
# import kivy
# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout


# class MyApp(App):
#     def build(self):
#         return FloatLayout()


# if __name__ == "__main__":
#     MyApp().run()
# <Button>:
#     font_size: 40
#     color: 0.1,0.5,0.6,1
#     size_hint: 0.5,0.5

# <FloatLayout>:
#     Button:
#         text: "Tech With"
#         pos_hint: {"x":0.5, "top":1}

#     Button:
#         id: btn
#         text:"Tim" if btn.state == "normal" else "down"


#5
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen


# class MainWindow(Screen):
#     pass


# class SecondWindow(Screen):
#     pass


# class WindowManager(ScreenManager):
#     pass


# kv = Builder.load_file("my.kv")


# class MyMainApp(App):
#     def build(self):
#         return kv


# if __name__ == "__main__":
#     MyMainApp().run()


# my.kv
# WindowManager:
#     MainWindow:
#     SecondWindow:

# <MainWindow>:
#     name: "main"

#     GridLayout:
#         cols:1

#         GridLayout:
#             cols: 2

#             Label:
#                 text: "Password: "

#             TextInput:
#                 id: passw
#                 multiline: False

#         Button:
#             text: "Submit"
#             on_release:
#                 app.root.current = "second" if passw.text == "tim" else "main"
#                 root.manager.transition.direction = "left"


# <SecondWindow>:
#     name: "second"

#     Button:
#         text: "Go Back"
#         on_release:
#             app.root.current = "main"
#             root.manager.transition.direction = "right"


#6
# import kivy
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.uix.label import Label
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.popup import Popup


# class Widgets(Widget):
#     def btn(self):
#         show_popup()

# class P(FloatLayout):
#     pass


# class MyApp(App):
#     def build(self):
#         return Widgets()


# def show_popup():
#     show = P()

#     popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))

#     popupWindow.open()


# if __name__ == "__main__":
#     MyApp().run()

# <Widgets>:
#     Button:
#         text: "Press me"
#         on_release: root.btn()

# <P>:
#     Label:
#         text: "You pressed the button"
#         size_hint: 0.6, 0.2
#         pos_hint: {"x":0.2, "top":1}

#     Button:
#         text: "You pressed the button"
#         size_hint: 0.8, 0.2
#         pos_hint: {"x":0.1, "y":0.1}


#7
