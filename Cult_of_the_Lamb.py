import SeleniumInfo
import time

browser = SeleniumInfo.browser

browser.get('https://www.trueachievements.com/game/Cult-of-the-Lamb')
hub = browser.find_element_by_class_name('game-hub')
article = hub.find_element_by_tag_name('article').find_element_by_tag_name('a')

with open('recentHeadline.txt','r+') as f:
    if f.read() != article.find_elements_by_tag_name('h3')[0].text:
        f.seek(0)
        message = client.messages \
                    .create(
                         body='Read the updated news story for Cult of the Lamb:\n' + article.get_attribute('href'),
                         from_=twilio_phone,
                         to='+16039212997'
                     )
        f.write(article.find_elements_by_tag_name('h3')[0].text)
        f.truncate()
        print(article.find_elements_by_tag_name('h3')[0].text)
        print(article.get_attribute('href'))
    else:
        print('No updates on Cult of the Lamb')

browser.quit()
input()
