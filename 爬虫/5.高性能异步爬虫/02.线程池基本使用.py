import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool


def get_page(str):
    print('正在下载：', str)
    time.sleep(2)
    print('下载成功：', str)


name_list = ['kk', 'aa', 'xx', 'cc']

# 使用单线程串行的方式执行
# 开始时间
start_time1 = time.time()
for name in name_list:
    get_page(name)
# 结束时间
end_time1 = time.time()

print('=====================')
# 使用线程池
# 实例化一个线程池对象
pool = Pool(4)
start_time2 = time.time()
# 将列表中每一个元素传递给get_page进行处理
pool.map(get_page, name_list)
end_time2 = time.time()

pool.close()
pool.join()

print('单线程需%ds' % (end_time1-start_time1))
print('线程池需%ds' % (end_time2-start_time2))
