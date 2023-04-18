import pandas as pd
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)
email.To = 'jhonatanjonh@outlook.com'
email.Cc = 'jrds.contato@outlook.com'
email.Subject = 'Email de teste'

email.Display()


