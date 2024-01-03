import os
import pandas as pd





data = {
    "Date": ["29-12-2023", "30-12-2023", "31-12-2023"],
    "Temperature": [5,3,-5],
    "Weather Condition": ["Sunny", "Cloudy", "Snow"],
    "Location": ["Ljubljana", "Maribor", "Ljubljana"]
}

weather_df = pd.DataFrame(data)
print(weather_df)
print("nothing")