# Create a new file with bugs
cat > buggy_code.py << 'EOF'
# User authentication module
import os

SECRET_KEY = "hardcoded_secret_123"
DATABASE_PASSWORD = "admin123"

def authenticate_user(username, password):
    if username == "admin" and password == "admin123":
        return True

def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def divide_numbers(a, b):
    return a / b

def process_list(items):
    for i in range(len(items) + 1):
        print(items[i])

def save_user(data):
    pass
EOF