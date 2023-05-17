import pymysql

try:
    db = pymysql.connect(host='localhost',user='root', password='root', database='School')
    print("OK")
except pymysql.Error as e:
    print('数据库连接失败')
cur = db.cursor()
if not cur:
    print('失败')
else:
    print('成功')


