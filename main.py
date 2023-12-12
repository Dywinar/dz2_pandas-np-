import pandas as pd
data = pd.read_csv('/content/Customers.csv', sep = ';')
print(data[(data['Age'] > 30 ) & (data['Income'] < 30000)])
print(data[(data['Profession'] == 'Lawyer' ) & (data['Work Experience'] > 5)])
