import math
from datetime import datetime

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Read data from the CSV files
data1 = pd.read_csv('PepsiSales.csv')
data2 = pd.read_csv('SpriteSales.csv')
data3 = pd.read_csv('FantaSales.csv')
data4 = pd.read_csv('RubiconSales.csv')

# Define features and target variable
X1 = data1[['Date/Time', 'Temperature', 'Promotion', 'Customers']]  # Features
y1 = data1['Drinks Sold']  # Target variable

# Extract start time and end time from the Date/Time column
data1['start_time'] = pd.to_datetime(data1['Date/Time'].str.split('-').str[0], format='%a %d/%m/%y %H:%M')
data1['end_time'] = pd.to_datetime(data1['Date/Time'].str.split('-').str[1], format='%H:%M')

# Extract day of week as a numerical value (Monday=0, Sunday=6)
data1['day_of_week'] = pd.to_datetime(data1['Date/Time'].str.split('-').str[0], format='%a %d/%m/%y %H:%M').dt.dayofweek

# Extract start hour and end hour from the time interval
data1['start_hour'] = data1['start_time'].dt.hour
data1['end_hour'] = data1['end_time'].dt.hour

X1 = data1[['Temperature', 'Promotion', 'Customers', 'day_of_week', 'start_hour', 'end_hour']]

# Split the data into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model1 = LinearRegression()
model1.fit(X1_train, y1_train)

# Predict on the test set
y1_pred = model1.predict(X1_test)

# Define features and target variable
X2 = data2[['Date/Time', 'Temperature', 'Promotion', 'Customers']]  # Features
y2 = data2['Drinks Sold']  # Target variable

# Extract start time and end time from the Date/Time column
data2['start_time'] = pd.to_datetime(data2['Date/Time'].str.split('-').str[0], format='%a %d/%m/%y %H:%M')
data2['end_time'] = pd.to_datetime(data2['Date/Time'].str.split('-').str[1], format='%H:%M')

# Extract day of week as a numerical value (Monday=0, Sunday=6)
data2['day_of_week'] = pd.to_datetime(data2['Date/Time'].str.split('-').str[0], format='%a %d/%m/%y %H:%M').dt.dayofweek

# Extract start hour and end hour from the time interval
data2['start_hour'] = data2['start_time'].dt.hour
data2['end_hour'] = data2['end_time'].dt.hour

X2 = data2[['Temperature', 'Promotion', 'Customers', 'day_of_week', 'start_hour', 'end_hour']]

# Split the data into training and testing sets
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model2 = LinearRegression()
model2.fit(X2_train, y2_train)

# Predict on the test set
y2_pred = model2.predict(X2_test)

# Define features and target variable
X3 = data3[['Date/Time', 'Temperature', 'Promotion', 'Customers']]  # Features
y3 = data3['Drinks Sold']  # Target variable

# Extract start time and end time from the Date/Time column
data3['start_time'] = pd.to_datetime(data3['Date/Time'].str.split('-').str[0], format='%a %d/%m/%y %H:%M')
data3['end_time'] = pd.to_datetime(data3['Date/Time'].str.split('-').str[1], format='%H:%M')

# Extract day of week as a numerical value (Monday=0, Sunday=6)
data3['day_of_week'] = pd.to_datetime(data3['Date/Time'].str.split('-').str[0], format='%a %d/%m/%y %H:%M').dt.dayofweek

# Extract start hour and end hour from the time interval
data3['start_hour'] = data3['start_time'].dt.hour
data3['end_hour'] = data3['end_time'].dt.hour

X3 = data3[['Temperature', 'Promotion', 'Customers', 'day_of_week', 'start_hour', 'end_hour']]

# Split the data into training and testing sets
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model3 = LinearRegression()
model3.fit(X3_train, y3_train)

# Predict on the test set
y3_pred = model3.predict(X3_test)

# Define features and target variable
X4 = data4[['Date/Time', 'Temperature', 'Promotion', 'Customers']]  # Features
y4 = data4['Drinks Sold']  # Target variable

# Extract start time and end time from the Date/Time column
data4['start_time'] = pd.to_datetime(data4['Date/Time'].str.split('-').str[0], format='%a %d/%m/%y %H:%M')
data4['end_time'] = pd.to_datetime(data4['Date/Time'].str.split('-').str[1], format='%H:%M')

# Extract day of week as a numerical value (Monday=0, Sunday=6)
data4['day_of_week'] = pd.to_datetime(data4['Date/Time'].str.split('-').str[0], format='%a %d/%m/%y %H:%M').dt.dayofweek

# Extract start hour and end hour from the time interval
data4['start_hour'] = data4['start_time'].dt.hour
data4['end_hour'] = data4['end_time'].dt.hour

X4 = data4[['Temperature', 'Promotion', 'Customers', 'day_of_week', 'start_hour', 'end_hour']]

# Split the data into training and testing sets
X4_train, X4_test, y4_train, y4_test = train_test_split(X4, y4, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model4 = LinearRegression()
model4.fit(X4_train, y4_train)

# Predict on the test set
y4_pred = model4.predict(X4_test)

# Evaluate the model
#mse = mean_squared_error(y_test, y_pred)
#r2 = r2_score(y_test, y_pred)

#print(f'Mean Squared Error: {mse}')
#print(f'R-squared: {r2}')

# Output the model predictions

print("Enter data for a model prediction:")
drink = input("Enter Drink (Pepsi/Sprite/Fanta/Rubicon): ")
if drink == "Pepsi":
    data = data1
    model = model1
elif drink == "Sprite":
    data = data2
    model = model2
elif drink == "Fanta":
    data = data3
    model = model3
else:
    data = data4
    model = model4

dateTime = input("Enter Date/Time (e.g., Mon 01/01/22 15:00-17:00): ")
start_time = pd.to_datetime(dateTime.split('-')[0].strip(), format='%a %d/%m/%y %H:%M')
end_time = pd.to_datetime(dateTime.split('-')[1].strip(), format='%H:%M')

start_hour = start_time.hour
end_hour = end_time.hour
day_of_week = start_time.dayofweek

temperature = int(input("Enter Temperature: "))
promotion = int(input("Enter Promotion (0/1): "))
customers = int(input("Enter Customers: "))

# Convert new_data to DataFrame with appropriate column names
new_data_df = pd.DataFrame([[temperature, promotion, customers, day_of_week, start_hour, end_hour]],
                           columns=['Temperature', 'Promotion', 'Customers', 'day_of_week', 'start_hour', 'end_hour'])

# Predict using the new DataFrame
prediction = model.predict(new_data_df)
print(f"Predicted Drinks Sold: {math.floor(prediction[0])}")
