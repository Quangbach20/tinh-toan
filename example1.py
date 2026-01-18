from datetime import date


users = [
    {
        "username": "admin",
        "password": "123456",
        "email": "admin@example.com",
        "full_name": "Admin User",
        "active": True,
        "created_at": "2026-01-18 10:00:00",
        "updated_at": "2026-01-18 10:00:00"
    },
    {
        "username": "user",
        "password": "123456",
        "email": "user@example.com",
        "full_name": "User User",
        "active": True,
        "created_at": "2026-01-18 10:00:00",
        "updated_at": "2026-01-18 10:00:00"
    }
]

def display_menu():
    print("1. Login")
    print("2. Register")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "0":
        print("Exit")
        exit()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful")
            return
    print("Login failed")

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")
    full_name = input("Enter your full name: ")
    active = True
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    users.append({
        "username": username,
        "password": password,
        "email": email,
        "full_name": full_name,
        "active": active,
        "created_at": created_at,
        "updated_at": updated_at
    })

    print("Register successful")

while True:
    display_menu()
























    
