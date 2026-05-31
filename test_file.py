# test_file.py
def divide(a, b):
    return a / b      # bug: no check for b == 0

def get_user(users, id):
    return users[id]  # bug: no bounds check