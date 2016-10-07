class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # html输出
        # fout = open('output.html', 'w', encoding='utf-8')
        #
        # fout.write("<html>")
        # fout.write('<head><meta charset="utf-8">')
        # fout.write('<link href="http://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">')
        # fout.write("</head>")
        # fout.write("<body>")
        # fout.write("<table class='table table-bordered table-striped'>")
        #
        # for data in self.datas:
        #     fout.write("<tr>")
        #     fout.write("<td><a href='%s' target='_blank'>%s</a></td>" % (data['url'], data['title']))
        #     fout.write("<td>%s</td>" % data['summary'])
        #     fout.write("</tr>")
        #
        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")
        #
        # fout.close()

        # MarkDown语法输出
        fout = open('output.md', 'w', encoding='utf8')

        # 使用MarkDown语法输出
        fout.write('#百度百科\n')
        for data in self.datas:
            fout.write("##[%s](%s)\n" % (data['title'], data['url']))
            fout.write("> %s" % (data['summary']))
            fout.write('\n\n---------\n\n')  # 分隔线

        fout.close()

        # import pymysql.cursors
        #
        # # change root password to yours:
        # conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8mb4')
        #
        # try:
        #     #获取会话指针
        #     cursor = conn.cursor()
        #     # 创建baike表:
        #     cursor.execute('CREATE TABLE IF NOT EXISTS `baike` ('
        #                    '`id` INT NOT NULL AUTO_INCREMENT,'
        #                    '`title` VARCHAR (255) NOT NULL,'
        #                    '`intro` text NOT NULL,'
        #                    '`link` VARCHAR (255) NOT NULL,'
        #                    'PRIMARY KEY (`id`))')
        #     # 插入一行记录，注意MySQL的占位符是%s:
        #     for data in self.datas:
        #         sql = 'INSERT INTO `baike` (`title`, `intro`, `link`) VALUES (%s, %s, %s)'
        #         cursor.execute(sql, (data["title"], data['summary'], data['url']))
        #     # 提交事务:
        #     conn.commit()
        # finally:
        #     conn.close()
