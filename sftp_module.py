import pysftp as sftp
import os 
from pathlib import Path
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
class SftpModule:
    def __init__(self, FTP_HOST, FTP_USER, FTP_PASS, PORT=22,):
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        self.host = FTP_HOST
        self.user = FTP_USER
        self.password = FTP_PASS
        self.port = PORT

        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        self.sftp = sftp.Connection(host=self.host, port=self.port, username=self.user, password=self.password, cnopts=cnopts)
        self.base_dir = Path(os.getcwd())
        print("connection established successfully")

    def download_sftp(self,local_file_path=None, sftp_file_path=None):
        try:
            serv_details = self.sftp
            current_dir = serv_details.pwd

            if local_file_path!= None:
                local_folder = local_file_path
            else:
                local_folder = os.getcwd()
            print(current_dir)

            if sftp_file_path!= None and serv_details.exists(sftp_file_path):
                if serv_details.isdir(sftp_file_path):
                    local_file = os.path.join(local_folder, sftp_file_path)
                    if not os.path.exists(local_file):
                        os.makedirs(local_folder +'/'+ sftp_file_path)
                    serv_details.get_d(sftp_file_path, local_file, preserve_mtime=True)

                if serv_details.isfile(sftp_file_path):
                    remote_file_path = current_dir + '/' + sftp_file_path
                    file = os.path.split(sftp_file_path)[-1]
                    local_file = local_folder + '/' + file
                    serv_details.get(remote_file_path, local_file, preserve_mtime=True)

                print(sftp_file_path,'downloaded successfully')
                return 'File downloaded successfully'
            else:
                return 'specified file not found'
       
        except Exception as err:
            raise err

    def upload_sftp(self, local_file_name = None, sftp_folder_name=None):
        try:
            serv_details = self.sftp
            server_home_dir = serv_details.pwd
            if sftp_folder_name!= None:
                remote_file_path = server_home_dir + '/' + sftp_folder_name
                if not serv_details.exists(remote_file_path):
                    serv_details.makedirs(remote_file_path)
            else:
                remote_file_path = serv_details.pwd

            if (local_file_name!= None) and (os.path.exists(local_file_name)):
                if os.path.isdir(local_file_name):
                    folder = os.path.split(local_file_name)[-1]
                    remote_file_path = remote_file_path + '/' + folder
                    if not serv_details.exists(remote_file_path):
                        serv_details.makedirs(remote_file_path)

                    for file in os.listdir(local_file_name):
                        file_name = os.path.join(local_file_name, file)
                        remote_file = remote_file_path + '/' + file
                        serv_details.put(file_name, remote_file, preserve_mtime=True)   

                if os.path.isfile(local_file_name):   
                    file_name = os.path.split(local_file_name)[-1]
                    remote_file =  remote_file_path +'/'+ file_name
                    serv_details.put(local_file_name, remote_file, preserve_mtime=True)

                print(local_file_name,'uploaded successfully')
                return "File uploaded successfully"
            else:
                return 'please provide valid file name'
        except Exception as err:
            raise err


    def sftp_get_list(self):
        try:
            serv_details = self.sftp
            print("connection established successfully")
            cur_dir = serv_details.pwd
            list_d = serv_details.listdir()
            print(list_d)
            input_folder = input('please enther the folder name:')
            serv_details.cwd(cur_dir+'/'+input_folder)
            list_d = serv_details.listdir()
            print(list_d)
            return list_d
        except Exception as err:
            raise err

    def sftp_remove(self, file_name):
        try:
            serv_details = self.sftp
            current_dir = serv_details.pwd
            remote_file_path = current_dir + '/' + file_name
            if serv_details.isdir(remote_file_path):
                for item in serv_details.listdir(remote_file_path):
                    item_path = remote_file_path + '/' + item
                    serv_details.remove(item_path) 
            else:
                serv_details.remove(remote_file_path)
            return 'File removed successfully'
        except Exception as err:
            raise err
            
    def sftp_close(self):
        self.sftp.close()

if __name__ == "__main__":
    pass
