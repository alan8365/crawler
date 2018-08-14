class UrlManager(object):#這個通常不用改

    #初始設定
    def  __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #加入新的url
    def add_new_url(self,url):
         if url is None:
             return
         if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #加入一群新的url
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #檢查new_urls裡有沒有東西
    def has_new_url(self):
        return len(self.new_urls) != 0

    #拿出url並且避免重複訪問
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url