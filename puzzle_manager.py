from hold_timer import hold_timer

class puzzle_manager:
    def __init__(self, button_pairs, required_time=3.0):
        self.required_time = required_time
        self.timer = hold_timer(required_time)
        self.reset(button_pairs)

    def reset(self, button_pairs):
        self.button_pairs = button_pairs
        self.completed_pairs = set()
        self.timer.reset()

    def _is_holding_both(self, left_hand, right_hand):
        return left_hand.get_active_state() and right_hand.get_active_state()

    def _find_matched_pair(self, left_hand, right_hand):
        for pair in self.button_pairs:
            if pair in self.completed_pairs:
                continue
            l_btn, r_btn = pair
            if (left_hand.is_colliding_with(l_btn) and right_hand.is_colliding_with(r_btn)) or \
               (left_hand.is_colliding_with(r_btn) and right_hand.is_colliding_with(l_btn)):
                return pair
        return None

    def update(self, left_hand, right_hand, dt):
        is_holding_both = self._is_holding_both(left_hand, right_hand)
        matched_pair = self._find_matched_pair(left_hand, right_hand)
        completed_this_frame = self.timer.update(is_holding_both, matched_pair, dt)

        if completed_this_frame and matched_pair:
            l_btn, r_btn = matched_pair
            l_btn.set_active_state(True)
            r_btn.set_active_state(True)
            self.completed_pairs.add(matched_pair)

    def is_complete(self):
        return len(self.button_pairs) > 0 and len(self.completed_pairs) == len(self.button_pairs)
