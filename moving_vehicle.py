from colliding_object import colliding_object

class moving_vehicle(colliding_object):
    def __init__(self, image_fname, loc=(0,0), size=None, other_image_fname=None):
        super().__init__(image_fname, loc, size, other_image_fname)
        self.default_loc = loc

    def set_location(self, loc):
        self.loc = loc
        self.bounding_box.x = loc[0]
        self.bounding_box.y = loc[1]

    def set_default_location(self):
        self.set_location(self.default_loc)
