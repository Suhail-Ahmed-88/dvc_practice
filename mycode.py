import os
import pandas as pd

# Step 1: Create a sample dataset in dictionary format
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Step 2: Convert dictionary to DataFrame
df = pd.DataFrame(data_dict)

# Step 3: Create a folder named 'data' (use exist_ok=True to avoid errors if it exists)
folder_name = 'data'
os.makedirs(folder_name, exist_ok=True)

# Step 4: Save the DataFrame as CSV inside the 'data' folder
file_path = os.path.join(folder_name, 'sample_data.csv')
df.to_csv(file_path, index=False)

print(f"✅ Dataset saved successfully at: {file_path}")
