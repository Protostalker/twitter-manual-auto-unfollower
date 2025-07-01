import pyautogui
import time
import os
import math

# --- CONFIG ---
image_dir = r"C:\pyscripts"
batch_size = 9  # 👈 Process 9 accounts per cycle
sleep_before_start = 5
refresh_wait = 8
image_confidence = 0.85
clicked_positions = set()

# Bounding box for follower column
Y_MIN = 200
Y_MAX = 950
X_MIN = 800
X_MAX = 1400
position_tolerance = 20

def click_image(image_name, timeout=10, confidence_override=None):
    image_path = os.path.join(image_dir, image_name)
    actual_conf = confidence_override if confidence_override else image_confidence
    print(f"[🔍] Looking for: {image_name} (confidence={actual_conf})")
    start = time.time()

    while time.time() - start < timeout:
        try:
            matches = list(pyautogui.locateAllOnScreen(image_path, confidence=actual_conf))
        except Exception as e:
            print(f"[⚠️] locateAllOnScreen failed: {e}")
            return False

        for match in matches:
            center = pyautogui.center(match)
            if image_name == "unfollow_button.png":
                if not already_clicked(center) and in_target_bounds(center):
                    return click_and_record(center)
            else:
                return click_and_record(center)

        time.sleep(0.5)

    print(f"[⚠️] Couldn't find {image_name}")
    pyautogui.screenshot("failed_step.png")
    print("[📸] Saved screenshot as 'failed_step.png' for debugging.")
    return False

def click_and_record(point):
    print(f"[✅] Clicking at {point}")
    pyautogui.moveTo(point, duration=0.3)
    pyautogui.click()
    clicked_positions.add(point)
    return True

def already_clicked(point):
    return any(math.hypot(p[0] - point[0], p[1] - point[1]) < position_tolerance for p in clicked_positions)

def in_target_bounds(point):
    x, y = point
    return Y_MIN <= y <= Y_MAX and X_MIN <= x <= X_MAX

def unfollow_batch():
    for i in range(batch_size):
        print(f"\n[🔁] Unfollowing account {i + 1}/{batch_size}")
        if click_image("unfollow_button.png"):
            time.sleep(0.8)
            click_image("remove_follower_button.png", timeout=8, confidence_override=0.75)
            time.sleep(0.6)
            click_image("remove_button.png", timeout=8, confidence_override=0.7)
            time.sleep(1)
        else:
            print("[⏭️] Skipping—Unfollow not found or already clicked.")

try:
    while True:
        print(f"\n[⏳] Starting in {sleep_before_start} seconds. Please focus your browser tab!")
        time.sleep(sleep_before_start)
        clicked_positions.clear()
        unfollow_batch()
        print("[🔄] Refreshing page...")
        pyautogui.press('f5')
        print(f"[⏱️] Waiting {refresh_wait} seconds for reload...")
        time.sleep(refresh_wait)

except Exception as e:
    print(f"\n[💥] Script crashed with error:\n{e}")
    input("\n[🧯] Press Enter to exit...")
