import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (x + 3) ** 2

def grad_func(x):
    return 2 * (x + 3)

def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    x_history = [x]
    for _ in range(num_iterations):
        gradient = grad_func(x)
        x = x - learning_rate * gradient
        x_history.append(x)
    return x, x_history

starting_point = 2
learning_rate = 0.1
num_iterations = 20

final_x, x_history = gradient_descent(starting_point, learning_rate, num_iterations)

print(f"Final x value after {num_iterations} iterations: {final_x}")
print(f"Minimum value of the function: {func(final_x)}")

x_vals = np.linspace(-10, 5, 100)
y_vals = func(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='y = (x + 3)^2')
plt.scatter(x_history, [func(x) for x in x_history])
plt.plot(x_history, [func(x) for x in x_history], linestyle='dashed')
plt.title('Gradient Descent to Find Local Minima')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
