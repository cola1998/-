import os,sys,copy
import numpy as np
from bisect import bisect_right, bisect_left
from collections import deque
import pandas as pd
import copy
from pandas import DataFrame
import os

def linkage_operation(relationship1,relationship2,condition,core_relationship):
    file_name = 'new_'+core_relationship+'.csv'
    if os.path.isfile(file_name) == True:
        if core_relationship == relationship1:
            relationship1_data = pd.read_csv(file_name, dtype=str)
            relationship2_fname = 'H:\\new_data\\' + relationship2 + '.csv'
            relationship2_data = pd.read_csv(relationship2_fname, dtype=str)
        else:
            relationship1_fname = 'H:\\new_data\\' + relationship1 + '.csv'
            relationship1_data = pd.read_csv(relationship1_fname, dtype=str)
            relationship2_data = pd.read_csv(file_name, dtype=str)
    else:
        relationship1_fname = 'temp_' + relationship1 + '.csv'
        relationship1_data = pd.read_csv(relationship1_fname, dtype=str)
        relationship2_fname = 'temp_' + relationship2 + '.csv'
        relationship2_data = pd.read_csv(relationship2_fname, dtype=str)

    condition = condition.strip("' ").split('=')
    condition1 = str(condition[0]).split('.')
    condition2 = str(condition[1]).split('.')
    if (condition1[0] == relationship1) and (condition2[0] == relationship2):
        # 两张表进行连接
        # 初始化new_data
        new_data = {}
        for v in relationship1_data:
            new_data[v] = []
        for u in relationship2_data:
            new_data[u] = []
        for i in range(len(relationship1_data)):
            for j in range(len(relationship2_data)):
                if relationship1_data[condition1[1]][i] == relationship2_data[condition2[1]][j]:
                    for v in new_data:
                        if (v in relationship1_data) == True:
                            new_data[v].append(relationship1_data[v][i])
                        elif (v in relationship2_data) == True:
                            new_data[v].append(relationship2_data[v][j])
                        else:
                            print('Wrong')
        new_data = pd.DataFrame(new_data)
    elif (condition2[0] == relationship1) and (condition1[0] == relationship2):
            temp = condition1
            condition1 = condition2
            condition2 = temp
            # 交换后就可以了
            print("relationship1_data:\n", relationship1_data)
            print("relationship2_data:\n", relationship2_data)
            # 初始化new_data
            new_data = {}
            for v in relationship1_data:
                new_data[v] = []
            for u in relationship2_data:
                new_data[u] = []
            print(new_data)
            for i in range(len(relationship1_data)):
                for j in range(len(relationship2_data)):
                    if relationship1_data[condition1[1]][i] == relationship2_data[condition2[1]][j]:
                        for v in new_data:
                            if (v in relationship1_data) == True:
                                new_data[v].append(relationship1_data[v][i])
                            elif (v in relationship2_data) == True:
                                new_data[v].append(relationship2_data[v][j])
                            else:
                                print('Wrong')
            print(new_data)
            new_data = pd.DataFrame(new_data)
    else:
        print('condition is not match, you need check!')
        return 0
    print(new_data)
    new_data.to_csv(file_name,mode='w',index=False)


def match_id_pwd(id,pwd):
    # 读文件
    db_data = pd.read_csv('users.csv', converters={'user_id':str, 'user_pwd':str}, keep_default_na=False)
    #print(db_data)
    #print(type(db_data))
    dx = copy.copy(db_data.loc[(db_data['user_id'] == id) & (db_data['user_pwd'] == pwd)])
    if(dx.empty == True):
        print('未找到该集合')
        return 0
    else:
        # print(dx)
        return 1


class InitError(Exception):
    pass


class ParaError(Exception):
    pass


# 生成键值对
class KeyValue(object):
    __slots__ = ('key', 'value')

    def __init__(self, key, value):
        self.key = int(key)  # 一定要保证键值是整型
        self.value = value

    def __str__(self):
        return str((self.key, self.value))

    def __cmp__(self, key):
        if self.key > key:
            return 1
        elif self.key < key:
            return -1
        else:
            return 0

    def __lt__(self, other):
        if (type(self) == type(other)):
            return self.key < other.key;
        else:
            return int(self.key) < int(other);

    def __eq__(self, other):
        if (type(self) == type(other)):
            return self.key == other.key;
        else:
            return int(self.key) == int(other);

    def __gt__(self, other):
        return not self < other;

# B+树实现
# 实现过程和btree很像，不过有几点显著不同。
# 1.内节点不存储key-value，只存放key
#
# 2.沿着内节点搜索的时候，查到索引相等的数要向树的右边走。所以二分查找要选择
# bisect_right
#
# 3.在叶子节点满的时候，并不是先分裂再插入而是先插入再分裂。因为b+tree无法保证
# 分裂的两个节点的大小都是相等的。在奇数大小的数据分裂的时候右边的子节点会比左
# 边的大。如果先分裂再插入无法保证插入的节点一定会插在数量更少的子节点上，满足
# 节点数量平衡的条件。
#
# 4.在删除数据的时候，b+tree的左右子节点借数据的方式比btree更加简单有效，只把子
# 节点的子树直接剪切过来，再把索引变一下就行了，而且叶子节点的兄弟指针也不用动。
#
class Bptree(object):
    class __InterNode(object):
        def __init__(self, M):
            if not isinstance(M, int):
                raise InitError('M must be int')
            if M <= 3:
                raise InitError('M must be greater then 3')
            else:
                self.__M = M
                self.clist = []  # 存放区间
                self.ilist = []  # 存放索引/序号
                self.par = None

        def isleaf(self):
            return False

        def isfull(self):
            return len(self.ilist) >= self.M - 1

        def isempty(self):
            return len(self.ilist) <= (self.M + 1) / 2 - 1

        @property
        def M(self):
            return self.__M

    # 叶子
    class __Leaf(object):
        def __init__(self, L):
            if not isinstance(L, int):
                raise InitError('L must be int')
            else:
                self.__L = L
                self.vlist = []
                self.bro = None  # 兄弟结点
                self.par = None  # 父结点

        def isleaf(self):
            return True

        def isfull(self):
            return len(self.vlist) > self.L

        def isempty(self):
            return len(self.vlist) <= (self.L + 1) / 2

        @property
        def L(self):
            return self.__L

    # 初始化
    def __init__(self, M, L,file_name):
        if L > M:
            raise InitError('L must be less or equal then M')
        else:
            self.__M = M
            self.__L = L
            self.__root = Bptree.__Leaf(L)
            self.__leaf = self.__root
            self.name = file_name

    @property
    def M(self):
        return self.__M

    @property
    def L(self):
        return self.__L

    # 插入
    def insert(self, key_value):
        node = self.__root

        def split_node(n1):
            mid = self.M // 2  # 此处注意，可能出错
            newnode = Bptree.__InterNode(self.M)
            newnode.ilist = n1.ilist[mid:]
            newnode.clist = n1.clist[mid:]
            newnode.par = n1.par
            for c in newnode.clist:
                c.par = newnode
            if n1.par is None:
                newroot = Bptree.__InterNode(self.M)
                newroot.ilist = [n1.ilist[mid - 1]]
                newroot.clist = [n1, newnode]
                n1.par = newnode.par = newroot
                self.__root = newroot
            else:
                i = n1.par.clist.index(n1)
                n1.par.ilist.insert(i, n1.ilist[mid - 1])
                n1.par.clist.insert(i + 1, newnode)
            n1.ilist = n1.ilist[:mid - 1]
            n1.clist = n1.clist[:mid]
            return n1.par

        def split_leaf(n2):
            mid = (self.L + 1) // 2
            newleaf = Bptree.__Leaf(self.L)
            newleaf.vlist = n2.vlist[mid:]
            if n2.par == None:
                newroot = Bptree.__InterNode(self.M)
                newroot.ilist = [n2.vlist[mid].key]
                newroot.clist = [n2, newleaf]
                n2.par = newleaf.par = newroot
                self.__root = newroot
            else:
                i = n2.par.clist.index(n2)
                n2.par.ilist.insert(i, n2.vlist[mid].key)
                n2.par.clist.insert(i + 1, newleaf)
                newleaf.par = n2.par
            n2.vlist = n2.vlist[:mid]
            n2.bro = newleaf

        def insert_node(n):
            if not n.isleaf():
                if n.isfull():
                    insert_node(split_node(n))
                else:
                    p = bisect_right(n.ilist, key_value)
                    insert_node(n.clist[p])
            else:
                p = bisect_right(n.vlist, key_value)
                n.vlist.insert(p, key_value)
                if n.isfull():
                    split_leaf(n)
                else:
                    return

        insert_node(node)

    # 搜索
    def search(self, mi=None, ma=None):
        result = []
        node = self.__root
        leaf = self.__leaf
        if mi is None or ma is None:
            raise ParaError('you need to setup searching range')
        elif mi > ma:
            raise ParaError('upper bound must be greater or equal than lower bound')

        def search_key(n, k):
            if n.isleaf():
                p = bisect_left(n.vlist, k)
                return (p, n)
            else:
                p = bisect_right(n.ilist, k)
                return search_key(n.clist[p], k)

        if mi is None:
            while True:
                for kv in leaf.vlist:
                    if kv <= ma:
                        result.append(kv)
                    else:
                        return result
                if leaf.bro == None:
                    return result
                else:
                    leaf = leaf.bro
        elif ma is None:
            index, leaf = search_key(node, mi)
            result.extend(leaf.vlist[index:])
            while True:
                if leaf.bro == None:
                    return result
                else:
                    leaf = leaf.bro
                    result.extend(leaf.vlist)
        else:
            if mi == ma:
                i, l = search_key(node, mi)
                try:
                    if l.vlist[i] == mi:
                        result.append(l.vlist[i])
                        return result
                    else:
                        return result
                except IndexError:
                    return result
            else:
                i1, l1 = search_key(node, mi)
                i2, l2 = search_key(node, ma)
                if l1 is l2:
                    if i1 == i2:
                        return result
                    else:
                        result.extend(l2.vlist[i1:i2])
                        return result
                else:
                    result.extend(l1.vlist[i1:])
                    l = l1
                    while True:
                        if l.bro == l2:
                            result.extend(l2.vlist[:i2])
                            return result
                        elif l.bro != None:
                            result.extend(l.bro.vlist)
                            l = l.bro
                        else:
                            return result

    def traversal(self):
        result = []
        l = self.__leaf
        while True:
            result.extend(l.vlist)
            if l.bro == None:
                return result
            else:
                l = l.bro

    def show(self):
        # 展示的同时生成一个索引文件
        print('this b+tree is:\n')

        q = deque() #s双端队列容器
        h = 0
        q.append([self.__root, h])
        f_name = (self.name+'_index.txt')
        with open(f_name, 'w') as f:
            while True:
                try:
                    w, hei = q.popleft()
                except IndexError:
                    return
                else:
                    if not w.isleaf():
                        print(w.ilist, 'the height is,', hei)
                        f.write(str(w.ilist)+'the height is,'+str(hei)+'\n')
                        if hei == h:
                            h += 1
                        q.extend([[i, h] for i in w.clist])
                    else:
                        d = ''
                        for v in w.vlist:
                            d += ('('+str(v.key)+","+str(v.value)+')'+',')
                        print(d.strip(','), 'the leaf is,', hei)
                        f.write(d+'the leaf is,'+str(hei)+'\n')

    # 删除
    def delete(self, key_value):
        def merge(n, i):
            if n.clist[i].isleaf():
                n.clist[i].vlist = n.clist[i].vlist + n.clist[i + 1].vlist
                n.clist[i].bro = n.clist[i + 1].bro
            else:
                print(n.clist[i].ilist)
                print([n.ilist[i]])
                print(n.clist[i + 1].ilist)
                n.clist[i].ilist = n.clist[i].ilist + [n.ilist[i]] + n.clist[i + 1].ilist
                n.clist[i].clist = n.clist[i].clist + n.clist[i + 1].clist
            n.clist.remove(n.clist[i + 1])
            n.ilist.remove(n.ilist[i])
            if n.ilist == []:
                n.clist[0].par = None
                self.__root = n.clist[0]
                del n
                return self.__root
            else:
                return n

        def tran_l2r(n, i):
            if not n.clist[i].isleaf():
                n.clist[i + 1].clist.insert(0, n.clist[i].clist[-1])
                n.clist[i].clist[-1].par = n.clist[i + 1]
                n.clist[i + 1].ilist.insert(0, n.ilist[i])
                n.ilist[i] = n.clist[i].ilist[-1]
                n.clist[i].clist.pop()
                n.clist[i].ilist.pop()
            else:
                n.clist[i + 1].vlist.insert(0, n.clist[i].vlist[-1])
                n.clist[i].vlist.pop()
                n.ilist[i] = n.clist[i + 1].vlist[0].key

        def tran_r2l(n, i):
            if not n.clist[i].isleaf():
                n.clist[i].clist.append(n.clist[i + 1].clist[0])
                n.clist[i + 1].clist[0].par = n.clist[i]
                n.clist[i].ilist.append(n.ilist[i])
                n.ilist[i] = n.clist[i + 1].ilist[0]
                n.clist[i + 1].clist.remove(n.clist[i + 1].clist[0])
                n.clist[i + 1].ilist.remove(n.clist[i + 1].ilist[0])
            else:
                n.clist[i].vlist.append(n.clist[i + 1].vlist[0])
                n.clist[i + 1].vlist.remove(n.clist[i + 1].vlist[0])
                n.ilist[i] = n.clist[i + 1].vlist[0].key

        def del_node(n, kv):
            if not n.isleaf():
                p = bisect_right(n.ilist, kv)
                if p == len(n.ilist):
                    if not n.clist[p].isempty():
                        return del_node(n.clist[p], kv)
                    elif not n.clist[p - 1].isempty():
                        tran_l2r(n, p - 1)
                        return del_node(n.clist[p], kv)
                    else:
                        return del_node(merge(n, p), kv)
                else:
                    if not n.clist[p].isempty():
                        return del_node(n.clist[p], kv)
                    elif not n.clist[p + 1].isempty():
                        tran_r2l(n, p)
                        return del_node(n.clist[p], kv)
                    else:
                        return del_node(merge(n, p), kv)
            else:
                p = bisect_left(n.vlist, kv)
                try:
                    pp = n.vlist[p]
                except IndexError:
                    return -1
                else:
                    if pp != kv:
                        return -1
                    else:
                        n.vlist.remove(kv)
                        return 0

        del_node(self.__root, key_value)


class User():  #管理员
    # 默认使用mysql数据库
    db = 'mysql'
    def __init__(self,id,password):
        self.id = id
        self.password = password


    def create_user(self):
        # 创建用户
        # create user 'hanhan'@'localhost' identified by '123456';
        t_user_id = str(command[2]).strip('\'').split('@')
        new_user_id = str(t_user_id[0]).strip('\'')
        print('user_id=', new_user_id)
        df = pd.read_csv('users.csv', converters={'user_id': str, 'user_pwd': str}, index_col=0)  # 旧数据
        dd = copy.copy(df.loc[df['user_id'] == new_user_id])
        if dd.empty == True:
            if command[3] == 'identified':
                if command[4] == 'by':
                    new_user_pwd = str(command[5]).strip('\'')
                    print(new_user_pwd)
                else:
                    print("Wrong！please check the position '%s'" % (command[4]))
                    return 0
            else:
                print("Wrong！please check the position '%s'" % (command[3]))
                return 0
        else:
            print('Wrong! This user has existed....')
            return 0

        d2 = {'user_id': [new_user_id], 'user_pwd': [new_user_pwd]}  # 新数据

        df = df.merge(DataFrame(d2), how='outer')  # 合并后
        df.to_csv('users.csv', mode='w')

        # 读文件，检查是否写入正确
        db_data = pd.read_csv('users.csv')
        print(db_data)


    def create_tables(self):
        # 创建表
        table_name = str(command[2]).strip(';\n')  # 处理table_name
        dt = pd.read_csv('tables.csv', converters={'DataBases': str, 'table': str})
        temp = copy.copy(dt.loc[dt['table'] == table_name])

        if temp.empty == False:  # 检查table是否存在
            print('Wrong! this table has been exists.~~o(>_<)o ~~')

        else:
            df = pd.read_csv('columns.csv',
                             converters={'DataBase': str, 'table': str, 'columns': str, 'not_null': str,
                                         'primary_key': str}, keep_default_na=False)  # 旧数据
            while True:
                c = input("please input columns ['name' 'data_type' 'not_null' 'primary_key']:")

                if c == 'end':
                    df.to_csv('columns.csv', mode='w', index=False)
                    print(df)
                    break
                else:
                    c = c.strip('\n').split(' ')
                    print(c)
                    while len(c) < 5:
                        c.append('no')

                    if c[2] == 'no' and c[3] == 'yes':
                        print('主键不能为空！本次记录未保存')
                    else:
                        new_df = {'DataBase': [self.db], 'table': [table_name], 'columns': [c[0]],
                                  'data_type': [c[1]], 'not_null': [c[2]],
                                  'primary_key': [c[3]]}
                        #print(new_df)
                        dd = df.merge(DataFrame(new_df), how='outer')
                        df = copy.copy(dd)
                        #print(df)

            new_dt = {'DataBase': self.db, 'table': table_name}
            temp = dt.merge(DataFrame(new_dt, index=[0]), how='outer')
            temp.to_csv('tables.csv', mode='w')  # 写入表名


    def create_bd(self):
        db_name = str(command[2])
        try:
            df = pd.read_csv('schematas.csv', converters={'DataBase': str}, keep_default_na=False, index_col=False)
        except FileNotFoundError:
            pass
        dx = copy.copy(df.loc[(df['DataBase'] == str(command[2]))])
        if dx.empty == False:
            print('Wrong! this database has exists o(╥﹏╥)o')
            return 0
        df = pd.read_csv('user_privileges.csv',
                         converters={'user_id': str, 'db_privilege': str, 'grant': str, 'create': str, 'select': str,
                                     'insert': str, 'delete': str, 'update': str, 'all': str}, keep_default_na=False)
        dx = copy.copy(df.loc[(df['user_id'] == self.id) & (df['all'] == 'yes')])
        if dx.empty == True:
            print('Wrong! you have no privilege on create database o(╥﹏╥)o')
        else:
            df = pd.read_csv('schematas.csv',
                             converters={'DataBase': str}, keep_default_na=False, index_col=0)  # 旧数据

            new_df = {'DataBase': [db_name]}
            dd = df.merge(DataFrame(new_df), how='outer')
            df = copy.copy(dd)
            df.to_csv('schematas.csv', mode='w')
            print(df)


    def use_db(self):
        # 去数据库表中检查是否有command[2]
        df = pd.read_csv('schematas.csv', converters={'DataBase': str}, keep_default_na=False)
        try:
            dx = copy.copy(df.loc[(df['DataBase'] == str(command[2]))])
            if dx.empty == True:
                print('Wrong! this database not exists o(╥﹏╥)o')
                return 0
            else:
                self.db = str(command[2])
                print('成功切换database为', self.db)
        except IndexError and Exception:
            print('Invalid command')


    def show_table_in(self):
        # select * from tables
        if command[2] == 'from':
            table_name = 'H:\\DATA\\' + str(command[3]) + '.csv'
            try:
                df = pd.read_csv(table_name, keep_default_na=False,dtype=str)
                print(df)
            except FileNotFoundError:
                print('File not exists! o(╥﹏╥)o')
                return 0
        else:
            print("Wrong! Invalid Format in '%s' " % (command[2]))
            return 0


    def show_tables(self):
        # 展示当前数据库中的表
        df = pd.read_csv('tables.csv', converters={'DataBase': str, 'table': str}, keep_default_na=False)
        dx = copy.copy(df.loc[(df['DataBase'] == self.db)])
        print(dx)


    def desc(self):
        #展示表结构
        table_name = str(command[1]).strip(';\n')
        df = pd.read_csv('columns.csv', converters={'DataBase': str, 'table': str, 'columns': str, 'not_null': str,
                                         'primary_key': str}, keep_default_na=False)
        dx = copy.copy(df.loc[(df['table'] == table_name)&(df['DataBase'] == self.db)])
        print(dx)


    def drop_tables(self):
        # 检查用户有无权限 检查表是否存在 删除tables columns 以及表文件
        table_name0 = str(command[2]).strip("\n;")
        df = pd.read_csv('user_privileges.csv', converters={'user_id': str, 'db_privilege': str, 'grant': str, 'create': str, 'select': str,
                                     'insert': str, 'delete': str, 'update': str, 'all': str}, keep_default_na=False)
        dx = copy.copy(df.loc[(df['delete'] == 'yes')&(df['user_id'] == self.id)&(df['db_privilege'] ==self.db )&(df['table']==table_name0)])
        print(dx)
        if dx.empty == True:
            print('Wrong! no privilege o(╥﹏╥)o')
            return 0
        else:
            df = pd.read_csv('tables.csv', converters={'DataBase': str, 'table':str}, keep_default_na=False)
            dx = copy.copy(df.loc[(df['DataBase'] == self.db)&(df['table'] == table_name0)])
            if dx.empty == True:
                print('Wrong! this table not exists o(╥﹏╥)o')
            else:
                # 开始删除操作
                df = df.drop(index=(df.loc[(df['table']==table_name0)].index))#删除table表中

                df.to_csv('tables.csv', mode='w', index=False)  #写回去

                df = pd.read_csv('columns.csv', converters={'DataBase': str, 'table': str, 'columns': str, 'not_null': str,
                                         'primary_key': str}, keep_default_na=False)

                df = df.drop(index=(df.loc[(df['table']==table_name0)].index))  #删除columns表
                try:
                    df.to_csv('columns.csv',mode='w',index=False)
                    table_name = 'H:\\DATA\\' +table_name0 + '.csv'
                    os.remove(table_name)
                    print('Success!!ヾ(✿ﾟ▽ﾟ)ノ')
                except FileNotFoundError:
                    print('暂无文件')


    def insert(self):
        # 检查表是否存在 插入数据表文件即可
        table_name = str(command[2]).strip('\n;')
        df = pd.read_csv('tables.csv', converters={'DataBase': str, 'table': str}, keep_default_na=False)
        dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)])
        if dx.empty == True:
            print('Wrong! this table not exists o(╥﹏╥)o')
        else:
            df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
            dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)])
            print('table desc,please insert according the sequence Thanks♪(･ω･)ﾉ \n ',dx)
            key = list(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)]['columns'])
            #print(key)
            all_data = {}
            while True:
                row_data = input("MySQL>column_name column_data ").strip(";'")
                #print(len(dx))
                if row_data != 'end':
                    new_data = row_data.strip("' ").split('=')
                    for i in range(len(new_data)):
                        new_data[i] = new_data[i].strip("' ")
                    try:
                        all_data[new_data[0]] = new_data[1].strip("' ")
                    except IndexError and Exception:
                        print('Invalid Command!')

                else:
                    #输入结束，检查主键是否为空,以及是否重复
                    print('ending...')
                    pri = str(list(dx.loc[(dx['primary_key'] == 'yes') ]['columns'])[0])
                    if (pri in all_data) == False:
                        print('Wrong! primary_key can not null')
                        return 0
                    else:
                        table_name1 = 'H:\\DATA\\' + table_name + '.csv'
                        df = pd.read_csv(table_name1, keep_default_na=False,dtype=str)
                        #print(all_data[pri])
                        print(all_data)
                        dx = copy.copy(df.loc[df[pri] == all_data[pri]])
                        print(dx)
                        if (dx.empty) == False:
                            print('Wrong! primary_key must be unique!o(╥﹏╥)o')
                            return 0
                        else:
                            print('all_data',all_data)

                            #更新索引
                            df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
                            dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)  & (df['is_index'] == 'yes')])
                            if dx.empty == True:
                                pass
                            else:
                                print('This columns has index !')
                                col_name = str(list(dx['columns'])[0])
                                print('col-name',col_name)
                                table_file = 'H:\\DATA\\' + table_name + '.csv'
                                test = pd.read_csv(table_file, keep_default_na=False)
                                keyname = []
                                for i in range(len(test.columns)):
                                    keyname.append(test.columns[i])
                                testlist = []
                                for i in range(len(test)):
                                    values = ''
                                    for j in range(1, len(keyname)):
                                        values += (str(test.loc[i][keyname[j]]) + ' ')
                                    testlist.append(KeyValue(test.loc[i][keyname[0]], values))
                                mybptree = Bptree(4, 4, col_name)
                                for x in testlist:
                                    mybptree.insert(x)
                                print('插入前')
                                mybptree.show()
                                print(all_data)
                                values = ''
                                for v in all_data:
                                    if v != pri:
                                        values += (str(all_data[v])+' ')
                                        print(values)
                                new_d = KeyValue(all_data[pri],values)
                                print(new_d)
                                mybptree.insert(new_d)
                                print('插入后.....')
                                mybptree.show()

                            df = pd.read_csv(table_name1, keep_default_na=False,dtype=str)  # 旧数据

                            dd = df.merge(DataFrame(all_data,index=[0]), how='outer')
                            df = copy.copy(dd)
                            df.to_csv(table_name1, mode='w', index=False)

                            print('Success!ヾ(✿ﾟ▽ﾟ)ノ')
                            return 0


    def update(self):
        #检查表是否存在 检查位置 修改数据表
        #update student set sname = '小李' where sno='1';

        table_name = str(command[1]).strip('\n;')
        df = pd.read_csv('tables.csv', converters={'DataBase': str, 'table': str}, keep_default_na=False)
        dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)])
        if dx.empty == True:
            print('Wrong! this table not exists o(╥﹏╥)o')
        else:
            table_name1 = 'H:\\DATA\\' + table_name + '.csv'
            command1 = input('set>>').strip('\n; ').split('=')  # 新值
            i = 0
            old_command = []
            while True:
                old_command.append(input('where>>'))
                if old_command[i] == 'end':
                    old_command.remove('end')
                    break
                else:
                    i += 1

            command1[0] = command1[0].strip(' ')
            command1[1] = command1[1].strip("' ")
            df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
            # 检查新值是不是主键-检查columns表 是主键的话 检查值是否存在 存在不能修改
            dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name) & (
                    df['columns'] == command1[0]) & (df['primary_key'] == 'yes')])
            flag = 0
            try:
                if dx.empty == False:
                    df = pd.read_csv(table_name1, dtype=str, keep_default_na=False)
                    flag = 1  # 是主键
                    dx = copy.copy(df.loc[df[command1[0]] == command1[1]])  # 找重复值
                    if dx.empty == False:
                        print('Wrong! primary key must be unique o(╥﹏╥)o')
                        flag = 2  # 是主键并且值重复
                if flag == 0:  # 不是主键
                    df = pd.read_csv(table_name1, dtype=str, keep_default_na=False)
                    if len(old_command) == 0:
                        if flag == 0:
                            # where子句为空 整张表的列全部修改
                            df[command1[0]] = command1[1]
                        else:
                            print('Wrong! primary key must be unique o(╥﹏╥)o')
                    else:
                        for i in range(len(old_command)):
                            command[i] = old_command[i].strip('\n; ').split('=')
                            command[i][0] = command[i][0].strip(' ')
                            command[i][1] = command[i][1].strip("' ")
                        if len(old_command) == 2:
                            L = list(
                                df[(df[command[0][0]] == command[0][1]) & (df[command[1][0]] == command[1][1])].index)
                        else:
                            L = list(df[df[command[0][0]] == command[0][1]].index)
                        if len(L) > 1:
                            for i in range(len(L)):
                                df.loc[L[i], command1[0]] = command1[1]
                        else:
                            df.loc[L[0], command1[0]] = command1[1]

                    df.to_csv(table_name1, mode='w', index=False)
                    print('Success!ヾ(✿ﾟ▽ﾟ)ノ')

            except TypeError:
                print('Invalid type!')


    def alter_add(self):
        # 检查表是否存在 列是否存在 修改columns表即可
        # alter table students add columns phonenumber string(32) not_null primary_key
        table_name = str(command[2]).strip('\n;')
        df = pd.read_csv('tables.csv', keep_default_na=False, dtype=str)
        dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)])
        if dx.empty == True:
            print('Wrong! this table not exists o(╥﹏╥)o')
        else:
            df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
            dx = copy.copy(df.loc[(df['columns'] == command[5])])
            if dx.empty == False:
                print('Wrong! this column has exists o(╥﹏╥)o')
            else:
                df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)  # 旧数据
                c1 = input("not_null>>").strip("';\n ")
                c2 = input('primary_key>>').strip("';\n ")
                new_df = {'DataBase': [self.db], 'table': [table_name], 'columns': [command[5]],
                          'data_type': [command[6]], 'not_null': [c1],
                          'primary_key': [c2]}

                print(new_df)
                dd = df.merge(DataFrame(new_df), how='outer')
                df = copy.copy(dd)
                df.to_csv('columns.csv', mode='w', index=False)
                print('Success!ヾ(✿ﾟ▽ﾟ)ノ')


    def alter_drop(self):
        # 检查表是否存在 列是否存在 修改columns表,以及数据表的列删除
        #alter table students drop phone
        table_name = str(command[2]).strip('\n;')
        table_name1 = 'H:\\DATA\\'+ table_name +'.csv'
        col_name = str(command[4]).strip(';\n ')
        df = pd.read_csv('tables.csv', keep_default_na=False, dtype=str)
        dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)])
        if dx.empty == True:
            print('Wrong! this table not exists o(╥﹏╥)o')
        else:
            df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
            dx = copy.copy(df.loc[(df['columns'] == col_name)])
            if dx.empty == True:
                print('Wrong! this column no exists o(╥﹏╥)o')
            else:
                df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)  # 旧数据
                df = df.drop(index=(df.loc[(df['columns']==col_name )].index))
                df.to_csv('columns.csv', mode='w', index=False)
                print('columns表修改成功')
                df = pd.read_csv(table_name1, dtype=str, keep_default_na=False)  # 旧数据
                try:
                    df = df.drop(columns=str(col_name))
                    df.to_csv(table_name1, mode='w', index=False)
                    print('Success!ヾ(✿ﾟ▽ﾟ)ノ')
                except KeyError:
                    print('此列中暂无数据')


    def grant(self):
        #检查权限grant是否为yes 检查关系用户是否存在 修改user_privilege表
        #grant select on students to gaogao
        grant_name = str(command[1]).strip('\n ')
        if str(command[2]) == 'on':
            table_name = str(command[3]).strip('\n ')
            if command[4] == 'to':
                user_name = str(command[5]).strip('\n ')
            else:
                print("Wrong! Invalid Format in '%s' " % (command[4]))
        else:
            print("Wrong! Invalid Format in '%s' " % (command[2]))
        # 检查本用户权限
        df = pd.read_csv('user_privileges.csv', dtype=str, keep_default_na=False)
        dx = copy.copy(df.loc[(df['user_id'] == self.id) & (df['db_privilege'] == self.db) &(df['grant'] == 'yes')])
        if dx.empty == True:
            print('Wrong! you have no privilege  o(╥﹏╥)o')
        else:
            df = pd.read_csv('tables.csv', dtype=str, keep_default_na=False)
            dx = copy.copy(
                df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)])
            if dx.empty == True:
                print('Wrong! this table has no exist o(╥﹏╥)o')
            else:
                df = pd.read_csv('users.csv', dtype=str, keep_default_na=False)
                dx = copy.copy(df.loc[(df['user_id'] == user_name)])
                if dx.empty == True:
                    print('Wrong! this user has no exist o(╥﹏╥)o')
                else:
                    df = pd.read_csv('user_privileges.csv', dtype=str, keep_default_na=False)
                    # grant select on students to gaogao
                    print(grant_name)
                    df.loc[list(df[(df['user_id'] == user_name)&(df['db_privilege'] == self.db)&(df['table'] == table_name)].index)[0], grant_name] = 'yes'
                    df.to_csv('user_privileges.csv', mode='w', index=False)
                    print(df['select'])
                    print('Success!ヾ(✿ﾟ▽ﾟ)ノ')


    def revoke(self):
        # 检查权限grant是否为yes 检查关系用户是否存在 修改user_privilege表
        # revoke select on students from gaogao
        grant_name = str(command[1]).strip('\n ')
        if str(command[2]) == 'on':
            table_name = str(command[3]).strip('\n ')
            if command[4] == 'from':
                user_name = str(command[5]).strip('\n ')
            else:
                print("Wrong! Invalid Format in '%s' " % (command[4]))
        else:
            print("Wrong! Invalid Format in '%s' " % (command[2]))
        # 检查本用户权限
        df = pd.read_csv('user_privileges.csv', dtype=str, keep_default_na=False)
        dx = copy.copy(df.loc[(df['user_id'] == self.id) & (df['db_privilege'] == self.db) & (df['grant'] == 'yes')])
        if dx.empty == True:
            print('Wrong! you have no privilege  o(╥﹏╥)o')
        else:
            df = pd.read_csv('tables.csv', dtype=str, keep_default_na=False)
            dx = copy.copy(
                df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name)])
            if dx.empty == True:
                print('Wrong! this table has no exist o(╥﹏╥)o')
            else:
                df = pd.read_csv('users.csv', dtype=str, keep_default_na=False)
                dx = copy.copy(df.loc[(df['user_id'] == user_name)])
                if dx.empty == True:
                    print('Wrong! this user has no exist o(╥﹏╥)o')
                else:
                    df = pd.read_csv('user_privileges.csv', dtype=str, keep_default_na=False)
                    # grant select on students to gaogao
                    df.loc[list(df[(df['user_id'] == user_name) & (df['db_privilege'] == self.db) & (
                                df['table'] == table_name)].index)[0], grant_name] = 'no'
                    df.to_csv('user_privileges.csv', mode='w', index=False)
                    print(df['select'])
                    print('Success!ヾ(✿ﾟ▽ﾟ)ノ')


    def delete(self):
        #delete from 关系名 where ** 如果where为空 直接删除整个表 sno=''
        table_name = command[2].strip("' ")
        location = input("where>>")
        print(location)
        if len(location)== 0:
            # 表示删除整张表
            user.drop_tables()
        else:
            location1 = location.strip("' ").split('=')
            col_name = location1[0]
            d_data =location1[1].strip("' ")
            table_name1 = 'H:\\DATA\\' +table_name + '.csv'
            df = pd.read_csv(table_name1, dtype=str, keep_default_na=False)  # 旧数据
            #print(df)
            #try:
            dx = copy.copy(df.loc[df[col_name] == d_data])
            if dx.empty == True:
                print('Wrong! this data not exists o(╥﹏╥)o')
            else:
                # print(df)
                # 检查这个列是否有索引 如果有修改索引
                df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
                dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name) & (
                        df['columns'] == col_name) & (df['is_index'] == 'yes')])
                if dx.empty == True:
                    pass
                else:
                    print('This columns has index !')
                    table_file = 'H:\\DATA\\' + table_name + '.csv'
                    test = pd.read_csv(table_file, keep_default_na=False)
                    keyname = []
                    for i in range(len(test.columns)):
                        keyname.append(test.columns[i])
                    testlist = []
                    for i in range(len(test)):
                        values = ''
                        for j in range(1, len(keyname)):
                            values += (str(test.loc[i][keyname[j]]) + ' ')
                        testlist.append(KeyValue(test.loc[i][keyname[0]], values))
                    mybptree = Bptree(4, 4, col_name)
                    for x in testlist:
                        mybptree.insert(x)
                    print('删除前.....')
                    mybptree.show()
                    mybptree.delete(int(d_data))
                    print('删除后.....')
                    mybptree.show()

                # 开始删除操作
                df = pd.read_csv(table_name1, dtype=str, keep_default_na=False)  # 旧数据
                df = df.drop(index=(df.loc[(df[col_name] == d_data)].index))  # 删除表中该行数据
                df.to_csv(table_name1, mode='w', index=False)

            print('Success!ヾ(✿ﾟ▽ﾟ)ノ')
            #except KeyError:
                #print('----------------------')


    def create_index(self):
        #为某一个属性创建B+树索引 同时修改数据字典 columns 改为'yes'
        # alter table students add index 'sno'
        table_name = command[2]
        col_name = command[5].strip("' ")

        # 检查有没有这列 如果有修改数据字典中的权限 生成索引文件。。。
        df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
        dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name) & (
                df['columns'] == col_name)])
        if dx.empty==True:
            print('Sorry! This column has no exists ~~o(>_<)o ~~')
        else:
            df.loc[list(df[(df['DataBase'] == self.db)&(df['table'] == table_name)& (df['columns'] == col_name)].index)[0], 'is_index'] = 'yes'
            df.to_csv('columns.csv', mode='w', index=False)

            table_file = 'H:\\DATA\\' + table_name + '.csv'
            test = pd.read_csv(table_file, keep_default_na=False)
            keyname = []
            for i in range(len(test.columns)):
                keyname.append(test.columns[i])
            testlist = []
            for i in range(len(test)):
                values = ''
                for j in range(1,len(keyname)):
                    values += (str(test.loc[i][keyname[j]])+' ')
                print(values)
                testlist.append(KeyValue(test.loc[i][keyname[0]],values))
            # 初始化B树
            mybptree = Bptree(4, 4,col_name)
            # 插入操作
            for x in testlist:
                mybptree.insert(x)

            mybptree.show()


    def drop_index(self):
        #删除索引
        # alter table students drop index sno
        table_name = command[2]
        col_name = command[5].strip("' ")

        # 检查有没有这列 如果有修改数据字典中的权限 生成索引文件。。。
        df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
        dx = copy.copy(df.loc[(df['DataBase'] == self.db) & (df['table'] == table_name) & (
                df['columns'] == col_name)&(df['is_index']=='yes')])
        if dx.empty == True:
            print('Sorry! This column has no index ~~o(>_<)o ~~')
        else:
            df.loc[
                list(df[(df['DataBase'] == self.db) & (df['table'] == table_name) & (df['columns'] == col_name)].index)[
                    0], 'is_index'] = 'no'
            df.to_csv('columns.csv', mode='w', index=False)
            index_name = col_name+'_index.txt'
            try:
                os.remove(index_name)
            except FileNotFoundError:
                print('This index has no index_file！')
            print('Success!φ(≧ω≦*)♪ ')


    def optimization(self):
        # 根节点
        if command[1] != '*':
            choose_cols = command[1].strip("' ").split(",")
            print("select :", choose_cols)
        else:
            choose_cols = '*'

        # 叶子结点
        c = ''
        tables = []
        while c != 'end':
            c = input('from>>').strip("'\n ")
            tables.append(c)
        tables.remove('end')
        print('from: ', tables)

        conditions = []
        c = ''
        while c != 'end':
            c = input('where>>').strip("'\n ")
            conditions.append(c)
        conditions.remove('end')
        print('where : ', conditions)

        for i in range(len(tables)):
            file_s = 'new_'+tables[i]+'.csv'
            file_n = 'temp_'+tables[i]+'.csv'
            try:
                os.remove(file_s)
                os.remove(file_n)
            except FileNotFoundError and Exception:
                pass


        # 先对关系创建投影列表
        if choose_cols == '*':  # 如果是* 那么应该直接将整个文件的列加入投影列表
            choose_cols = []
            projections = [[] for row in range(len(tables))]
            df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
            for v in range(len(tables)):
                dx = copy.copy(df.loc[(df['table'] == tables[v]), 'columns'])
                if dx.empty == False:
                    for j in list(dx):
                        projections[v].append(j)
                        choose_cols.append(j)
        else:
            projections = [[] for row in range(len(tables))]
            df = pd.read_csv('columns.csv', dtype=str, keep_default_na=False)
            for v in range(len(tables)):
                for i in range(len(choose_cols)):
                    # 从columns文件中获取每个关系列都添加到投影列表中
                    dx = copy.copy(df.loc[(df['table'] == tables[v]) & (df['columns'] == choose_cols[i])])
                    print(dx)
                    if dx.empty == False:
                        projections[v].append(choose_cols[i])
            print(projections)

        select_no = []  # 记录选择操作的条件的关系名以及条件号
        select_name = []

        if len(conditions) == 0:
            temp = copy.copy(tables)
        else:
            # 检查连接和选择条件
            for i in range(len(conditions)):  # 3个条件
                flag = 1
                if ('>' in conditions[i]):
                    condition = conditions[i].strip("' ").split('>')
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                elif ('<' in conditions[i]):
                    condition = conditions[i].strip("' ").split('<')
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                elif ('>=' in conditions[i]):
                    condition = conditions[i].strip("' ").split('>=')
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                elif ('<=' in conditions[i]):
                    condition = conditions[i].strip("' ").split('<=')
                    print(condition)
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                elif '=' in conditions[i]:
                    condition = conditions[i].strip("' ").split('=')
                    print(condition)
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                    condition2 = str(condition[1]).split('.')  # 0 --关系 1--列
                    if len(condition1) == 2:
                        if len(condition2) == 2:
                            flag = 0

                if flag == 1:
                    k = 0
                    for j in range(len(tables)):
                        if tables[j] == condition1[0]:
                            k = j  # 标记关系在table中的位置
                    select_no.append(k)
                    select_name.append(tables[k])
                    try:
                        if (condition1[1] in projections[k]):
                            pass
                        else:
                            projections[k].append(condition1[1])

                        k = 0
                        for j in range(len(tables)):
                            if tables[j] == condition1[0]:
                                k = i  # 标记关系在table中的位置
                        if (condition1[1] in projections[k]):
                            pass
                        else:
                            projections[k].append(condition1[1])
                    except IndexError and Exception:
                        print('please check your input!')

                elif flag == 0:
                    k = 0
                    for j in range(len(tables)):
                        if tables[j] == condition1[0]:
                            k = j  # 标记关系在table中的位置

                    if (condition1[1] in projections[k]):
                        pass
                    else:
                        projections[k].append(condition1[1])

                    k = 0
                    for j in range(len(tables)):
                        if tables[j] == condition1[0]:
                            k = i  # 标记关系在table中的位置
                    if (condition1[1] in projections[k]):
                        pass
                    else:
                        projections[k].append(condition1[1])

                    k = 0
                    for j in range(len(tables)):
                        if tables[j] == condition2[0]:
                            k = j  # 标记关系在table中的位置
                    if (condition2[1] in projections[k]):
                        pass
                    else:
                        projections[k].append(condition2[1])
                    k = 0
                    for j in range(len(tables)):
                        if tables[j] == condition2[0]:
                            k = i  # 标记关系在table中的位置
                    if (condition2[1] in projections[k]):
                        pass
                    else:
                        projections[k].append(condition2[1])

            for j in range(len(select_no)):
                print(conditions[select_no[j]])
                print(select_name[j])

        print("优化后得到每个关系应该投影出的列：", projections)
        # 将每个关系应该投影出的列暂存到内存中 以及选择条件进行筛选
        for i in range(len(tables)):
            file_name = 'H:\\DATA\\' + tables[i] + '.csv'
            new_file_name = 'temp_' + tables[i] + '.csv'

            if tables[i] in select_name:  # 该关系有选择操作
                df = pd.read_csv(file_name, dtype=str, keep_default_na=True)
                k = 0
                for j in range(len(select_name)):
                    if tables[i] == select_name[j]:
                        k = j
                print(conditions[select_no[k]])  # 打印出选择条件 进行分析
                c = str(conditions[select_no[k]])
                flag = 0
                if ('>=' in c):
                    condition = c.strip("' ").split('>=')
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                    flag = 3
                elif ('<=' in c):
                    condition = c.strip("' ").split('<=')
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                    flag = 4
                elif ('>' in c):
                    condition = c.strip("' ").split('>')
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                    flag = 1
                elif ('<' in c):
                    condition = c.strip("' ").split('<')
                    condition1 = str(condition[0]).split('.')  # 0 --关系 1--列
                    flag = 2
                elif ('=' in c):
                    condition = c.strip("' ").split('=')
                    condition1 = str(condition[0]).split('.')
                    flag = 5
                else:
                    print('Wrong!')
                print(projections[i])
                if flag == 1:
                    dx = copy.copy(df.loc[df[condition1[1]] > condition[1], projections[i]])
                elif flag == 2:
                    dx = copy.copy(df.loc[df[condition1[1]] < condition[1], projections[i]])
                elif flag == 3:
                    dx = copy.copy(df.loc[df[condition1[1]] >= condition[1], projections[i]])
                elif flag == 4:
                    dx = copy.copy(df.loc[df[condition1[1]] <= condition[1], projections[i]])
                elif flag == 5:
                    dx = copy.copy(df.loc[df[condition1[1]] == condition[1], projections[i]])
                dx.to_csv(new_file_name, index=False)
            else:
                try:
                    df = pd.read_csv(file_name, dtype=str, keep_default_na=True)
                    dx = copy.copy(df[projections[i]])
                    dx.to_csv(new_file_name, index=False)
                except FileNotFoundError and Exception:
                    print('File cannot found,please check your input!')
        print('Success! You can check the projected operation result!')
        print('选择和投影后读入内存已经结束...')

        if conditions != []:
            # 处理relationship
            relationship = copy.copy(tables)
            connect = []  # 用于记录分析后的连接的条件
            for i in range(len(conditions)):
                if i not in select_no:
                    # 不是选择操作,分析条件，调用连接函数
                    connect.append(conditions[i])
            if len(connect) == 2 and len(relationship) == 3:  # 如果是三张表进行连接
                if (relationship[0] in connect[0]) and (relationship[0] in connect[1]):
                    temp = relationship[0]
                    relationship[0] = relationship[1]
                    relationship[1] = temp
                elif (relationship[1] in connect[0]) and (relationship[1] in connect[1]):
                    temp = relationship[1]
                elif (relationship[2] in connect[0]) and (relationship[2] in connect[1]):
                    temp = relationship[2]
                    relationship[2] = relationship[1]
                    relationship[1] = temp
                else:
                    print('Wrong!')
                linkage_operation(relationship[0], relationship[1], connect[0], temp)
                linkage_operation(relationship[1], relationship[2], connect[1], temp)
            elif len(connect) == 0 and len(relationship) == 1:
                # 如果是单张表筛选
                temp = relationship[0]
                file_name0 = 'temp_' + relationship[0] + '.csv'
                file_name1 = 'new_' + relationship[0] + '.csv'
                data = pd.read_csv(file_name0, dtype=str)
                data.to_csv(file_name1, mode='w', index=False)
            else:  # 如果是两张表进行连接
                temp = relationship[0]  # 随意指定一个作为temp即可
                linkage_operation(relationship[0], relationship[1], connect[0], temp)
            print('连接操作结束，ending 可以检查结果中间文件')

        if type(temp) == str:
            new_file_name = 'new_' + temp + '.csv'
            # 最终投影操作
            df = pd.read_csv(new_file_name, dtype=str)
            dx = copy.copy(df[choose_cols])
            print('final_result:\n', dx)
        else:
            for i in temp:
                new_file_name = 'temp_' + i + '.csv'
                # 最终投影操作
                df = pd.read_csv(new_file_name, dtype=str)
                dx = copy.copy(df[choose_cols])
                print('final_result:\n', dx)


# user = User('gaohan','14562563')
print('************************************')
user_id = input('Enter ID：')
user_pwd = input('Enter password：')

#检查管理员密码
u = match_id_pwd(user_id,user_pwd)
if u == 1:
    print('Welcome to My DBMS (*^▽^*)  .....')
    user = User(user_id,user_pwd)
else:
    print('sorry! your password is Wrong! o(╥﹏╥)o')
    exit()
print('************************************')
while True:
    command = input('MySQL>').strip(';\n').split(' ')
    # 通过处理 识别命令
    #print(command)
    if command[0] == 'create':
        if command[1] == 'user':
            print('进入创建用户函数')
            user.create_user()
        elif command[1] == 'databases':
            print('进入创建数据库函数')
            user.create_bd()
        elif command[1] == 'tables':
            print('进入创建表函数')
            user.create_tables()
        else:
            print("Wrong!  Invalid Format in '%s' "%(command[1]))
    elif command[0] == 'select':
        # select
        user.optimization()
    elif command[0] == 'show':
        if command[1] == 'tables':
            user.show_tables()
        else:
            print("Wrong!  Invalid Format in '%s' "%(command[1]))
    elif command[0] == 'desc':
        user.desc()
    elif command[0] == 'alter':
        if command[1] == 'table' :
            if command[3] == 'add':
                if command[4] == 'columns':
                    user.alter_add()
                elif command[4] == 'index':
                    user.create_index()
                else:
                    print("Wrong!  Invalid Format in '%s " % command[4])
            elif command[3] == 'drop':
                if command[4] == 'index':
                    user.drop_index()
                else:
                    user.alter_drop()
            else:
                print("Wrong!  Invalid Format in '%s' "%command[3])
        else:
            print("Wrong!  Invalid Format in '%s' " % (command[1]))
    elif command[0] == 'use':
        if command[1] == 'databases':
            user.use_db()
        else:
            print("Wrong!  Invalid Format in '%s' "%(command[1]))
    elif command[0] == 'drop':
        if command[1] == 'tables':
            user.drop_tables()
        else:
            print("Wrong!  Invalid Format in '%s' "%(command[1]))
    elif command[0] == 'insert':
        if command[1]  == 'into':
            user.insert()
        else:
            print("Wrong!  Invalid Format in '%s' " % (command[1]))
    elif command[0] == 'update':
        user.update()
    elif command[0] == 'grant':
        user.grant()
    elif command[0] == 'revoke':
        user.revoke()
    elif command[0] == 'delete':
        if command[1] == 'from':
            user.delete()
        else:
            print("Wrong!  Invalid Format in '%s' " % (command[1]))
    elif command[0] == 'quit':
        exit()
    else:
        print('Invalid command')