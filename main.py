from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time
import undetected_chromedriver as uc

# Inisialisasi driver
chrome_options = Options()
chrome_options.add_argument("user-agent=USERAGENT") # ganti USERAGENT dengan user agent yang digunakan
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--window-size=1280,720")  # ukuran jendela yang lebih kecil
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--user-data-dir=USERDATA") # ganti USERDATA dengan lokasi folder data user untuk login yang tidak berkali kali

driver = uc.Chrome(options=chrome_options)

# URL shopee flash sale
url = "URL_SHOPEE_FLASH_SALE" # ganti URL_SHOPEE_FLASH_SALE dengan url shopee flash sale yang akan dijadwalkan

# Buka halaman web
driver.get(url)
print("Berhasil masuk ke dalam website.")

input("Tekan enter untuk melanjutkan...") # Untuk mengantisipasi capctha (solve manual)

# Countdown Waktu flash sale 00.00.00
target_time = "00:00:00"

def wait_until_target_time(target_time):
    print(f"Menunggu hingga waktu {target_time}...")
    while True:
        # Ambil waktu sekarang
        now = datetime.now().strftime("%H:%M:%S")
        if now == target_time:
            print("Waktu yang diinginkan telah tiba.")
            break
        time.sleep(1)  # Cek setiap 1 detik (atau sesuai kebutuhan)

# Tunggu hingga waktu target untuk merefresh
wait_until_target_time(target_time)

# Refresh halaman web pada waktu yang diinginkan
print("Merefresh halaman web...")
driver.refresh()
print("Berhasil merefresh halaman web.")

# Opsi dalam produk
# Tunggu dan klik tombol Red
try:
    button_purple = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Red']")) # bisa diganti dengan xpath yang lain jika tombolnya berbeda
    )
    button_purple.click()
    print("Berhasil klik tombol Red.")
except TimeoutException:
    print("Error: Tombol Purple tidak ditemukan.")

# Klik Beli dengan voucher
try:
    # Tunggu tombol yang mengandung teks "Beli Dengan Voucher"
    button_voucher = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sll2-normal-pdp-main"]/div/div[1]/div/div[2]/section[1]/section[2]/div/div[5]/div/div/button[2]'))
    )
    button_voucher.click()
    print("Berhasil klik tombol 'Beli Dengan Voucher'.")
except TimeoutException:
    print("Error: Tombol 'Beli Dengan Voucher' tidak ditemukan.")

# Klik Beli Sekarang
try:
    # Tunggu tombol yang mengandung teks "Beli Sekarang" jika tidak ada "Beli Dengan Voucher"
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn-solid-primary') and text()='beli sekarang']"))
    ).click()
    print("Berhasil klik beli sekarang.")
except TimeoutException:
    print("Error: Tombol 'beli sekarang' tidak ditemukan.")

# Klik Checkout
try:
    # Tunggu elemen checkout muncul
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'shopee-button-solid') and .//span[text()='checkout']]"))
    ).click()
    print("Berhasil klik checkout.")
except TimeoutException:
    print("Error.")

# buat metode pembayaran bisa pilih salah satu

# Memilih metode pembayaran Shopee Pay
try:
    button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='ShopeePay']]"))
    )
    button.click()
    print("Berhasil memilih metode pembayaran ShopeePay.")
except TimeoutException:
    print("Error: Tombol ShopeePay tidak ditemukan atau saldo habis.")

# memilih metode pembayaran COD
try:
    # Tunggu tombol COD yang aktif (aria-disabled="false")
    button_cod = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='COD' and @aria-disabled='false']"))
    )
    button_cod.click()
    print("Berhasil klik tombol COD.")
except TimeoutException:
    print("Error: Tombol COD tidak ditemukan atau tidak aktif.")

# Memilih metode pembayaran Transfer Bank
try:
    # Tunggu elemen metode pembayaran muncul
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'product-variation') and text()='Transfer Bank']"))
    ).click()
    print("Berhasil klik metode pembayaran Transfer Bank.")
except TimeoutException:
    print("Error.")

try:
    # tunggu elemen metode pembayaran muncul berdasarkan XPath yang lebih spesifik
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'checkout-bank-transfer-item__title') and text()='Bank BNI']")) # ganti dengan bank yang dipilih
    ).click()
    print("Berhasil klik metode pembayaran Bank BNI.")
except TimeoutException:
    print("Error: Metode pembayaran Bank BNI tidak ditemukan.")

input("Tekan enter untuk melanjutkan...") # Untuk memastikan metode pembayaran sudah dipilih

try:
    button = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.stardust-button.stardust-button--primary.stardust-button--large.LtH6tW"))
    )
    button.click()
    print("Berhasil klik buat pesanan.")
except TimeoutException:
    print("Error: Tombol tidak ditemukan.")

time.sleep(120)