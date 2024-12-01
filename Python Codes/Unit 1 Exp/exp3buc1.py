# bucket list Q2

# Implement a Singleton class named DatabaseConnection that ensures only one instance of the class can exist.
# Create a method get_instance that returns the single instance of the class.
# Demonstrate that multiple calls to get_instance return the same instance.
# Concepts Covered: Singleton Pattern

# Extend the DatabaseConnection Singleton class to include a method connect that prints a connection message.
# Demonstrate that only one instance is used even when calling connect from different parts of the program.
# Concepts Covered: Singleton Pattern with Methods

class DatabaseConnection:
    __instance = None

    def __init__(self):
        print("Creating new database connection...")
        self.connection = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = DatabaseConnection()
        return cls.__instance

    def connect(self):
        print("Connecting to database...")
        # database connection code
        self.connection = "Connected!"

# Demonstrate usage
if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")

    conn1 = DatabaseConnection.get_instance()
    conn2 = DatabaseConnection.get_instance()

    conn1.connect()
    conn2.connect()

    print(conn1 is conn2)