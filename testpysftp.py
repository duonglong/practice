import pysftp
# import paramiko

client = pysftp.Connection('211.25.102.2', username='40000108', password='DYobz1p')
print client.listdir()

