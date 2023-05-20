import psutil

# import psycopg2

# sourceuser="postgres"

# sourcepassword="postgres"

# sourcehost="10.10.10.138"

# sourceport=5432

# sourcedbname="dba"

# conn = psycopg2.connect(dbname=sourcedbname, user=sourceuser,password=sourcepassword, host=sourcehost, port=sourceport)

# cur=conn.cursor()

disklabel=['C:','D:','E:']

#获取磁盘信息

disktotalstr=""

diskfreestr=""

for i in disklabel:

    g=psutil.disk_usage(i)

    print(i,'total: ',g.total/1024/1024/1024,'GB')

    disktotalstr=disktotalstr+i+' '+ str(g.total/1024/1024/1024)+' '

    print(i,'free: ',g.free/1024/1024/1024,'GB')

    diskfreestr=diskfreestr+i+' '+ str(g.free/1024/1024/1024)+' '

#磁盘读写情况

#print(psutil.disk_io_counters(perdisk=True).keys())

for t in psutil.disk_io_counters(perdisk=True).keys():

    print(t)

    m=psutil.disk_io_counters(perdisk=True)[t]

    insertdriverstr="insert into Drivestatus values ('OATEST','%s',%s,%s,%s,%s"%(t,m[0],m[1],m[2],m[3])+',now())'

    # cur.execute(insertdriverstr)

    print(t,"read_count  :",m[0])

    print(t,"write_count  :",m[1])

    print(t,"read_bytes  :",m[2])

    print(t,"write_bytes  :",m[3])

    print(insertdriverstr)

    #read_count=147940, write_count=56915, read_bytes=4819768832, write_bytes=2194343936, read_time=388, write_time=215

mem=psutil.virtual_memory()

memtotal=mem[0]/1024/1024/1024

memavailable=mem[1]/1024/1024/1024

mempercent=mem[2]

memfree=mem[3]/1024/1024/1024

cpustatsstr=psutil.cpu_percent(interval=2,percpu = True)

insertserverstr="insert into serverstatus values ('OATEST','%s',%s,%s,%s,%s,'%s','%s'"%(cpustatsstr,memtotal,memavailable,mempercent,memfree,disktotalstr,diskfreestr)+',now())'

# cur.execute(insertserverstr)

# conn.commit()

disktotalstr=""

diskfreestr=""

