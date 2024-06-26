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