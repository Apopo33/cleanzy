# generate_data.py

import pandas as pd
import random
from faker import Faker

fake = Faker()
random.seed(42)

num_users = 200
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def random_juja_coordinates():
    lat = random.uniform(-1.099, -1.097)      # Latitude range for Juja
    lon = random.uniform(37.010, 37.015)      # Longitude range for Juja
    return lat, lon

data = []

for i in range(num_users):
    lat, lon = random_juja_coordinates()
    data.append({
        'user_id': f"user_{i+1}",
        'apartment': f"Apt_{random.randint(1, 50)}",
        'preferred_day': random.choice(days),
        'latitude': lat,
        'longitude': lon
    })

df = pd.DataFrame(data)
df.to_csv("data/laundry_users.csv", index=False)
print("Dummy data saved to data/laundry_users.csv")
