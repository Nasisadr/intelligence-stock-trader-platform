import tkinter as tk
from tkinter import *

OPTIONS = [
'BTC-GBP','ETH-GBP','USDT-GBP','BNB-GBP','USDC-GBP','XRP-GBP',
			'DOGE-GBP','ADA-GBP','MATIC-GBP','DOT-GBP','DAI-GBP','LTC-GBP',
			'SOL-GBP','TRX-GBP','HEX-GBP','UNI7083-GBP','AVAX-GBP','LINK-GBP'
			,'ATOM-GBP','XMR-GBP','CVNA','GME','RXDX','BYND','SAVA','AMC','MOMO','RENT','TSLA','AI',
			'BILI','MYSZ','EXPR','NUWE','ASML','ATOS','ZIM','CRM','RIG','GSL','AVCT',
			'MULN','BTI','GOCO','MBLY','VRM','MTB','EVGO','LULU','LVS','AAPL'
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
   return(variable.get())

button = Button(master, text="OK", command=ok)
button.pack()



mainloop()
