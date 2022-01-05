import xlwt





def into_xls(datalist, file_name):
    workbook = xlwt.Workbook(encoding="utf-8")
    n = 0
    for i, data in enumerate(datalist):
        if i%50 == 0:
            sheet = workbook.add_sheet("sheet%d"%(i//50+1))
            n = 0
            sheet.write(0, 0, "编号")
            sheet.write(0, 1, "工作链接")
            sheet.write(0, 2, "公司链接")
            sheet.write(0, 3, "工作名称")
            sheet.write(0, 4, "公司名称")
            sheet.write(0, 5, "工资")
            sheet.write(0, 6, "发布日期")
            sheet.write(0, 7, "公司规模")
            sheet.write(0, 8, "待遇")
            sheet.write(0, 9, "工作详情")
            sheet.write(0, 10, "工作类别")
        sheet.write(n + 1, 0, str(i+1))
        for j in range(len(data)):
            sheet.write(n + 1, j + 1, data[j])
        n += 1
    workbook.save(file_name)

if __name__ == "__main__":
    bbb = open("bbb.txt", "r", encoding="utf-8")
    res = bbb.read()
    into_xls(eval(res), "bbb.xls")
