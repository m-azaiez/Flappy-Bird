# ======================== bird.py ========================

import pygame
from config import BIRD_SIZE, bird_dict, BIRD_X, SCREEN_HEIGHT, LIVES

# ======================== PARTIE 1.1 ========================
# TODO : Charger l’image de l’oiseau et la redimensionner
# - Utiliser pygame.image.load("chemin/vers/image")
# - Redimensionner avec pygame.transform.scale(...)
# - Stocker le résultat dans la variable « bird_img »

bird_img_mid = pygame.transform.scale(pygame.image.load("assets/bluebird-midflap.png"), BIRD_SIZE)

bird_img_up = pygame.transform.scale(pygame.image.load("assets/bluebird-upflap.png"), BIRD_SIZE)

bird_img_down = pygame.transform.scale(pygame.image.load("assets/bluebird-downflap.png"), BIRD_SIZE)

bird_img = bird_img_mid  # Default
bird_images = [bird_img_up, bird_img_mid, bird_img_down]


# ======================== PARTIE 1.2 ========================
# TODO : Initialiser les valeurs dans le dictionnaire « bird_dict »
# - x : position horizontale de départ (utiliser BIRD_X)
# - y : position verticale (centrée dans l’écran)
# - vel_y : vitesse verticale (commence à 0)
# - lives : nombre de vies (utiliser LIVES)
# - score : démarre à 0

bird_dict.update(
    {"x": BIRD_X, "y": SCREEN_HEIGHT // 2, "vel_y": 0, "lives": LIVES, "score": 0}
)
