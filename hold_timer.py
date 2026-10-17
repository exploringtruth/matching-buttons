class hold_timer:
    def __init__(self, required_time=3.0):
        self.required_time = required_time
        self.reset()

    def reset(self):
        self.hold_timer = 0.0
        self.active_holding_pair = None

    def update(self, is_holding_both, current_matched_pair, dt):
        if is_holding_both and current_matched_pair:
            if current_matched_pair == self.active_holding_pair:
                self.hold_timer += dt
                if self.hold_timer >= self.required_time:
                    self.reset()
                    return True
            else:
                self.hold_timer = 0.0
                self.active_holding_pair = current_matched_pair
        else:
            self.reset()

        return False

    def get_progress_ratio(self):
        return min(self.hold_timer / self.required_time, 1.0)
