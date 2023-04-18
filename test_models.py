from appcoins.models import ALLCoinApiIo
from appcoins.config import APIKEY

def test_allcoin():
    todo = ALLCoinApiIo()
    assert isinstance(todo, ALLCoinApiIo)
    todo.getAllCoins(APIKEY)
    total = len(todo.lista_criptos) + len(todo.lista_no_criptos)
    assert total == 16379
