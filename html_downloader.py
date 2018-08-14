from selenium import webdriver as wb

class HtmlDownloader(object):#這個不用改

    def download(self, url):
        if url is None:
            return None

        driver = wb.PhantomJS(executable_path=r'D:\Users\USER\PycharmProjects\crawler\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        driver.get(url)
        page_source = driver.page_source

        driver.close()

        return page_source