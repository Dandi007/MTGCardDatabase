import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建一个浏览器设置等待加载时间
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


# 打开淘宝首页，添加搜索关键字
def searcher():
    try:
        browser.get("https://www.taobao.com")
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")))
        input.send_keys("美食")
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total")))
        get_products()
        return total.text
    except TimeoutException:
        return searcher()


# 执行翻页的操作
def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.active > span"), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)


# 提取每个产品的详细信息
def get_products():
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#mainsrp-itemlist .items .item")))
    html = browser.page_source
    print(html)


def main():
    total = searcher()
    # 产品总页数
    total = int(re.compile("(\d+)").search(total).group(1))
    for i in range(2, total + 1):
        next_page(i)
    browser.quit()


if __name__ == "__main__":
    main()
