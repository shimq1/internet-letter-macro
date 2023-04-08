from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

TARGET_URL = "https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=sub&dum=dum&command2=writeEmail&searchCate=&searchVal=&page=1&memberSeqVal=329895870&sodaeVal=1208"
DRIVER_DIR = "/Users/shimq1/Downloads/chromedriver_mac_arm64/chromedriver"


# 웹 드라이버 실행 (Chrome 사용 예시)
driver = webdriver.Chrome(DRIVER_DIR)


# 웹 페이지 로드
driver.get(TARGET_URL)

original_window = driver.current_window_handle

# 우편번호 검색 클릭
driver.find_element(By.CSS_SELECTOR, "#emailPic-container > form > div.UIview > table > tbody > tr:nth-child(3) > td > div:nth-child(1) > span > input").click()

# 팝업창으로 전환
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

# 무시하고 보내기 클릭
driver.find_element(By.ID, "proceed-button").click()

# 주소 검색창에 입력
driver.find_element(By.ID, "keyword").send_keys("관악로 1")
# 검색 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#searchContentBox > div.search-wrap > fieldset > span > input[type=button]:nth-child(2)").click()
# 서울대 주소 클릭
driver.find_element(By.CSS_SELECTOR, "#roadAddrDiv1 > b").click()
# 상세주소 지환부 입력
driver.find_element(By.CSS_SELECTOR, "#rtAddrDetail").send_keys("지환부")
# 주소입력 클릭
driver.find_element(By.CSS_SELECTOR, "#resultData > div > a").click()

# 원래 창으로 전환
driver.switch_to.window(original_window)

# 변수 정의
senderName = driver.find_element(By.ID, "senderName")
relationship = driver.find_element(By.ID, "relationship")
title = driver.find_element(By.ID, "title")
contents = driver.find_element(By.ID, "contents")
password = driver.find_element(By.ID, "password")

#-------------------------------------------

# 내용 입력
senderName.send_keys()
relationship.send_keys()
title.send_keys()
contents.send_keys()
password.send_keys()

# 작성완료 클릭
driver.find_element(By.CSS_SELECTOR, "#emailPic-container > form > div.UIbtn > span.wizBtn.large.Ngray.submit > input").click()

driver.close()
sleep(0.2)