import ftplib
import os

host = '1.254.87.254'
port = 3325
id = 'ftp_user'
pw = '1q2w3e4r1!'

file_name = 'test.png'
file_path = 'C:\\Users\\user\\Desktop\\'

try:
    ftp=ftplib.FTP()
    ftp.connect(host=host,port=port)
    ftp.login(id,pw)
    ftp.cwd("./sample")
    sf = open(file=file_path+file_name,mode='rb')
    ftp.storbinary('STOR '+file_name,sf)
    print(ftp.dir())

except Exception as e:
    print(e)