from random import choice

class RandomWalk:
    def __init__(self, num_points=5000) -> None:
        self.num_points = num_points
        self.distances = [0, 1, 2, 3, 4]

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        
        #  Keep taking steps until the desired length is reached
        while len(self.x_values) < self.num_points:
            
            # Decide which direction and how far to go
            x_step = self.get_step()
            y_step = self.get_step()
            
            # Reject steps that do not move along either axis
            if x_step == 0 and y_step == 0:
                continue
            
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
    
    def get_step(self):
        direction = choice([1, -1])
        distance = choice(self.distances)
        return direction * distance
            