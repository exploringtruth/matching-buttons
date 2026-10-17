class game_controller:
    def __init__(self, button_files, y_slots, decorations, win_background, restart_text, left_hand, right_hand, puzzle, create_colliding_objects):
        self.button_files = button_files
        self.y_slots = y_slots
        self.decorations = decorations
        self.win_background = win_background
        self.restart_text = restart_text
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.puzzle = puzzle
        self.create_colliding_objects = create_colliding_objects
        self.game_won = False
        self.reset_game()

    def reset_game(self):
        pairs, buttons = self.create_colliding_objects(self.button_files, self.y_slots)
        self.puzzle.reset(pairs)
        self.buttons = buttons
        self.left_hand.set_default_location()
        self.right_hand.set_default_location()
        self.game_won = False

    def get_play_render_list(self):
        return self.decorations + self.buttons + [self.left_hand, self.right_hand]

    def get_win_render_list(self):
        return [self.win_background, self.restart_text]

    def get_render_list(self):
        if self.game_won:
            return self.get_win_render_list()
        return self.get_play_render_list()
