import os
import logging
from playwright.sync_api import sync_playwright


RU_HHTOKEN = os.getenv("RU_HHTOKEN")
KZ_HHTOKEN = os.getenv("KZ_HHTOKEN", default=None)
RU_RESUME = os.getenv("RU_RESUME")
KZ_RESUME= os.getenv("KZ_RESUME", default=None)
ru_cookies = [{"domain": ".hh.ru", "path": "/", "name": "hhtoken", "value": RU_HHTOKEN}]
kz_cookies = [{"domain": ".hh.kz", "path": "/", "name": "hhtoken", "value": KZ_HHTOKEN}]


logging.basicConfig(filename='hh_renewer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.add_cookies(ru_cookies)
    page = context.new_page()
    page.goto(RU_RESUME)
    if page.locator('[data-qa="resume-update-button"]').is_enabled():
        page.locator('[data-qa="resume-update-button"]').click()
        logging.info('RU_SUCCESS')
        print('RU_SUCCESS')
    else:
        logging.critical('RU_FAILED')
        print('RU_FAILED')

    if KZ_HHTOKEN is not None and KZ_RESUME is not None:
        context = browser.new_context()
        context.add_cookies(kz_cookies)
        page = context.new_page()
        page.goto(KZ_RESUME)
        if page.locator('[data-qa="resume-update-button"]').is_enabled():
            page.locator('[data-qa="resume-update-button"]').click()
            logging.info('KZ_SUCCESS')
            print('KZ_SUCCESS')
        else:
            logging.critical('KZ_FAILED')
            print('KZ_FAILED')
    browser.close()

logging.shutdown()