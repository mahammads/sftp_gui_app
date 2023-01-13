import pysftp as sftp
import os 
from datetime import date

class SftpModule:
    def __init__(self,FTP_HOST, FTP_USER, FTP_PASS, PORT=22):
        self.host = FTP_HOST
        self.user = FTP_USER
        self.password = FTP_PASS
        self.port = PORT
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        self.sftp = sftp.Connection(host=self.host, port=self.port, username=self.user, password=self.password, cnopts=cnopts)
        print("connection established successfully")

    def download_sftp(self,local_folder_name=None, sftp_file_name=None):
        try:
            serv_details = self.sftp
            current_dir = serv_details.pwd

            if local_folder_name!= None:
                local_file_path = local_folder_name
            else:
                local_file_path = os.getcwd()
            print(current_dir)
            if sftp_file_name!= None:
                remote_file_path = current_dir + '/' + sftp_file_name
                local_file = local_file_path + '/' + sftp_file_name
                serv_details.get(remote_file_path, local_file)
                print(local_file,'downloaded successfully')

            else:
                print('specified file not found')
        except Exception as e:
            raise e

    def upload_sftp(self, local_file_name =None, sftp_folder_name=None):
        try:
            cnopts = sftp.CnOpts()
            cnopts.hostkeys = None
            serv_details = self.sftp
            print("connection established successfully")
            current_dir = serv_details.pwd
            if local_file_name!= None or local_file_name!= '':
                file_name = os.path.basename(local_file_name)
                if sftp_folder_name!= None:
                    if serv_details.exists(sftp_folder_name):
                        remote_file_path = sftp_folder_name +'/'+ file_name
                    else:
                        serv_details.makedirs(sftp_folder_name)
                        remote_file_path = sftp_folder_name +'/'+ file_name
                else:
                    remote_file_path = current_dir +'/'+ file_name
                
                serv_details.put(local_file_name, remote_file_path)
                print(local_file_name,'uploaded successfully')

            else:
                print('please provide valid file name')
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
        except Exception as e:
            raise e
            
    def sftp_close(self):
        self.sftp.close()

if __name__ == "__main__":
    pass
# download_sftp('data','myfile.zip')
# FTP_HOST =  '10.55.196.70'
# FTP_USER = 'mahammad138724'
# FTP_PASS = 'Mar@2022'
# port=22
# obj = SftpModule(FTP_HOST,FTP_USER,FTP_PASS,port)
# obj.upload_sftp(local_file_name = r"C:\Users\mahammad138724\Downloads\data.xlsx", sftp_folder_name='juber')
# obj.download_sftp(sftp_file_name = '')
# result = obj.sftp_get_list()