from guizero import App,Text, PushButton
from random import choice

# functions
def choose_name():
    first_name = ["trevor", "tevin", "bob", "andy", "michael"]
    last_name = ["roberts", "michaels", "makumbi", "mwangi"]

    spy_name = choice(first_name) +" "+choice(last_name)

    name = Text(app, text=spy_name)


# app
app = App("Top Secret")

# widgets
title = Text(app, "Push the red buttion to get a spy name")
name = Text(app, text="")
button = PushButton(app, choose_name, text="Click to Choose")
button.bg= "red"
button.text_size=20


# display
app.display()