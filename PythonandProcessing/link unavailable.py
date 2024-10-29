import socket

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print("Server listening on port 12345...")

    while True:
        conn, addr = server.accept()
        print(f"Connection from {addr}")

        while True:  # Keep the connection open for repeated calculations
            data = conn.recv(1024).decode().strip()

            if not data:  # Break if the client disconnects
                print(f"Connection closed by {addr}")
                break

            print("Data received:", data)
            try:
                input1, input2, operation = data.split(",")
                num1 = int(input1)
                num2 = int(input2)
                result = calculate(num1, num2, operation)
                print("Calculation result:", result)  # Displaying result on the server console
                conn.sendall(str(result).encode())
            except ValueError:
                error_message = "Error: Invalid input, please enter two integers."
                print(error_message)
                conn.sendall(error_message.encode())
            except Exception as e:
                error_message = f"Error: {str(e)}"
                print(error_message)
                conn.sendall(error_message.encode())

        conn.close()  # Close the connection to the client after finishing

if __name__ == "__main__":
    start_server()
