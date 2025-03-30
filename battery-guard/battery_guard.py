# ================================================
# 🧠 PSEUDOCODE + IMPLEMENTATION: Battery Guard
# ================================================

import psutil  # For fetching battery info
import time  # For adding sleep intervals
import os  # For system notifications


def check_battery():
    # 1. CHECK battery info using psutil
    battery = psutil.sensors_battery()

    # 2. IF no battery is found:
    if battery is None:
        # PRINT warning and EXIT
        print("No battery detected—check hardware!")
        return

    # 3. GET current battery percentage, plugged-in state, and estimated time left
    percent = battery.percent
    plugged = battery.power_plugged
    secs_left = battery.secsleft

    # Calculate minutes left (if time estimation is available)
    # Else, show "Unknown"
    mins_left = secs_left // 60 if secs_left > 0 else "Unknown"

    # 4. FORMAT and display important battery statistics
    status = f"Battery: {percent}% | Plugged in: {plugged} | Time left: {mins_left} mins"
    print(status)

    # 5. IF unplugged AND battery < 20%:
    #       SEND system popup alert
    if not plugged and percent < 20:
        os.system(f'msg * "Low battery! Plug in now—only {percent}% left!"')

    # 6. IF charging AND battery < 95%:
    #       PRINT "Charging" status
    elif plugged and percent < 95:
        print("Charging—keep it plugged in.")

    # 7. IF charging AND battery >= 95%:
    #       PRINT "Unplug suggestion"
    elif plugged and percent >= 95:
        print("Fully charged—unplug to save battery cycles.")


if __name__ == "__main__":
    # 8. LOOP every 5 minutes to track battery state continuously
    while True:
        check_battery()
        time.sleep(300)  # Pause execution for 5 minutes (300 seconds)
