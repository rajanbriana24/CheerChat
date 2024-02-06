# -*- coding: utf-8 -*-
import pandas as pd
import json

# Load JSON data
with open('/content/drive/MyDrive/Colab Notebooks/sml_project_data.json', 'r') as file:
    json_data = json.load(file)

# Extract intents data
data = json_data["intents"]

# Create DataFrame
df = pd.DataFrame(data)

# Unique tags
print(df['tag'].unique())

# Display first row
print(df.loc[0])

# Create empty DataFrame for training data
train_df = pd.DataFrame(columns=df.columns)

# Iterate over DataFrame rows
for row in df.itertuples():
    # Iterate over patterns and responses
    for pattern in row[2]:
        for response in row[3]:
            new_row = pd.Series({'tag': row[1], 'patterns': pattern, 'responses': response})
            # Append the new row to the train_df
            train_df = train_df.append(new_row, ignore_index=True)

# Unique tags in train_df
print(train_df['tag'])

# Fill NaN values
train_df.fillna("", inplace=True)

# Display train_df
print(train_df)

# Prepare input text for training
input_text = []
for _, row in train_df.iterrows():
    prompt = 'You are a helpful chatbot named CheerChat. You talk with people and help them with their mental issues. \
    Below is an input received from a user. Write a response in a friendly and cheerful tone.'
    user_input = str(row['patterns'])
    response = str(row['responses'])
    text = prompt + '### User input: ' + user_input + '\n### Response: ' + response
    input_text.append(text)
train_df.loc[:, "text"] = input_text

# Display train_df with text column
print(train_df)

# Save DataFrame to CSV
file_path = 'data_train.csv'
train_df.to_csv(file_path, index=False)  # Set index=False to exclude the DataFrame's index in the CSV
print(f'DataFrame saved to {file_path}')
