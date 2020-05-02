
import paramiko
import warnings
import cryptography
import json
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)


class Sftp():

    def put(filename, localDirectory):
        with open('sftp.json') as f:
  			parameters = json.load(f)

        remoteDirectory = DIRECTORY

        host = parameters['host']
        port = parameters['port']
        
        username = parameters['user']
        password = parameters['pwd']
        
        transport = paramiko.Transport((host,port))
                  
        transport.connect(None,username,password)
            
        sftp = paramiko.SFTPClient.from_transport(transport)

        sftp.put(localDirectory + filename,remoteDirectory + filename)

        if sftp: sftp.close()
        if transport: transport.close()
