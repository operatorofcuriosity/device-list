
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# �]�w Selenium �s�����ﶵ
options = Options()
options.headless = True  # �L�Y�Ҧ��A������s�����e��

# �Ұ��s����
driver = webdriver.Chrome(options=options)

# �i�J���Ѿ��n�J����
driver.get("http://192.168.1.1/Main_WStatus_Content.asp")

# ���b���P�K�X��J��
username_input = driver.find_element(By.NAME, "login_username")
password_input = driver.find_element(By.NAME, "login_passwd")

# ��J�b���M�K�X�]�д������A���n�J��T�^
username_input.send_keys("admin")
password_input.send_keys("admin")
password_input.send_keys(Keys.RETURN)

# ���ݵn�J����
time.sleep(5)

# �۰ʨ�s����
refresh_interval = 10  # �]�w�C 10 ���s�@��

try:
                                                                                while True:
                                                                                                                                                                        time.sleep(refresh_interval)  # ���ݤ@�q�ɶ�
                                                                                                                                                                                driver.refresh()  # ��s����
                                                                                                                                                                                        
        # �^���S�w��T�]�d�ҡGSSID�W�١^
                try:
                                                                                                            ssid = driver.find_element(By.ID, "elliptic_ssid_2g").text
                                                                                                                        print(f"�ثe SSID: {ssid}")
                                                                                                                                except:
                                                                                                                                                                                                                            print("����� SSID ��T�A�нT�{�����O�_�s�b�C")
                                                                                                                                                                                                                            except KeyboardInterrupt:
                                                                                                                                                                                                                                                                                                                print("�{���Q����C")
                                                                                                                                                                                                                                                                                                                finally:
                                                                                                                                                                                                                                                                                                                                                                                                    driver.quit()
                                                                                                                                                                                                                                                                                                                                                                                                    