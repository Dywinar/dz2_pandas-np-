import pandas as pd
data = pd.read_csv('/content/Customers.csv', sep = ';')
data[(data['Age'] > 30 ) & (data['Income'] < 30000)]
data[(data['Profession'] == 'Lawyer' ) & (data['Work Experience'] > 5)]
