import url_manager,html_downloader,html_parser,html_outputer,time

class SpiderMain(object):

    #初始設定
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.starttime = time.time()

    def craw(self, root_url):
        count = 1

        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():#只要還有url
            new_url = self.urls.get_new_url()#拿一個url出來
            print('craw',count,':',new_url)
            html_cont = self.downloader.download(new_url)#把剛剛url的網頁內容載下來
            # print('download:', time.time() - self.starttime)
            new_urls, new_data = self.parser.parse(new_url,html_cont)#從剛剛的html裡拿出新的url和data
            # print('dataget:', time.time() - self.starttime)
            self.urls.add_new_urls(new_urls)#把新的url裝進url_manager
            self.outputer.clooect_data(new_data)#把data輸出給html_outputer
            count = count + 1

        self.outputer.out_html()#輸出成html


root_url = 'https://aisap.nutc.edu.tw/public/day/course_list.aspx?sem=1071&clsno=1320181191'#輸入根網址
obj_spider = SpiderMain()
obj_spider.craw(root_url)