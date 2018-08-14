from bs4 import BeautifulSoup as bs
import urllib.parse
import re


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = bs(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)  # 找新urls
        new_data = self._get_new_data(page_url, soup)  # 找新data
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.htm
        links = soup.find_all('option', value=re.compile(r"132"))
        for link in links:
            new_url = 'https://aisap.nutc.edu.tw/public/day/course_list.aspx?sem=1071&clsno=' + link['value']
            # new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = []

        # <td style="text-align:left; padding-left:10px;">星期五第５～７節 (2403)</td>
        td_nodes = soup.find_all('tr')
        # if td_node != None:
        #     # tr
        #     res_data['tr'] = td_node.find_parents('tr')
        # else:
        #     res_data['tr'] = None

        for td_node in td_nodes:
            res_data.append(td_node)

        return res_data
