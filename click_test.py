import pyautogui
import pygetwindow as gw


print('All windows: '+gw.getAllWindows().__str__())
print('All titles: '+gw.getAllTitles().__str__())
cal = gw.getWindowsWithTitle("Cal")[0]
print(cal.isMaximized)
cal.activate()
cal.resizeTo(1500, 1000)

print(cal.isMaximized)
