from main import GameContainer
import pytest


@pytest.mark.parametrize(
    ("width", "height"),
    [
        [x*2, x]
        for x in range(0, 1000, 10)
    ]
)
def test_init(width, height):
    if width < 4 or height < 4:
        with pytest.raises(AssertionError):
            GameContainer(False, width, height)
    else:
        GameContainer(False, width, height)


def test_render():
    game = GameContainer(False, 20, 10)
    game.render()
