#!/usr/bin/python3

import pymongo
import time

"""
功能：创建指定数量的用户手机账号供测试使用
"""

# 数据库链接参数
MONGO_HOST = "10.0.0.5:27017"
MONGO_USER = "mongouser"
MONGO_PWD = "Wz19840311"
MONGO_AUTH = "admin"
# 数据库名
MONGO_DB = "blockchain"
# 表名
MONGO_COL = "user"

myclient = pymongo.MongoClient(MONGO_HOST, username=MONGO_USER, password=MONGO_PWD, authSource=MONGO_AUTH)
mydb = myclient[MONGO_DB]
mycol = mydb[MONGO_COL]

# 需要创建的用户数（范围：0~99）
USER_COUNT = 10
# 手机用户固定账户前缀（国际区域编码+前9位）
PHONE_PERFIX = '86166000000'
# 密码SHA1摘要
PASSWORD = '601f1889667efaebb33b8c12572835da3f027f78'   # 明文‘123123’
# 待处理的用户列表
userlist = []
# 获取当前毫秒时间戳
current_milli_time = lambda: int(round(time.time() * 1000))

for i in range(0, USER_COUNT):
    num  = '0'+str(i) if i<10 else str(i) # 账号后两位处理
    userlist.append({
        "nickName": PHONE_PERFIX+num,
        "phone": PHONE_PERFIX+num,
        "password": PASSWORD,
        "registerIP": 'test',
        "registerTime": current_milli_time()
    })

x = mycol.insert_many(userlist)
print(x.inserted_ids)