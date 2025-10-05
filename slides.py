import msvcrt
import os

# ANSI colors
RED = "\033[91m"
CYAN = "\033[96m"
DARKGRAY = "\033[90m"
RESET = "\033[0m"


def getch():
    return msvcrt.getch().decode().lower()


class Slides:
    def __init__(self, slides: list[str]) -> None:
        self.slides = slides
        self.index = 0

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def show_slide(self) -> None:
        self.clear()
        print(self.slides[self.index])
        print(f"\n{DARKGRAY}[n] next  |  [p] prev  |  [q] quit{RESET}")

    def run(self) -> None:
        while True:
            self.show_slide()
            key = getch()
            if key == "n" and self.index < len(self.slides) - 1:
                self.index += 1
            elif key == "p" and self.index > 0:
                self.index -= 1
            elif key == "q":
                break
