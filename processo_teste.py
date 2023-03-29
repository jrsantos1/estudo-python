data_ref = '20232703'

import time, glob, os, shutil
import pandas as pd
from datetime import datetime, timedelta


# PART 1

target_dir = 'C:/code/estudos/python/fundamentos/manipulacao_de_arquivos/arquivos' + data_ref + '/'
start = time.time()

pd.set_option('display.max_columns', 540)
pd.set_option('display.max_row', 30)
pd.options.display.float_format = '{0:,.2f}'.format
file_dir = 'C:/code/estudos/python/fundamentos/manipulacao_de_arquivos/arquivos/'

# PART 2

os.chdir(file_dir)
files = glob.glob('PESSOAS.*')
files.sort(key=os.path.getmtime, reverse=True)
file=files[0]

print(f"getting file {file}")

new_file = target_dir + file

file_exists = os.path.isfile(new_file)
if file_exists:
    print('File already exists')
else:
    print("deu ruim, copiando arquivo")
    shutil.copy(file, target_dir)
    print("file copied")