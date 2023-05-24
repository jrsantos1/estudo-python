import pandas as pd

data_frame_1 = pd.DataFrame(data={'torcedores': [20000, 1000, 100], 'vendas': [200, 300, 400]}, index=['sao paulo', 'santos','francisco'])
data_frame_2 = pd.DataFrame(data={'torcedores': [10, 0, 0], 'vendas': [0, 0, 0]}, index=['sao paulo', 'santos', 'francisco'])

print(data_frame_1 + data_frame_2)


for index, row in data_frame_1.iterrows():
    for row_column, row_value in row.items():
        data_frame_2.at[index, row_column] = row_value

print(data_frame_2)