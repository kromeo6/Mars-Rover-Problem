'''
We would like you to write a simulation of the movement of a remote-controlled rover on Mars.
The Mars Rover’s movement involves a grid, where the rover's position is represented by a pair of coordinates (x, y) and a cardinal direction 
they face (N, S, E, or W). The rover is controlled by a set of commands: 'L' and 'R' to turn left or right, respectively, and 'M' to move one 
step forward in the direction they are facing.
Model the Mars Rover. Your program should begin by reading in a start location for the rover, it's initial direction, and a sequence of commands 
it will execute. The program should then progress through its implementation by interpreting each command’s meaning, and performing the appropriate action.
For example, if the Mars rover starts at location (1,2), initially facing N, and receives the commands MMLMRMM, it’s execution pattern will look like:
M: The rover will move one square North to (1,3).
M: The rover will move one square North to (1,4).
L: The rover will turn Left to face West.
M: The rover will move one square West to (0,4).
R: The rover will turn Right to face North.
M: The rover will move one square North to (0,5).
M: The rover will move one square North to (0,6).
And so the rover’s final position will be (0,6), facing N.
Given your Mars Rover starts from (5,5) and facing North, where will the Mars rover end after executing the following program: MMLMMRMLLMRMRMMML ?
'''

def rover_movement(coordinates, controls, initial_dir):
  cur_coord = [coordinates[0], coordinates[1]]
  dir_map = {
    'N': 1,
    'E': 2,
    'S': 3,
    'W': 4
  }
  # if we have next direction R, it means we have to add 1 to the current direction
  # if we have L we have to add -1 to the current direction
  cur_dir = dir_map[initial_dir]

  for c in controls:
    if c == 'L':
      cur_dir = cur_dir - 1
      if cur_dir == 0: # in cas previous direction was 1, means North, and we have to turn left it will become 0, which is equivalent of 4
        cur_dir = 4 # so, we are adjusting here
    elif c == 'R':
      cur_dir = cur_dir + 1
      if cur_dir == 5: # udjustment 4 +1 case
        cur_dir = 1
    
    if cur_dir == 3:
      cur_coord[1] = cur_coord[1] - 1
    elif cur_dir == 1:
      cur_coord[1] = cur_coord[1] + 1
    elif cur_dir == 4:
      cur_coord[0] = cur_coord[0] - 1
    else:
      cur_coord[0] = cur_coord[0] + 1

  return cur_coord

      

      

print(rover_movement([0, 1], 'MLRR', 'S'))

