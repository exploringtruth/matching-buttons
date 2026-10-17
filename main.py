import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random

from my_sprite_modified import my_sprite
from colliding_object_modified import colliding_object
from moving_vehicle_modified import moving_vehicle
from text_sprite import text_sprite
from initialize_game import initialize_game
from map import map
from keyboard_mover import keyboard_mover
from puzzle_manager import puzzle_manager
from game_controller import game_controller


def create_decorative_sprites():
    background = my_sprite("background/game_bg.png", (0, 0))
    decoration_one = my_sprite("decorations/alien.png", (40, 20), size=(50, 50))
    decoration_two = my_sprite("decorations/star.png", (120, 20), size=(50, 50))
    decoration_three = my_sprite("decorations/star.png", (1052, 20), size=(50, 50))
    decoration_four = my_sprite("decorations/alien.png", (1132, 20), size=(50, 50))
    return [background, decoration_one, decoration_two, decoration_three, decoration_four]


def create_colliding_objects(button_files, y_slots):
    left_y_slots = y_slots.copy()
    right_y_slots = y_slots.copy()
    random.shuffle(left_y_slots)
    random.shuffle(right_y_slots)

    pairs = []
    buttons = []
    grey_image = "buttons/grey_button.png"

    for i, color_path in enumerate(button_files):
        left_btn = colliding_object(color_path, loc=(275, left_y_slots[i]), size=(50, 50), other_image_fname=grey_image)
        right_btn = colliding_object(color_path, loc=(875, right_y_slots[i]), size=(50, 50), other_image_fname=grey_image)
        left_btn.set_active_state(False)
        right_btn.set_active_state(False)
        pairs.append((left_btn, right_btn))
        buttons.extend([left_btn, right_btn])

    return pairs, buttons


def create_vehicles():
    left_hand = moving_vehicle("hands/left_hand.png", loc=(500, 400), size=(90, 90), other_image_fname="hands/left_hand_click.png")
    right_hand = moving_vehicle("hands/right_hand.png", loc=(600, 400), size=(90, 90), other_image_fname="hands/right_hand_click.png")
    return left_hand, right_hand


def handle_input(left_hand_kb, right_hand_kb, controller):
    if controller.game_won:
        if pygame.key.get_pressed()[pygame.K_r]:
            controller.reset_game()
        return

    left_hand_kb.update()
    right_hand_kb.update()


def handle_collisions(controller, dt):
    if controller.game_won:
        return

    controller.puzzle.update(controller.left_hand, controller.right_hand, dt)
    if controller.puzzle.is_complete():
        controller.game_won = True


def draw_objects(game_map, controller):
    game_map.update(controller.get_render_list())


def main():
    game_window = initialize_game(caption="Matching Buttons")
    clock = pygame.time.Clock()
    game_map = map(game_window.screen)

    decorations = create_decorative_sprites()
    win_background = my_sprite("background/win_bg.png", (0, 0), size=(1200, 800))
    restart_text = text_sprite("Press R to Restart", size=36, color=(255, 255, 255), loc=(452.5, 500))

    left_hand, right_hand = create_vehicles()
    left_hand_kb = keyboard_mover(left_hand, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_SPACE)
    right_hand_kb = keyboard_mover(right_hand, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_RETURN)

    button_files = [
        "buttons/blue_button.png",
        "buttons/green_button.png",
        "buttons/orange_button.png",
        "buttons/red_button.png",
        "buttons/yellow_button.png",
    ]
    y_slots = [80 + (i * 135) for i in range(len(button_files))]

    puzzle = puzzle_manager([], required_time=3.0)
    controller = game_controller(
        button_files,
        y_slots,
        decorations,
        win_background,
        restart_text,
        left_hand,
        right_hand,
        puzzle,
        create_colliding_objects,
    )

    running = True
    while running:
        dt = clock.tick(120) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input(left_hand_kb, right_hand_kb, controller)
        handle_collisions(controller, dt)
        draw_objects(game_map, controller)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
