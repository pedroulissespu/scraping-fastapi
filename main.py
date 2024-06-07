from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/bianca")
async def root():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Download the webdriver
    service = Service("chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("http://bianca.com")

    title = driver.title
    cookies = driver.get_cookies()
    text = driver.find_element(By.XPATH, '/html').text
    inner_html = driver.find_element(By.XPATH, '/html').get_attribute('innerHTML')
    is_selected = driver.find_element(By.XPATH, '/html').is_selected()
    css_value = driver.find_element(By.XPATH, '/html').value_of_css_property('propriedade_css')

    attributes_rows = []

    rows = driver.find_elements(By.XPATH, 'xpath_das_linhas')
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        attributes_rows.append(cells)

    link = driver.find_element(By.XPATH, '/html').get_attribute('h1')

    items = driver.find_elements(By.XPATH, '/html')

    list_items = []
    for item in items:
        list_items.append(item.text)

    driver.quit()
    return {'title': title,
            'cookies': cookies,
            'text_html': text,
            'inner_html': inner_html,
            'is_selected': is_selected,
            'css_value': css_value,
            'attributes_rows': attributes_rows,
            'link': link,
            'list_items': list_items}

    