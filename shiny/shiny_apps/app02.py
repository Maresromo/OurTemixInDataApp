from shiny import App, reactive, render, ui

app_ui = ui.page_fixed(
    ui.h4("Saludo Personalizado"),
    ui.input_text("name", "Introduce tu nombre:", value="Shiny User"),
    ui.output_text_verbatim("greeting"),
)

def server(input, output, session):
    @reactive.Calc
    def saludo():
        return f"Hola, {input.name()}! Bienvenido a Shiny."

    @render.text
    def greeting():
        return saludo()

app = App(app_ui, server)
