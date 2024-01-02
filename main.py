import random
import pyautogui
import time
import sys


PIXEL_DISTANCE = 1
INTERVAL_SECONDS = 60

def wiggle_mouse():
    screen_width, screen_height = get_screen_dimensions()
    mouse_x, mouse_y = get_current_mouse_location()

    # Generate a random offset
    offset_x = random.randint(-PIXEL_DISTANCE, PIXEL_DISTANCE)
    offset_y = random.randint(-PIXEL_DISTANCE, PIXEL_DISTANCE)

    # Calculate new mouse position
    new_mouse_x = mouse_x + offset_x
    new_mouse_y = mouse_y + offset_y

    # Ensure the new position is within screen bounds
    new_mouse_x = max(100, min(new_mouse_x, screen_width - 100))
    new_mouse_y = max(100, min(new_mouse_y, screen_height - 100))

    pyautogui.moveTo(new_mouse_x, new_mouse_y)

    time.sleep(INTERVAL_SECONDS)


def get_screen_dimensions() -> tuple:
  """
  Returns a list of coordinates in the 
  format [x=1980, y=1080]
  """
  screen = pyautogui.size()
  width = screen[0]
  height = screen[1]
  return width, height


def get_current_mouse_location() -> tuple:
  """
  Returns a list of coordinates in the 
  format [x=1980, y=1080]
  """
  mouse_location = pyautogui.position()
  mouse_x = mouse_location[0]
  mouse_y = mouse_location[1]
  return mouse_x, mouse_y



if __name__ == "__main__":
  print("Welcome to awake. Press Ctrl-c to quit.")
  try:
    while True:
      wiggle_mouse()
      sys.stdout.flush()
  except KeyboardInterrupt:
    print('\n')