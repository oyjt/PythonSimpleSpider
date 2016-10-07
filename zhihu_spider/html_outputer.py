class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):

        # MarkDown语法输出
        fout = open('output.md', 'w', encoding='utf8')

        # 使用MarkDown语法输出
        fout.write('#知乎话题\n')
        for data in self.datas:
            fout.write("##[%s](%s)\n" % (data['topic'], data['url']))
            fout.write("> %s" % (data['content']))
            fout.write('\n\n---------\n\n')  # 分隔线

        fout.close()