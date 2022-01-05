import re


def analysis(datalist, dictData):
    for item in dictData.get("engine_jds"):
        data = [item.get("job_href",""),
                item.get("company_href",""),
                item.get("job_name",""),
                item.get("company_name",""),
                item.get("providesalary_text",""),
                item.get("updatedate",""),
                item.get("companytype_text","") + " " + item.get("companysize_text", ""),
                item.get("jobwelf",""),
                " ".join(item.get("attribute_text")),
                item.get("companyind_text", "")]
        for i, n in enumerate(data):
            data[i] = re.sub(r'\\*', '', n)
        datalist.append(data)
