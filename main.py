import pygame
import numpy as np
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nuclear Fission Simulation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Simulation parameters
nucleus_radius = 10
neutron_radius = 3
nucleus_color = RED
neutron_color = WHITE
neutrons = []
nuclei = []

# Initialize nuclei
for i in range(10):
    x = random.randint(nucleus_radius, width - nucleus_radius)
    y = random.randint(nucleus_radius, height - nucleus_radius)
    nuclei.append({"id": i, "pos": np.array([x, y], dtype=float), "radius": nucleus_radius})

# Initialize neutrons
def create_neutron(x, y):
    vx = random.uniform(-2, 2)  # Increased velocity range
    vy = random.uniform(-2, 2)  # Increased velocity range
    return {"pos": np.array([x, y], dtype=float), "vel": np.array([vx, vy], dtype=float), "radius": neutron_radius}

neutrons.append(create_neutron(width // 2, height // 2))

# Main loop
running = True
while running:
    pass

# Update neutron positions

# Check for collisions
    # Collision
    # Split nucleus and create new neutrons

# Remove collided nuclei

# Add new neutrons

# Draw nuclei

# Draw neutrons
