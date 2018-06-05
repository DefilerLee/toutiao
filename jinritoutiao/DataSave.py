from jinritoutiao.MySQL.MysqlHelper import *

class DataSave(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.db = 'jinri'
        self.user = 'root'
        self.passwd = 'root'
        self.mysqllink = MysqlHelper(self.host, self.port, self.db, self.user, self.passwd)

    def add_wenda(self, new_id, new_url,new_title,new_content):
        params = [ new_id, new_url,new_title,new_content]
        sql = 'INSERT INTO new_wenda (new_id, new_url,new_title,new_content ) VALUES ( %s,%s,%s,%s)'
        self.mysqllink.insert(sql, params)

    def add_article(self,new_id, new_url,new_title,new_content,new_from,new_time):
        params = [new_id, new_url,new_title,new_content,new_from,new_time]
        sql = 'insert into new_article (new_id, new_url,new_title,new_content,new_from,new_time) VALUES (%s,%s,%s,%s,%s,%s)'
        self.mysqllink.insert(sql, params)

# if __name__ == '__main__':
#     item = manhua_biaoti()
#     item['name'] = 'name14'
#     da = DataSave()
#     da.add_manhua(item['name'])