from common_units.database import DataBaseClient
from read_config import ConfigReader
from common_units.small_tools import get_time

config = ConfigReader().get("mysql")


def db_test():
    db = DataBaseClient(**config)
    db.connection()
    sql = "insert into knowledge(t_uid, name, info, time) value ({}, \"{}\", \"{}\", \"{}\")".format(1, "第一次测验", "第一题\n第二题",
                                                                                                 get_time())
    sql = "select * from knowledge"
    print(sql)
    data = db.execute(sql)
    print(data[0][3])
    db.close()


if __name__ == '__main__':
    db_test()
