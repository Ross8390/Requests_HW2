import requests

TOKEN = ''

class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self.get_upload_link(disk_file_path=disk_file_path).get('href','')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
   ya = YandexDisk(token=TOKEN)
   print(ya.get_files_list())
   print(ya.upload_file_to_disk('test1.txt','test.txt'))

