# ======================== game.py ========================

from config import (
    GRAVITY,
    JUMP_VELOCITY,
    PIPES,
    PIPE_SPEED,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    bird_dict,
    BIRD_SIZE,
    PIPE_WIDTH,
    PIPE_HEIGHT,
)

# ======================== PARTIE 3.1 ========================
# TODO : Gérer la gravité
# - Ajouter GRAVITY à la vitesse verticale de l’oiseau (vel_y)
# - Mettre à jour la position verticale de l’oiseau avec vel_y
# - Cela simule la chute progressive de l’oiseau


def apply_gravity():
    bird_dict["vel_y"] += GRAVITY
    bird_dict["y"] += bird_dict["vel_y"]


# ======================== PARTIE 3.2 ========================
# TODO : Sauter
# - Quand l’utilisateur appuie sur une touche, l’oiseau saute
# - Pour cela, on remet sa vitesse verticale à 0
# - Puis on applique JUMP_VELOCITY (valeur négative) pour le faire monter


def jump():
    bird_dict["vel_y"] = JUMP_VELOCITY


# ======================== PARTIE 3.3 ========================
# TODO : Déplacer les tuyaux
# - Pour créer l’illusion que l’oiseau avance, les tuyaux doivent défiler vers la gauche
# - Pour chaque tuyau, réduire sa position x de PIPE_SPEED


def move_pipes():
    for pipe in PIPES:
        pipe["x"] -= PIPE_SPEED


# ======================== PARTIE 3.4 ========================
# TODO : Supprimer les tuyaux hors écran
# - Quand un tuyau sort complètement de l’écran à gauche, on le retire de la liste PIPES
# - Cela permet d’optimiser les performances


def remove_offscreen_pipes():
    for pipe in PIPES[:]:
        if pipe["x"] + PIPE_WIDTH < 0:
            PIPES.remove(pipe)


# ======================== PARTIE 3.5 ========================
# TODO : Détection de collision
# - Créer un rectangle (x, y, largeur, hauteur) autour de l’oiseau
# - Pour chaque tuyau, créer aussi un rectangle
# - Si ces rectangles se chevauchent, il y a collision → retourner True
# - Si l’oiseau touche le sol ou sort de l’écran par le haut → retourner aussi True


def check_collision():
    bird_rect = (bird_dict["x"], bird_dict["y"], BIRD_SIZE[0], BIRD_SIZE[1])

    for pipe in PIPES:
        pipe_rect = (pipe["x"], pipe["y"], PIPE_WIDTH, PIPE_HEIGHT)
        if rects_collide(bird_rect, pipe_rect):
            return True

    #
    floor_y = SCREEN_HEIGHT - 112
    if bird_dict["y"] + BIRD_SIZE[1] >= floor_y or bird_dict["y"] < 0:
        return True

    return False


# Fonction utilitaire pour tester la collision entre deux rectangles
# (Ne pas modifier cette fonction)
def rects_collide(r1, r2):
    return not (
        r1[0] + r1[2] < r2[0]
        or r1[0] > r2[0] + r2[2]
        or r1[1] + r1[3] < r2[1]
        or r1[1] > r2[1] + r2[3]
    )


# ======================== PARTIE 3.6 ========================
# TODO : Mise à jour du score
# - Pour chaque tuyau :
#     - Si l’oiseau a dépassé le tuyau (son x est à droite du tuyau)
#     - Et que le tuyau n’a pas encore été « compté » (passed == False)
#     - Alors marquer le tuyau comme passé, et ajouter 0.5 points au score
# - Chaque paire de tuyaux vaut 1 point (0.5 pour haut, 0.5 pour bas)


def update_score():
    for pipe in PIPES:
        if bird_dict["x"] > pipe["x"] and not pipe["passed"]:
            pipe["passed"] = True
            bird_dict["score"] += 0.5
