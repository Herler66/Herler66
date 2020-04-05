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
# import kivy
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty


# class Touch(Widget):
#     btn = ObjectProperty(None)

#     def on_touch_down(self, touch):
#         print("Mouse Down", touch)
#         self.btn.opacity = 0.5

#     def on_touch_move(self, touch):
#         print("Mouse Move", touch)

#     def on_touch_up(self, touch):
#         print("Mouse UP", touch)
#         self.btn.opacity = 1


# class MyApp(App):
#     def build(self):
#         return Touch()


# if __name__ == "__main__":
#     MyApp().run()

# <Touch>:
#     btn: btn

#     Button:
#         id: btn
#         text:"My Btn"

#6
# from kivy.app import App
# from kivy.graphics import Rectangle
# from kivy.graphics import Color
# from kivy.uix.widget import Widget
# from kivy.graphics import Line
# class Touch(Widget):
#     def __init__(self, **kwargs):
#         super(Touch, self).__init__(**kwargs)

#         with self.canvas:
#             Line(points=(20,30,400,500,60,500))
#             Color(1,0,0,0.5, mode="rgba")
#             self.rect = Rectangle(pos=(0,0), size=(50,50))


#     def on_touch_down(self, touch):
#         self.rect.pos = touch.pos

#     def on_touch_move(self, touch):
#         self.rect.pos = touch.pos
# class MyApp(App):
#     def build(self):
#         return Touch()
# if __name__ == "__main__":
#     MyApp().run()

#7
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return Widgets()


def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()


if __name__ == "__main__":
    MyApp().run()