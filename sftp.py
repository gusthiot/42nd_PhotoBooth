
import paramiko
import warnings
import cryptography
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)


class Sftp():

    def put(filename, localDirectory):
        
        remoteDirectory = DIRECTORY

        host = HOST
        port = PORT
        
        username = USER
        password = PWD
        
        transport = paramiko.Transport((host,port))
                  
        transport.connect(None,username,password)
            
        sftp = paramiko.SFTPClient.from_transport(transport)

        sftp.put(localDirectory + filename,remoteDirectory + filename)

        if sftp: sftp.close()
        if transport: transport.close()
