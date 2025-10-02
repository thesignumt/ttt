from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static


class TTT(App):
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        with Grid():
            for row in range(3):
                for col in range(3):
                    yield Static(f"Cell ({row}, {col})")


if __name__ == "__main__":
    app = TTT()
    app.run()
