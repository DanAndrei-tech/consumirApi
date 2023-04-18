from appcoins.models import AllCoinApiIO,Exchange,ModelError
from appcoins.config import APIKEY
import pytest

def test_allcoin():
    todo = AllCoinApiIO()
    assert isinstance(todo, AllCoinApiIO)
    todo.getAllCoins(APIKEY)
    total = len(todo.lista_criptos) + len(todo.lista_no_criptos)
    assert total == 16379

def test_exchange_ok():
    cambio = Exchange("ETH")
    cambio.updateExchange(APIKEY)
    assert cambio.rate > 0
    assert cambio.rate != None

def test_exchange_error():
    cambio2 = Exchange("ÑIÑO")
    with pytest.raises(ModelError) as exceptionInfo:  
        cambio2.updateExchange(APIKEY)       
    assert str(exceptionInfo.value) == "status: 550, error: You requested specific single item that we don't have at this moment."
    assert cambio2.status_code == 550

