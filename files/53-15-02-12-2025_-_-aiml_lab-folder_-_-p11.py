import numpy as np
import matplotlib.pyplot as plt
# %%
def func(x):
  return (x + 3) ** 2
# %%
def grad_func(x):
  return 2 * (x + 3)
# %%
# Gradient Descent Algorithm
def gradient_descent(starting_point, learning_rate, num_iterations):
 x = starting_point
 x_history = [x] # Keep track of x values for plotting
 for _ in range(num_iterations):
# Calculate gradient
   gradient = grad_func(x)
# Update x by moving against the gradient
   x = x - learning_rate * gradient
# Append the new x value to history
   x_history.append(x)
 return x, x_history
# %%
# Parameters for gradient descent
starting_point = 2 # Starting point x = 2
learning_rate = 0.1 # Learning rate
num_iterations = 20 # Number of iterations
# %%
final_x, x_history = gradient_descent(starting_point, learning_rate,
num_iterations)
# %%
print(f"Final x value after {num_iterations} iterations: {final_x}")
print(f"Minimum value of the function: {func(final_x)}")
# %%
x_vals = np.linspace(-10, 5, 100)
y_vals = func(x_vals)
# %%
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='y = (x + 3)^2', color='blue')
plt.scatter(x_history, [func(x) for x in x_history], color='red',
label='Gradient Descent Path')
plt.plot(x_history, [func(x) for x in x_history], color='red',
linestyle='dashed', alpha=0.6)
plt.title('Gradient Descent to Find Local Minima')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()