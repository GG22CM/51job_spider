import sqlite3


def into_sqlite(datalist, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for data in datalist:
        for i in range(len(data)):
            data[i] = "\'" + data[i] + "\'"
        sql = "insert into t_jobs(job_href, company_href, job_name, company_name, salary, up_date, company_size, treatment, info, category) values(%s)"%(",".join(data))
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    bbb = open("bbb.txt", "r", encoding="utf-8")
    res = bbb.read()
    into_sqlite(eval(res), "jobs.db")