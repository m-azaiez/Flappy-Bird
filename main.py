# ======================== main.py ========================

import pygame
import sys

pygame.init()
from config import FPS, bird_dict, PIPES, SCREEN_WIDTH, SCREEN_HEIGHT, BIRD_X, LIVES
from window import draw_window, show_game_over_message, add_pipes
from game import (
    apply_gravity,
    move_pipes,
    remove_offscreen_pipes,
    check_collision,
    update_score,
    jump,
)


clock = pygame.time.Clock()
running = True
game_started = False

# ======================== PARTIE 4.1 ========================
# TODO : Générer une première paire de tuyaux au début du jeu
add_pipes()


# ======================== PARTIE 4.2 ========================
# TODO : Fonction pour recommencer une partie
# - Remettre l’oiseau au centre
# - Réinitialiser vitesse, vies, score
# - Supprimer les anciens tuyaux
# - Ajouter une nouvelle paire


def restart_game():
    global game_started
    bird_dict["x"] = BIRD_X
    bird_dict["y"] = SCREEN_HEIGHT // 2
    bird_dict["vel_y"] = 0
    bird_dict["lives"] = LIVES
    bird_dict["score"] = 0
    PIPES.clear()
    add_pipes()
    game_started = False


# ======================== PARTIE 4.3 ========================
# TODO : Boucle principale du jeu
# - Appliquer la gravité
# - Gérer les événements clavier :
#     - Espace pour sauter
#     - R pour recommencer quand perdu
# - Vérifier les collisions
# - Générer une nouvelle paire de tuyaux régulièrement
# - Mettre à jour le score
# - Afficher le jeu (appel à draw_window)

while running:
    clock.tick(FPS)

    # ======================== PARTIE 5.4 ========================
           # TODO : Boucle d'événements (clavier + fermeture fenêtre)
    # - Parcourir les événements Pygame avec pygame.event.get()
    # - Si l'utilisateur ferme la fenêtre (pygame.QUIT), mettre running = False
    # - Si une touche est pressée (pygame.KEYDOWN) :  
    #     - Si la partie est terminée (bird_dict["lives"] <= 0) et que la touche est R (pygame.K_r) :
    #           appeler restart_game()
    #     - Sinon, si la touche est ESPACE (pygame.K_SPACE) et que l'oiseau a encore des vies :
    #           appeler jump()
    #
    # TODO : Gestion de l'état "Game Over"
    # - Si bird_dict["lives"] <= 0 :
    #     - afficher le message show_game_over_message()
    #     - ignorer le reste de la boucle (utiliser continue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if bird_dict["lives"] <= 0:
                if event.key == pygame.K_r:
                    restart_game()
            else:
                if event.key == pygame.K_SPACE:
                    if not game_started:
                        game_started = True
                    jump()

    # Gestion de l'état "Game Over"
    if bird_dict["lives"] <= 0:
        show_game_over_message()
        continue

    if game_started:
        if check_collision():
            bird_dict["lives"] -= 1
            if bird_dict["lives"] > 0:
                # Reset bird position and pipes for the next life
                bird_dict["x"] = BIRD_X
                bird_dict["y"] = SCREEN_HEIGHT // 2
                bird_dict["vel_y"] = 0
                PIPES.clear()
                add_pipes()
                game_started = False

        apply_gravity()
        move_pipes()
        remove_offscreen_pipes()
        update_score()

        # TODO : Générer une nouvelle paire si le dernier tuyau est suffisamment avancé
        if len(PIPES) > 0:
            if PIPES[-1]["x"] < SCREEN_WIDTH - 300:
                add_pipes()

    draw_window()

pygame.quit()
sys.exit()
