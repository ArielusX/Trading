import MetaTrader5 as mt5
import pandas as pd

if authorized:
    account_info=mt5.account_info()
    if account_info!=None:
        # mostramos como son los datos sobre la cuenta
        print(account_info)
        # mostramos los datos sobre la cuenta comercial en forma de diccionario
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
        print()
 
       # transformamos el diccionario en DataFrame y lo imprimimos
        df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
        print("account_info() as dataframe:")
        print(df)
else:
    print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())
 
# finalizamos la conexión con el terminal MetaTrader 5
mt5.shutdown()