from guizero import App, Text, Picture

app = App("Wanted!")
app.bg = "#FBFBD0"

wanted_text = Text(app, "WANTED")
wanted_text.text_size = 80
wanted_text.text_color = "red"
wanted_text.font= "Times New Roman"

cat = Picture(app, image="series x.png")

app.display()