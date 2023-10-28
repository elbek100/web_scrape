from playwright.sync_api import sync_playwright


def youtube():
    with sync_playwright() as p:
        url = 'https://youtube.com'

        browser = p.firefox.launch()

        page = browser.new_page()

        page.goto(url)

        img_url = page.locate_selector('img').screen(save_as='temp.jpg')

        browser.close()

        return img_url


if __name__ == '__main__':
    youtube()

'''
   ustoz uzur bir ikkta joyi esimdan chiqibti 
'''
