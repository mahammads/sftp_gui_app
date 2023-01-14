import pysftp as sftp
import os 
from datetime import date
from pathlib import Path

class SftpModule:
    def __init__(self,FTP_HOST, FTP_USER, FTP_PASS, PORT=22):
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
       
        except Exception as e:
            raise e

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
                return 'File uploaded successfully'
            else:
                return 'please provide valid file name'
        except Exception as e:
            raise e

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
        except:
            pass

    def sftp_remove(self, file_name):
        try:
            if self.sftp.isdir(file_name):
                for item in self.sftp.listdir(file_name):
                    self.sftp.remove(item) 
            self.sftp.remove(file_name)
            return 'File removed successfully'
        except Exception as e:
            raise e
            
    def sftp_close(self):
        self.sftp.close()

if __name__ == "__main__":
    pass
# # download_sftp('data','myfile.zip')
# FTP_HOST =  '54.236.252.50'
# FTP_USER = 'mdjuber'
# FTP_PASS = 'Mjaas@31193'
# port=22
# obj = SftpModule(FTP_HOST,FTP_USER,FTP_PASS,port)
# result = obj.upload_sftp(local_file_name = r"C:\Users\sarwa\Downloads\1672916981-test.xlsx", sftp_folder_name='juber/code')
# # obj.download_sftp(sftp_file_path = 'output1.log')
# # result = obj.sftp_get_list()