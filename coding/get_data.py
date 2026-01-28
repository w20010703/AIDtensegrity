import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pyjoycon import JoyCon, get_R_id
import numpy as np
import time


# Get the Joy-Con controller
joycon_id = get_R_id()
print("joycon_id: ", joycon_id)
joycon = JoyCon(*joycon_id)

# Initialize lists to store the acceleration data
x_data, y_data, z_data, time_data = [], [], [], []
start_time = None

def update(frame):
    global start_time
    status = joycon.get_status()
    x = status["accel"]["x"]
    y = status["accel"]["y"]
    z = status["accel"]["z"]

    # Record the start time
    if start_time is None:
        start_time = 0

    # Calculate the time elapsed since the start
    start_time += 1

    # Compute the magnitude of acceleration
    magnitude = np.sqrt(x**2 + y**2 + z**2)

    # Append data for plotting
    time_data.append(start_time)
    x_data.append(magnitude)

    # Clear the current plot
    plt.cla()

    # Plot the magnitude of acceleration
    plt.plot(time_data, x_data, label='accel')

    # Add legend and labels
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration')
    plt.title('Real-time Acceleration Magnitude')

# Create an animation
ani = FuncAnimation(plt.gcf(), update, interval=100)

plt.show()




















