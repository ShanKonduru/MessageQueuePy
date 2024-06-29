from EmployeeClass import Employee
from RabbitMQ_Manager import RabbitMQManager

class RabbitMQApp:
    def __init__(self):
        self.manager = RabbitMQManager()

    def setup_queues(self):
        self.manager.declare_queue('string_queue')
        self.manager.declare_queue('employee_queue')

    def send_string_message(self, message):
        self.manager.send_message('string_queue', message)

    def send_employee_message(self, employee):
        employee_message = employee.to_json()
        self.manager.send_message('employee_queue', employee_message)

    def close(self):
        self.manager.close_connection()

def main():
    app = RabbitMQApp()

    # Connect to RabbitMQ
    try:
        app.manager.connect()
    except Exception as e:
        print(f"Could not establish connection: {e}")
        return

    # Setup queues
    app.setup_queues()

    # Send a simple string message
    string_message = "12Hello, World!"
    app.send_string_message(string_message)

    # Create an employee object and send it as JSON
    employee = Employee(1, "John Doe", 30, 50000, "Software Engineer", "IT")
    app.send_employee_message(employee)

    # Close the connection
    app.close()

if __name__ == "__main__":
    main()