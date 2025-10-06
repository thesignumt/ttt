import msvcrt
import os

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
        if not self.slides:
            return
        self.clear()
        print(self.slides[self.index])
        print(f"\n{DARKGRAY}[n] next  |  [p] prev  |  [q] quit{RESET}")

    def run(self) -> None:
        if not self.slides:
            return

        size = len(self.slides)

        l_idx = -1
        while True:
            if self.index != l_idx:
                self.show_slide()
                l_idx = self.index

            match getch():
                case "n" if self.index < size - 1:
                    self.index += 1
                case "p" if self.index > 0:
                    self.index -= 1
                case "q":
                    break
