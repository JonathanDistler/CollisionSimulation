import matplotlib.pyplot as plt

def traject_animation(positions, radius=0.5, x_range=10, y_range=10):
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radius=radius, color='blue')
    ax.add_patch(circle)

    ax.set_xlim(-x_range, x_range)
    ax.set_ylim(-y_range, y_range)
    ax.set_aspect('equal')
    plt.grid(True)

    for pos in positions:
        circle.set_center(pos)
        plt.title(f"Position: ({pos[0]:.2f}, {pos[1]:.2f})")
        plt.pause(0.03)  # Faster update
    plt.show()


def in_boundary(x_position, y_position, radius, x_range, y_range, velocity):
    if x_position + radius >= x_range or x_position - radius <= -x_range:
        velocity[0] = -velocity[0]
    if y_position + radius >= y_range or y_position - radius <= -y_range:
        velocity[1] = -velocity[1]

def kinematics(position, velocity, acceleration, time, radius, x_range, y_range):
    position_x = position[0]
    position_y = position[1]

    # Use the velocity directly and update it as needed
    for t in range(time + 1):
        position_x += velocity[0] + 0.5 * acceleration[0]
        position_y += velocity[1] + 0.5 * acceleration[1]

        traject_pic(position_x, position_y)
        in_boundary(position_x, position_y, radius, x_range, y_range, velocity)

# Call the function
radius = 0.5
x_range = 10
y_range = 10
kinematics([0, 0], [2, 1], [0, 0], 10, radius, x_range, y_range)

#need to make the frame rate refresh all on the same frame
#could also include a coefficient of restitution 
