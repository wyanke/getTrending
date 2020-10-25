import splinter
from selenium.webdriver.chrome.options import Options
from splinter import Browser

chrome_options = Options()
chrome_options.add_argument("--headless") #this line hide your browser
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("start-maximised")

class Trending:
    def __init__(self, browser=Browser('chrome', options=chrome_options)):
        self.browser = browser
        self.titleArray = []
        self.timeArray = []
        self.dataVideo = []
        self.viewArray = []
        self.agoArray = []
        self.channelArray = []
        self.link = []
        self.ten = 1

    def start(self):
        Trending.access_main_page(self)
        Trending.open_trending(self)
        Trending.get_the_title_video(self)
        Trending.get_the_channel_name(self)
        Trending.get_the_video_length(self)
        Trending.get_the_link_video(self)
        Trending.get_the_views(self)
        Trending.console_view(self)

    def access_main_page(self):
        self.browser.visit('https://www.youtube.com')

    def open_trending(self):
        self.browser.find_by_css('a#endpoint')[1].click()

    def get_the_title_video(self):
        videosList = self.browser.find_by_css('.title-and-badge')
        for video in videosList:
            if self.ten <= 10 and video.text != '':
                self.titleArray.append(video.text)
                self.ten += 1
        self.ten = 1

    def get_the_link_video(self):
        videoLink = self.browser.find_by_css('.title-and-badge a')
        for link in videoLink:
            if self.ten <= 10:
                self.link.append(link['href'])
                self.ten += 1
        self.ten = 1

    def get_the_video_length(self):
        timeVideo = self.browser.find_by_css('#overlays')
        for clock in timeVideo:
            if self.ten <= 10 and clock.text != '':
                self.timeArray.append(clock.text)
                self.ten += 1
                self.browser.execute_script("window.scrollTo(0, 700);")
        self.ten = 1

    def get_the_channel_name(self):
        channelName = self.browser.find_by_css('ytd-expanded-shelf-contents-renderer #text')
        for channel in channelName:
            if self.ten <= 10 and channel.text != '':
                self.channelArray.append(channel.text)
                self.ten += 1
        self.ten = 1

    def get_the_views(self):
        viewsAndDaysAgo = self.browser.find_by_css('ytd-expanded-shelf-contents-renderer #metadata-line span')
        for video in viewsAndDaysAgo:
            if self.ten <= 20 and video.text != '':
                self.dataVideo.append(video.text)
                self.ten += 1

        for view in range(0, len(self.dataVideo), 2):
            self.viewArray.append(self.dataVideo[view])

        for ago in range(1, len(self.dataVideo), 2):
            self.agoArray.append(self.dataVideo[ago])


    def console_view(self):
        for list in range(0, 10):
            print(f'-'*70)
            print(f'''
    \033[32mTop \033[m{list+1}
    \033[32mName: \033[m{self.titleArray[list]}
    \033[32mBy: \033[m{self.channelArray[list]}
    \033[32mDuration: \033[m{self.timeArray[list]}
    \033[32mViews: \033[m{self.viewArray[list]}
    \033[32mDays ago: \033[m{self.agoArray[list]}
    \033[32mLink: \033[m{self.link[list]}
            ''')
            print(f'-'*70)
        self.browser.quit()

obj = Trending()
obj.start()
