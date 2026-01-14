from textual.app import ComposeResult
from textual.containers import VerticalGroup, Horizontal
from textual.css.query import NoMatches
from textual.events import Resize
from textual.screen import ModalScreen
from textual.widgets import Label


class TooSmallScreen(ModalScreen[None]):
    MODAL = True
    DEFAULT_CSS = """
    TooSmallScreen {
        width: 100%;
        height: 100%;
        dock: left;
        background: $background;

        #msg-column {
            width: 100%;
            height: 7;
            dock: top;
            align: left top;
            background: $background;
            border: round $error;
            padding: 1 2;
            margin: 1;
        }

        #msg-row-dynamic {
            height: auto;
        }

        #msg-err, #msg-dash, #msg-size, #msg-scale {
            color: $error-lighten-1;
            text-style: bold;
        }
    }
    """

    def __init__(self, min_height, min_width, width=None, height=None, **kwargs):
        super().__init__(**kwargs)
        self.min_height = min_height
        self.min_width = min_width
        self._pending_width = width
        self._pending_height = height

    def on_mount(self):
        """Updates the labels with the current terminal size when the screen is mounted."""
        self._update_labels()

    def on_show(self):
        """Updates the labels when the screen becomes visible."""
        self._update_labels()

    def on_resize(self, event: Resize) -> None:
        """Handles terminal resize events and updates the modal labels accordingly."""
        self.set_size(event.size.width, event.size.height)

    def compose(self) -> ComposeResult:
        with VerticalGroup(id="msg-column"):
            with Horizontal(id="msg-row-dynamic"):
                yield Label("Current window size is too small", id="msg-err")
                yield Label(" – ", id="msg-dash")
                yield Label("Awaiting live update values", id="msg-size")
            yield Label("Either resize the window or change scale using CTRL and +/-", id="msg-scale")

    def set_size(self, width, height):
        """Sets the current terminal size for display and updates the labels if mounted."""
        self._pending_width = width
        self._pending_height = height
        if self.is_mounted:
            self._update_labels()

    def _update_labels(self):
        """Updates the error and size labels displayed in the modal."""
        width = self._pending_width or 0
        height = self._pending_height or 0
        try:
            msg_err = self.query_one("#msg-err", expect_type=Label)
            msg_size = self.query_one("#msg-size", expect_type=Label)
            msg_err.update(
                f"Please, resize to at least {self.min_width} × {self.min_height}"
            )
            msg_size.update(
                f"Current size: {width} × {height}\n"
            )
        except NoMatches:
            pass