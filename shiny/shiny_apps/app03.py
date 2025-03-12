from shiny import App, reactive, render, ui

app_ui = ui.page_fixed(
    ui.h1("Contador con Botón"),
    ui.input_action_button("count_btn", "Haz clic para contar"),
    ui.output_text_verbatim("counter_display"),
)

def server(input, output, session):
    counter_value = reactive.Value(0)

    @reactive.Effect
    @reactive.event(input.count_btn)
    def update_counter():
        counter_value.set(counter_value.get() + 1)

    @render.text
    def counter_display():
        return f"Has hecho clic {counter_value.get()} veces."

app = App(app_ui, server)
