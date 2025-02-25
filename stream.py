import time
import random
import threading
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

# Danh sách các liên kết
link_list = [
"https://streamtape.com/v/r8d7y1gbg2ib22J/OND18002.mp4",
"https://streamtape.com/v/q9MAlR7JyKHzVP3/BOYST0247.mp4",
"https://streamtape.com/v/XkqbbZeW7WuDY3Z/TikTok_Id_taka2003cter_2025_01_27_15_44_57.mp4",
"https://streamtape.com/v/oWeGQMq7MKFJJyY/TikTok_Id_abskwkws_2025.02.13_07-26-15.mp4",
"https://streamtape.com/v/vDpjlyaGoPtD14/HAPPY_NEW_YEAR_ASIAN_Lunar_New_Year_BIG_UPDATE.%EF%BF%BD%EF%BF%BDSTRAIGHT_07.mp4",
"https://streamtape.com/v/jaK9zOOZyzUzeZD/NEW_CLIP_UPDATE_FUCK_STRAIGH_GUY_TK1107.mp4",
    "https://streamtape.com/v/8BdO9Mweaztog0j/TK_taka2003cter_2025.02.15_14-45-52.mp4",
    "https://streamtape.com/v/29aKmLYQ8KSWgB/TikTok_Id_inuya299_2025.02.16_14-36-24.mp4",
    "https://streamtape.com/v/8vBl161rowT8jm/TikTok_Id_inuya299_2025_02_07_14_54_05.mp4",
    "https://streamtape.com/v/VBQXaqQdPOTKrRp/TikTok_Id_inuya299_2025_02_02_14_42_51.mp4",
    "https://streamtape.com/v/llJbWp2epRC7MDA/TikTok_Id_inuya299_2025_02_03_14_34_25.mp4",
    "https://streamtape.com/v/pddmwejLLaFrovV/TikTok_Id_inuya299_2025_02_08_14_47_29.mp4",
    "https://streamtape.com/v/pddmwejLLaFrovV/TikTok_Id_inuya299_2025_02_08_14_47_29.mp4"
]
email_list = [
    ("duongbaotinqom3nqsusfs0@rotitk.us", "Phan9999"),
    ("tranbaohuynhay6v94ndq1u1@rotitk.us", "Phan9999"),
    ("lacthanhmaihozztj4te88d@rotitk.us", "Phan9999"),
    ("uathuyhoangejh1uph3trh1@rotitk.us", "Phan9999"),
    ("ngotuanngocozybfuvcohqw@rotitk.us", "Phan9999"),
    ("lacthanhmaihozztj4te88d@rotitk.us", "Phan9999"),
    ("dangminhdanqqsq1cy5p4lc@rotitk.us", "Phan9999"),
    ("huynhnamtu5dru7vzjsuxm@rotitk.us", "Phan9999"),
    ("ngohieuphong8mx04c4nyqu1@rotitk.us", "Phan9999"),
    ("phamthienanmyw9yn1bqbka@rotitk.us", "Phan9999"),
    ("tonghoangphat0t6efwjfjx3w@rotitk.us", "Phan9999"),
]

time.sleep(random.uniform(60, 120))
# Lựa chọn 3 liên kết ngẫu nhiên
selected_links = random.sample(link_list, 1)

# Khởi tạo driver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")
options.add_argument('--start-maximized')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

driver = uc.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Di chuyển chuột ngẫu nhiên
def random_mouse_move():
    try:
        window_width = driver.execute_script("return window.innerWidth;")
        window_height = driver.execute_script("return window.innerHeight;")
        action = ActionChains(driver)
        x_offset = random.randint(-window_width//2, window_width//2)
        y_offset = random.randint(-window_height//2, window_height//2)
        action.move_by_offset(x_offset, y_offset).perform()
        time.sleep(random.uniform(0.5, 1.5))  # Đảm bảo thời gian di chuyển không quá nhanh
    except WebDriverException as e:
        print(f"Error: {e}")
        driver.execute_script("window.scrollBy(0, 250);")
        time.sleep(1)
        
def run_my_selenium2(email, password):
    command = ["python", "youtube_stream.py", "--email", email, "--password", password]
    try:
        subprocess.run(command, check=True)
        print(f"youtube_stream.py đã chạy thành công với email: {email}")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy youtube_stream.py với email {email}: {e}")


# Chạy Selenium chính trong một thread
def run_main_selenium():
    driver = uc.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    for link in selected_links:
        driver.get("https://www.dailymotion.com/playlist/x9dd5m")
        time.sleep(random.uniform(60, 130))
        driver.save_screenshot(f"screenshot_main_{time.time()}.png")

        driver.get(link)
        time.sleep(random.uniform(1, 30))
        random_mouse_move(driver)

        driver.save_screenshot(f"screenshot_main_{time.time()}.png")
        time.sleep(random.uniform(300, 360))

    driver.quit()
    print("Selenium chính đã hoàn thành.")

# Chạy my_selenium2.py
def run_my_selenium2(email, password):
    command = ["python", "youtube_stream.py", "--email", email, "--password", password]
    try:
        subprocess.run(command, check=True)
        print(f"youtube_stream.py đã chạy thành công với email: {email}")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy youtube_stream.py với email {email}: {e}")

# Khởi tạo và chạy thread Selenium chính
main_thread = threading.Thread(target=run_main_selenium)
main_thread.start()

# Khởi chạy các thread của my_selenium2.py
threads = []
for email, password in email_list:
    thread = threading.Thread(target=run_my_selenium2, args=(email, password))
    threads.append(thread)
    thread.start()

# Chờ tất cả các thread hoàn thành
for thread in threads:
    thread.join()

# Chờ Selenium chính hoàn thành
main_thread.join()

print("Tất cả các quá trình đã hoàn tất.")

