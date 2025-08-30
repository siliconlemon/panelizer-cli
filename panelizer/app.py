from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static, Input
from textual.containers import Vertical
from panelizer.interface import panelize_from_ui

# Mock implementation

class Panelizer(App):
    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Input(placeholder="Input folder path", id="input_path"),
            Input(placeholder="Output folder path (default: output/)", id="output_path"),
            Button("Start Panelizing", id="start_btn"),
            Static(id="log_output"),
        )
        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start_btn":
            input_path = self.query_one("#input_path").value
            output_path = self.query_one("#output_path").value or "output"
            log_widget = self.query_one("#log_output")

            try:
                count = panelize_from_ui(input_path, output_path)
                log_widget.update(f"✅ Processed {count} image(s) into panels.")
            except Exception as e:
                log_widget.update(f"❌ Error: {e}")


def run():
    Panelizer().run()

def cli_entry():
    Panelizer().run()