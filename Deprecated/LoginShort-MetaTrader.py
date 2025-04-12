import MetaTrader5 as mt5

# Establecer conexión con la terminal
if not mt5.initialize():
    print("ERROR")
    quit()

def login():
     # Inicializar MetaTrader 5
    if not mt5.initialize():
        print("Error al inicializar MetaTrader 5:", mt5.last_error())
    return
 

account=5035129631
password="LbV@Tq0g"
inversor="!gBe1fFh"
server="MetaQuotes-Demo"

authorized=mt5.login(account, password,server)

if authorized:
  print("Autorizado")
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
 
mt5.shutdown()

