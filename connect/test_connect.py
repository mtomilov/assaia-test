import pytest

from .connect import CONNECTIONS, Connect, InvalidMove, Symbol

# TODO: add tests


@pytest.mark.parametrize("player", Symbol)
def test_win(player: Symbol) -> None:
    connect = Connect()
    for _ in range(CONNECTIONS):
        assert not connect.won()
        connect.drop(player, 0)
    assert connect.won()


@pytest.mark.parametrize("player", Symbol)
def test_not_win(player: Symbol) -> None:
    connect = Connect()
    for _ in range(CONNECTIONS - 1):
        assert not connect.won()
        connect.drop(player, 0)
    assert not connect.won()


@pytest.mark.parametrize("player", Symbol)
def test_invalid_move(player: Symbol) -> None:
    connect = Connect()
    with pytest.raises(InvalidMove):
        connect.drop(player, -1)
    with pytest.raises(InvalidMove):
        connect.drop(player, connect.width + 1)
