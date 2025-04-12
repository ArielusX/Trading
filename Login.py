import MetaTrader5 as mt5

account=5035129631
password="LbV@Tq0g"
inversor="!gBe1fFh"
server="MetaQuotes-Demo"

def initialize():
    if not mt5.initialize():
        print("Error al inicializar MetaTrader 5:", mt5.last_error())
        return

    authorized=mt5.login(account, password,server)

    if authorized:
      print("Se ha iniciado sesión correctamente")
    else:
        print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
    




