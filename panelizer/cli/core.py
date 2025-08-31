from textual import work
from textual.app import App
from textual_fspicker import SelectDirectory
from pathlib import Path


class PanelizerCli(App[None]):
    CSS_PATH = None
    TITLE = "Panelizer CLI"
    SUB_TITLE = "📸 Split images into gallery panels"

    def __init__(self):
        super().__init__()
        self.selected_input_dir: Path | None = None

    @work
    async def on_mount(self) -> None:
        await self.push_screen_wait(SelectDirectory(location=Path.home() / "Pictures"))
        if self.selected_input_dir:
            self.console.print(f"[green]Selected:[/green] {self.selected_input_dir}")
            self.exit()
        else:
            self.console.print("[red]No directory selected.")
            self.exit()