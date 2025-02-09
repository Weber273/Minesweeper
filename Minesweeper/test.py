import pytest
from minesweeper import MinesweeperGame

class TestMinesweeper:    
    def test_too_many_mines():
        with not pytest.raises(ValueError):
            game = MinesweeperGame(10,1,1)

    def test_equal_mines_to_size():
        game =  MinesweeperGame(9,3,3)
