import MetaTrader5 as mt5

# Establecer conexión con la terminal
if not mt5.initialize():
    print("ERROR")
    quit()
 

account=65051129
password="ixech2ac"
server="MetaQuotes-Demo"

authorized=mt5.login(account, password,server)

if authorized:
  print("Autorizado")
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
 
mt5.shutdown()

