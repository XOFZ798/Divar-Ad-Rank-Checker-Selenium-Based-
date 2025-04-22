from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import platform
import re
import time


def normalize(text):
    """حذف فاصله و علائم مخفی از متن"""
    return re.sub(r"[\u200c\u200f\xa0\s]+", "", text).strip().lower()


def get_ad_rank_selenium(exact_title):
    options = Options()
    # اجرای معمولی برای دیباگ (غیرفعال کردن Headless)
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        search_url = "https://divar.ir/s/mashhad/technology-services"
        driver.get(search_url)

        # صبر برای بارگذاری کامل صفحه
        time.sleep(10)

        # ذخیره سورس صفحه جهت بررسی
       # with open("divar_output.html", "w", encoding="utf-8") as f:
         ## print("✅ صفحه ذخیره شد در فایل: divar_output.html")

        # پیدا کردن تایتل‌ها
        elements = driver.find_elements(By.CLASS_NAME, "kt-post-card__title")
        norm_title = normalize(exact_title)

        for index, elem in enumerate(elements):
            if normalize(elem.text.strip()) == norm_title:
                return index + 1
        return None
    finally:
        driver.quit()


def play_alarm():
    """پخش آلارم در صورت رد شدن از حد مجاز"""
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(2000, 1500)
        else:
            print("\a")
    except:
        print("⚠️ Alarm failed.")


# -------------------------------------
# اجرای اصلی
if __name__ == "__main__":
    print("📡 Divar Ad Rank Checker [Selenium]")
    title = input("🔤 Enter exact ad title: ").strip()
    threshold = 3

    print("⏳ Searching in Divar...")
    rank = get_ad_rank_selenium(title)

    if rank is None:
        print("❗ Ad not found.")
    elif rank > threshold:
        print(f"🚨 ALERT: Rank is {rank} (above {threshold})")
        play_alarm()
    else:
        print(f"✅ Ad rank is {rank}. All good.")
