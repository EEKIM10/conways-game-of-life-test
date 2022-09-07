import click
from random import randint
from typing import Dict


class GameContainer:
    def __init__(self, pretty: bool, width: int, height: int):
        assert width >= 4, "Cannot have a width of less than four"
        assert height >= 4, "Cannot have a height of less than four"
        self.width = width
        self.height = height
        self.pretty = pretty
        self.state: Dict[int, Dict[int, bool]] = {}
        self.generate_initial_rows()

    def generate_initial_rows(self) -> None:
        """Generates initial grid"""
        for y in range(self.height):
            row: Dict[int, bool] = {
                x: False for x in range(self.width)
            }
            self.state[y] = row

        self.state[randint(0, self.height - 1)][randint(0, self.width - 1)] = True  # place a starting pixel

    def render(self) -> str:
        """Renders the current grid state to a human-readable format."""
        if self.pretty:
            chars = {
                True: "O",
                False: " "
            }
        else:
            chars = {
                True: "#",
                False: "+"
            }

        grid = ""
        for y in range(self.height):
            for x in range(self.width):
                grid += chars[self.state[y][x]]
            grid += "\n"
        return grid

    def play(self):
        print(self.render())


@click.command()
@click.option("--pretty", "-P", default=False, is_flag=True)
@click.argument("width", type=int, default=20)
@click.argument("height", type=int, default=10)
def main(pretty: bool, width: int, height: int):
    game = GameContainer(
        pretty,
        width,
        height
    )
    game.play()


if __name__ == '__main__':
    main()
