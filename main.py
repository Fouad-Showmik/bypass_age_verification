# # #To extract self-IP..
# #
# #
#
import requests
response=requests.get('https://ipinfo.io/json')
print(response.json())
# #
# #
# #
# # #To check valid proxies..
# #
# #
# #
import threading
import requests
import queue

q=queue.Queue()
valid_proxies=[]

with open('proxy.txt','r') as file:
    proxies=file.read().split('\n')
    for i in proxies:
        q.put(i)

def check_proxy():
    global q
    while not q.empty():
        proxy=q.get()
        try:
            response=requests.get('https://ipinfo.io/json',
                                  proxies={'http':proxy,'https':proxy})
        except:
            continue
        if response.status_code==200:
            print(proxy)
for j in range(10):
    threading.Thread(target=check_proxy).start()
    

# #
# #
# ####################################################
# #
# #
# #After rotating proxy we'll pick one of the valid proxies and put it here to check the origin..
#
#
import requests

proxies = {'http': 'http://190.104.245.86:8080'}
response = requests.get('http://httpbin.org/ip', proxies=proxies)
print(response.json())


######################################################

#User Agent (UA) Header..

import requests
import random

headers_list = [{
    'authority': 'httpbin.org',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',

    #Here in the array of user-agent, I Have to rotate it like the proxy too.
    #So, I can take the user-agents from the target website or other ideal websites
    #like Chrome, Firefox etc. by researching their updated user-agents (UA).
    #Besides,I can also provide a referrer user-agent from google or from the internal
    #page of the same website which will hide us more efficiently and provide more relay to the targeted
    #website to trust us.


    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0'
    'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0',


    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
}
]
headers = random.choice(headers_list)
response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json()['headers'])



#To avoid cookies we have to use a headless browser...

# import json
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch()
#         #Since the headless browsers identify themselves by their own, we are going
#         #to use custom user-agent here to over-write the defaluts of headless browsers..
#         page = browser.new_page(extra_http_headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/93.0.4576.0 Safari/537.36'
#                                                     'Mozilla/5.0 (X11; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0 '
#                                                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'})
#         page.goto('https://httpbin.org/headers')
#         jsonContent = json.loads(page.inner_text('pre'))
#         print(jsonContent['headers']['User-Agent'])
#         browser.close()


##Here I can use playwright-stealth to excelerate the code. But, sometimes it can give
#error since it doesn't cooperate with header and browser java-script API...

##sync
#Sync is a blocing operation which'll work after getting a response..

# from playwright import sync_playwright
# from playwright_stealth import stealth_sync

# with sync_playwright() as p:
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch()
#         page = browser.new_page()
#         stealth_sync(page)
#         page.goto('http://whatsmyuseragent.org/')
#         page.screenshot(path=f'example-{browser_type.name}.png')
#         browser.close()


##async
#async is a non-blocking operation which'll work without getting any response...

import asyncio
from playwright import async_playwright
from playwright_stealth import stealth_async

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await stealth_async(page)
            await page.goto('http://whatsmyuseragent.org/')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

asyncio.get_event_loop().run_until_complete(main())


#####async works more faster than sync and it is also efficient..


##################################################################################

##Sometimes we can't access due to GEO-Blocking. So, we have to use the specific country proxy IP..



#Here I'll use beautifulsoup to visit selected pages so that, the bot get confused to identify us..

import requests 
from bs4 import BeautifulSoup 
 
response = requests.get('https://scrapeme.live/shop/') 
soup = BeautifulSoup(response.content, 'html.parser') 
pages = soup.select('.woocommerce-pagination a.page-numbers:not(.next)') 
print(pages[0].get('href')) # https://scrapeme.live/shop/page/2/ 
print(pages[-1].get('href')) # https://scrapeme.live/shop/page/48/

##Here finishes the bypassing of age verification and then starts the bypassing session
#of captcha..

#######################################################################################
