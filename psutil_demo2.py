
# coding: utf-8
import os
from psutil import cpu_percent
os.system('pip3 install pymysql')
import pymysql
from ftplib import FTP
import tarfile
import datetime
import re
'''
应用服务名称
cpu最大频率
cpu核心数

内存占用情况
磁盘分区情况
磁盘读写字节数
网络连接总数
发送字节数
接收字节数
-----
暂时没实现
备份文件体积
是否备份成功
-----
进程数
'''
#业务名称
app_name='db'
#FTP备份文件夹
#backupfiledir='/PG-MES-BACKUP'
#备份文件名称
#timepart=datetime.datetime.now().strftime("%Y%m%d")
#ftpfilename=timepart+'pgMES_51.tar.gz'

#print(ftpfilename)
#数据库连接串
#################################################################################################################
#文件保存ftp，参数，不变
'''ftpip='10.10.10.35'
ftpport=2111
ftpuser='by'
ftppass='xxxx'''
#结果写入mysql数据库，不变
dbreportdbname='dbareport'
dbreportip='10.10.10.138'
dbreportport=3306
dbreportuser='root'
dbreportpasswd=''
dbreportconninfo = pymysql.connect(host=dbreportip,user=dbreportuser,password=dbreportpasswd,database=dbreportdbname,port=int(dbreportport))
##################################################################################################################
def insertappreport(app_name,cpu_max_fre,cpu_copunts,mem_used,disk_part,disk_read_bytes,disk_write_bytes,net_connections,recv_bytes,sent_bytes,process_counts):

    cursor = dbreportconninfo.cursor()
    execstr="insert into appreport values ('%s',%s,'%s','%s',%s,%s,%s,'%s',%s,%s,%s)"%()
    cursor.execute(execstr)
    dbreportconninfo.commit()
    


try:
  import psutil
except:
  os.system('pip3 install psutil')
  import psutil
  print("psutil模块安装完毕")


#############################

def getdiskinfo():
  diskinfo=""
  diskreadrwinfo=""
  g=psutil.disk_partitions()
  diskcount=psutil.disk_io_counters(1)
  for t in diskcount:
      diskreadrwinfo=diskreadrwinfo+t+":   r_counts:"+str(diskcount[t][2])+" w_counts: "+str(diskcount[t][3])+"     "
      

  for i in g:
    
    if i[2]!='':
      t=psutil.disk_usage(i[0])

      
      diskinfo=diskinfo+i[0].replace('\\','').replace('\'','')+' FreeSpace:'+ str(int(t[2]/1024/1024/1024))+' Usedpercent:'+str(t[3])+'  '
   
  #print(diskreadrwinfo)
  return str(diskinfo),diskreadrwinfo
  pass

def getcpuinfo():
    cpucounts=psutil.cpu_count()
    cpumaxfre=psutil.cpu_freq()[2]
    cpupercent=psutil.cpu_percent()
    return cpucounts,cpumaxfre,cpupercent
    pass

def getmeminfo():
    mem=psutil.virtual_memory()
    #2是已用
    return mem[0],mem[2]
    pass

def getnetinfo():
    packages=psutil.net_io_counters()
    tt=psutil.net_connections()
    c=0
    for i in tt:
        c=c+1
     
    return packages,c
    pass

def getprocessnum():
  process_num=0
  for i in psutil.pids():
    process_num=process_num+1
  return process_num


'''
#确认备份状态
def ensurebackupstatus(filename):
  ftp=FTP()
  ftp.set_debuglevel(2)
  ftp.connect(ftpip,ftpport)
  ftp.login(ftpuser,ftppass)
  print(ftp.getwelcome)
  ftp.cwd(backupfiledir)
 # ftp.dir('20220405OAmysqlbackup.sql')
 # print('xxxxxxxx')
  ftpfilesize=str(ftp.size(filename))
  return ftpfilesize 
  pass


'''

def finalExec():
  cpu_cores=getcpuinfo()[0]

  systeminfo=getcpuinfo(),getdiskinfo(),getmeminfo()
  print(app_name)
  #cpu_max_fre
  print(getcpuinfo()[1])
  #cpu_core_counts
  print(getcpuinfo()[0])
  #mem_used  total/used
  print(str(getmeminfo()[0])+'/'+str(getmeminfo()[1]))
  #disk_part
  print(getdiskinfo()[0])
  #disk_IO_bytes
  print(getdiskinfo()[1])
  #net_connections
  print(getnetinfo()[1])
  #recv_bytes
  print(getnetinfo()[0][1])
  #sent_bytes
  print(getnetinfo()[0][0])
  #process_counts
  print(getprocessnum())
  #print(systeminfo)
  pass



finalExec()
