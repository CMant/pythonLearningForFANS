```
#通过写一款监控脚本来入门python在运维当中的应用

  

#频繁读取服务器，执行脚本获取性能参数  可拉，可推

  

#  被监控服务器的连接信息

#  连接到服务器

#  一些读取linux性能参数的shell命令，bat，统一监控单位

#  把数据分门别类存入数据库

    #连接数据库

    #建表

#  ~~~做一个前台展示

#  发送告警邮件

  

import configparser

import paramiko

import time

import yagmail

  

def connServer_node(hostname,port,username,password,ctlcmd):

  
  

    ssh = paramiko.SSHClient()          #创建一个SSH客户端client对象

    #ssh.load_system_host_keys()         #获取客户端host_keys,默认~/.ssh/known_hosts,非默认路径需指定ssh.load_system_host_keys(/xxx/xxx)

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=hostname,port=port,username=username,password=password)    #创建SSH连接

    stdin,stdout,stderr = ssh.exec_command(ctlcmd)      #调用远程执行命令方法exec_command()

   # print(stdout.read().decode('utf-8'))        #打印命令执行结果，得到Python列表形式，可以使用stdout_readlines()

    result=stdout.read().decode('utf-8')

    ssh.close()

    return result

    pass

  
  

#连接数据库

import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres",

                        host="127.0.0.1", port=5432)

conn.set_client_encoding('UTF8')

cursor = conn.cursor()

  
  

cf = configparser.ConfigParser()

cf.read("C:\\Users\\m\\Desktop\\serverstatus1.conf")

print(cf.sections())

yag = yagmail.SMTP(user='useradmin@163.com', password='mailPassword', host='smtp.163.com')

  

def test_value(monitor_value):

    if monitor_value > 80:

            yag.send('sysadmin@qq.com','xxxx CPU HIGH',' ')

    if monitor_value > 90:

            yag.send('sysadmin@qq.com','xxxx CPU SOBUSY',' ')

    if monitor_value == 100:

            yag.send('sysadmin@qq.com','xxxx CPU DESTORY',' ')

    return 0

    pass

  
  

while(1):

    time.sleep(1)

    for i in cf.sections():

  

        print(i)

        server_stat_info=connServer_node(cf.get(i,"ip_address"),cf.get(i,"port"),cf.get(i,"username"),cf.get(i,"password"),"/home/root1/cc.sh")

        print(server_stat_info)

        test_value(server_stat_info)

       # root_path_used=connServer_node(cf.get(i,"ip_address"),cf.get(i,"port"),cf.get(i,"username"),cf.get(i,"password"),"df -h | grep /dev/mapper/vgubuntu-root | awk '{ print $5 }'")

     # total_mem=connServer_node(cf.get(i,"ip_address"),cf.get(i,"port"),cf.get(i,"username"),cf.get(i,"password"),"free -h | sed -n '2p'|awk '{print $2}'")

       # tuple_insert_str="insert into node_monitor_info values (nextval('node_monitor_info_seq'),'%s','%s','%s',now())"%(i,root_path_used.strip('\n'),total_mem.strip('\n'))

       # print(tuple_insert_str)

       # cursor.execute(tuple_insert_str)

       # conn.commit()

        # connServer_node(cf.get(i,"ip_address"),cf.get(i,"port"),cf.get(i,"username"),cf.get(i,"password"),"iostat")

        # connServer_node(cf.get(i,"ip_address"),cf.get(i,"port"),cf.get(i,"username"),cf.get(i,"password"),"cat /proc/cpuinfo")

        #awk,sed ,对你的执行结果进行筛选，处理

    # print(cf.get(i,"ip_address") + "  " + cf.get(i,"port") + " " + cf.get(i,"username") + " " + cf.get(i,"password") )
```
