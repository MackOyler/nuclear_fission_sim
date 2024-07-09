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

# Font for statistics
font = pygame.font.Font(None, 36)

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
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click to add neutron
                x, y = event.pos
                neutrons.append(create_neutron(x, y))
            elif event.button == 3:  # Right click to add nucleus
                x, y = event.pos
                nuclei.append({"id": len(nuclei), "pos": np.array([x, y], dtype=float), "radius": nucleus_radius})

    # Update neutron positions
    for neutron in neutrons:
        neutron["pos"] += neutron["vel"]
        if neutron["pos"][0] < 0 or neutron["pos"][0] > width:
            neutron["vel"][0] *= -1
        if neutron["pos"][1] < 0 or neutron["pos"][1] > height:
            neutron["vel"][1] *= -1

    # Check for collisions
    neutrons_to_add = []
    nuclei_to_remove = []
    for neutron in neutrons:
        for nucleus in nuclei:
            distance = np.linalg.norm(neutron["pos"] - nucleus["pos"])
            if distance < nucleus_radius + neutron_radius:
                # Collision occurred
                nuclei_to_remove.append(nucleus["id"])
                # Split nucleus and create new neutrons
                for _ in range(3):
                    neutrons_to_add.append(create_neutron(*neutron["pos"]))

    # Remove collided nuclei
    nuclei = [nucleus for nucleus in nuclei if nucleus["id"] not in nuclei_to_remove]

    # Add new neutrons
    neutrons.extend(neutrons_to_add)

    # Draw nuclei
    for nucleus in nuclei:
        pygame.draw.circle(screen, nucleus_color, nucleus["pos"].astype(int), nucleus["radius"])

    # Draw neutrons
    for neutron in neutrons:
        pygame.draw.circle(screen, neutron_color, neutron["pos"].astype(int), neutron["radius"])

    # Display statistics
    num_neutrons = len(neutrons)
    num_nuclei = len(nuclei)
    stats_text = f"Neutrons: {num_neutrons}  Nuclei: {num_nuclei}"
    stats_surface = font.render(stats_text, True, WHITE)
    screen.blit(stats_surface, (10, 10))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
