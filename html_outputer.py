class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def clooect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def out_html(self):
        fout = open('twoyeardata.html','w',encoding='utf-8')

        fout.write("<meta charset='utf-8'>")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")


        for data in self.datas:
            for d in data:
                fout.write("%s" % d)

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()