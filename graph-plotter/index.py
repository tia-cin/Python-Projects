import matplotlib.pyplot as plt

x_lines = int(input("How many lines do you need? "))

def create_graph(x_lines):

    for num in range(0, x_lines):
        x_c = input("Please provide x-axis coordinates (ex. 3-6-8-1): ")
        y_c = input("Please provide y-axis coordinates (ex. 3-6-8-1): ")

        x = x_c.split("-")
        y = y_c.split("-")

        plt.plot(x, y, label = f"Line {num}")

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph")
    plt.legend()

    plt.show()

create_graph(x_lines)