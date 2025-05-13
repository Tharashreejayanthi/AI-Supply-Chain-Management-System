import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import random
import time
import hashlib

# Demand Forecasting
data = {'Month': [1, 2, 3, 4, 5, 6], 'Sales': [120, 150, 170, 200, 220, 260]}
df = pd.DataFrame(data)
model = LinearRegression()
model.fit(df[['Month']], df['Sales'])
future = pd.DataFrame({'Month': [7, 8, 9]})
predictions = model.predict(future)
print("Predicted Sales:", predictions)

plt.plot(df['Month'], df['Sales'], label='Actual')
plt.plot(future['Month'], predictions, label='Forecast', linestyle='--')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.title('Demand Forecasting')
plt.show()

# IoT Simulation
def simulate_iot_event():
    event = {
        'timestamp': time.time(),
        'temperature': round(random.uniform(10.0, 30.0), 2),
        'humidity': round(random.uniform(40.0, 80.0), 2),
        'device_id': f'Device-{random.randint(1, 10)}'
    }
    return event

for _ in range(5):
    event = simulate_iot_event()
    print(f"Received IoT data: {event}")
    time.sleep(1)

# Chatbot System
responses = {
    'order status': "Your order is currently being processed and will ship soon.",
    'delay': "We apologize for the delay. We're actively resolving the issue.",
    'invoice': "Your invoice has been emailed to the registered address.",
    'default': "I'm sorry, could you please clarify your request?"
}

def chatbot(query):
    for keyword in responses:
        if keyword in query.lower():
            return responses[keyword]
    return responses['default']

while True:
    user_input = input("Vendor: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    print("Bot:", chatbot(user_input))

# Transaction Security Hash
def secure_transaction(transaction_id, amount, vendor):
    record = f"{transaction_id}|{amount}|{vendor}"
    hash_object = hashlib.sha256(record.encode())
    return hash_object.hexdigest()

transaction_hash = secure_transaction("TX12345", 1000, "VendorA")
print("Transaction Hash:", transaction_hash)
