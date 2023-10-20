import json
import mysql.connector

# Load the JSON data from your file
with open('intents.json', 'r') as json_file:
    data = json.load(json_file)

# Replace these variables with your MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ai_assistant'
}

# Connect to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Insert 'intents' data into the 'intents' table
for intent in data['intents']:
    tag = intent['tag']
    cursor.execute("INSERT INTO intents (tag) VALUES (%s)", (tag,))
    conn.commit()  # Commit after each insert

    # Get the last inserted intent_id
    intent_id = cursor.lastrowid

    # Insert 'patterns' associated with the intent
    for pattern in intent['patterns']:
        cursor.execute("INSERT INTO intent_data (intent_id, data_type, data_value) VALUES (%s, 'pattern', %s)", (intent_id, pattern))
        conn.commit()  # Commit after each insert

    # Insert 'responses' associated with the intent
    for response in intent['responses']:
        cursor.execute("INSERT INTO intent_data (intent_id, data_type, data_value) VALUES (%s, 'response', %s)", (intent_id, response))
        conn.commit()  # Commit after each insert

# Close the database connection
conn.close()
