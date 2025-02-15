import psycopg2

def enter_data():
    # Establishing the connection
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123",
        host="localhost",
        port="5433"
    )

    print("Connected successfully")

    # Creating a cursor object
    cursor = conn.cursor()

    # Taking user input
    while True:  # Loop until the user provides a unique roll number
        Number = input("Enter Roll No.: ")
        
        # Check if the Number already exists
        cursor.execute("SELECT 1 FROM employees WHERE Number = %s;", (Number,))
        if cursor.fetchone():
            print("ID already exists. Please enter a different Roll No.")
            continue  # Ask for a new roll number
        else:
            break  # Proceed if the ID is unique

    # Taking name and age input
    Name = input("Enter name: ")
    Age = input("Enter age: ")

    # Ensuring 'Age' is an integer
    try:
        Age = int(Age)
    except ValueError:
        print("Please enter a valid number for age.")
        conn.close()
        return

    # Use parameterized queries to avoid SQL injection
    query = '''INSERT INTO employees (Number, Name, Age) VALUES (%s, %s, %s);'''
    cursor.execute(query, (Number, Name, Age))

    print('Data added successfully')

    # Committing the transaction
    conn.commit()

    # Closing the connection
    conn.close()

# Call the function to enter data
enter_data()
