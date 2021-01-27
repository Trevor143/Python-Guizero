from guizero import App, TextBox, Drawing, Combo, Slider

#functions
def draw_meme():
    meme.clear()
    meme.image(0,0, "series x.png")
    meme.text(20,20, top_text.value, color=color.value, size=size.value, font="courier")
    meme.text(20,320, bottom_text.value, color=color.value, size=size.value, font="times new roman")

#app
app = App("Meme Generator")

#widgets
top_text = TextBox(app, "top_text",  command=draw_meme)
bottom_text = TextBox(app, "bottom_text", command=draw_meme)
color = Combo(app, options=["black","white", "red", "green", "blue", "orange"],
command=draw_meme, selected="green")
size = Slider(app, start=20, end=40, command=draw_meme)
meme = Drawing(app, width="fill", height="fill")


#display
draw_meme()
app.display()