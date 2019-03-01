class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def clooect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def out_html(self, output_name):
        with open(output_name, 'w', encoding='utf-8') as file_out:

            file_out.write("<meta charset='utf-8'>")
            file_out.write("<html>")
            file_out.write("<body>")
            file_out.write("<table>")

            for data in self.datas:
                for d in data:
                    file_out.write("%s" % d)

            file_out.write("</table>")
            file_out.write("</body>")
            file_out.write("</html>")
