
import paramiko
import traceback
import logging
import json

import warnings
import cryptography


class Sftp:

    def __init__(self, mdir, withCam):
        if withCam:
            warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)
        self.logger = logging.getLogger(__name__)
        try :
            with open(mdir +'sftp.json') as f:
                parameters = json.load(f)
            self.host = parameters['host']
            self.port = parameters['port']
            self.username = parameters['user']
            self.password = parameters['pwd']
            self.sftp = None
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        except:
            self.logger.error(traceback.format_exc())

    def connect(self):
        try:
            self.client.connect(hostname=self.host,
                                port=self.port,
                                username=self.username,
                                password=self.password)
            self.sftp = self.client.open_sftp()
            return True
        except:
            self.logger.error(traceback.format_exc())
            return False

    def put(self, filename, localDir, remoteDir):
        if self.sftp:
            try:
                self.sftp.put(localDir + filename, remoteDir + filename)
                return True
            except:
                self.logger.error(traceback.format_exc())
        return False

    def close(self):
        if self.sftp:
            self.sftp.close()
        self.client.close()
