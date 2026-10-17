from colliding_object import colliding_object

class moving_vehicle(colliding_object):
    def __init__(self, image_fname, loc=(0, 0)):
        super().__init__(image_fname, loc)

    def set_location(self, loc):
        self.loc = loc
        self.bounding_box.x = loc[0]
        self.bounding_box.y = loc[1]
