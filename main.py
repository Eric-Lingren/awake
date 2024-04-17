import os
import random
import pyautogui
import time
import sys

from datetime import datetime
import pytz


PIXEL_DISTANCE = 1
INTERVAL_SECONDS = 60
DISABLE_TIME_HOURS = 17 #1700 pst



def is_working_hours():
  utc_now = datetime.now(pytz.utc)
  pst = pytz.timezone('America/Los_Angeles')
  pst_now = utc_now.astimezone(pst)
  random_minute = random.randint(10, 59)
  five_pm_pst = pst.localize(datetime(pst_now.year, pst_now.month, pst_now.day, DISABLE_TIME_HOURS, random_minute, 0))

  if pst_now < five_pm_pst:
    print(f"It is {pst_now}. \nIt is not after {DISABLE_TIME_HOURS}:{random_minute} PST. \nRunning...\n")
    return True
  else:
    print(f"It is {pst_now}. \nAfter {DISABLE_TIME_HOURS}:{random_minute} PST. \nShutting Down...\n")
    return False


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


def sleep_computer():
  os.system("osascript -e 'tell application \"System Events\" to sleep'")


if __name__ == "__main__":
  print("Welcome to awake. Press Ctrl-c to quit.")
  try:
    while is_working_hours():
      wiggle_mouse()
      sys.stdout.flush()
  except KeyboardInterrupt:
    print('\n')