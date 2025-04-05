
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# 設定 Selenium 瀏覽器選項
options = Options()
options.headless = True  # 無頭模式，不顯示瀏覽器畫面

# 啟動瀏覽器
driver = webdriver.Chrome(options=options)

# 進入路由器登入頁面
driver.get("http://192.168.1.1/Main_WStatus_Content.asp")

# 找到帳號與密碼輸入框
username_input = driver.find_element(By.NAME, "login_username")
password_input = driver.find_element(By.NAME, "login_passwd")

# 輸入帳號和密碼（請替換成你的登入資訊）
username_input.send_keys("admin")
password_input.send_keys("admin")
password_input.send_keys(Keys.RETURN)

# 等待登入完成
time.sleep(5)

# 自動刷新頁面
refresh_interval = 10  # 設定每 10 秒刷新一次

try:
                                                                                while True:
                                                                                                                                                                        time.sleep(refresh_interval)  # 等待一段時間
                                                                                                                                                                                driver.refresh()  # 刷新頁面
                                                                                                                                                                                        
        # 擷取特定資訊（範例：SSID名稱）
                try:
                                                                                                            ssid = driver.find_element(By.ID, "elliptic_ssid_2g").text
                                                                                                                        print(f"目前 SSID: {ssid}")
                                                                                                                                except:
                                                                                                                                                                                                                            print("未找到 SSID 資訊，請確認元素是否存在。")
                                                                                                                                                                                                                            except KeyboardInterrupt:
                                                                                                                                                                                                                                                                                                                print("程式被停止。")
                                                                                                                                                                                                                                                                                                                finally:
                                                                                                                                                                                                                                                                                                                                                                                                    driver.quit()
                                                                                                                                                                                                                                                                                                                                                                                                    