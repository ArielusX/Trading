import MetaTrader5 as mt5
 
# establecemos la conexión con el terminal MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# conectamos con la cuenta comercial sin indicar la contraseña y el servidor
account=5002395715
authorized=mt5.login(account)  # la contraseña se tomará de la base de datos del terminal, si se ha indicado que se guarden los datos de conexión
if authorized:
    print("connected to account #{}".format(account))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
 
# ahora, conectamos con la cuenta comercial indicando la contraseña
account=5002395715
authorized=mt5.login(account, password="ypsyje3g", server="MetaQuotes-Demo")
if authorized:
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
 
# finalizamos la conexión con el terminal MetaTrader 5
mt5.shutdown()