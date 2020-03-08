import requests
import urllib.request as url

def save_image(query,page,per_page,path_to_file):
    """

    :param query: what kind of image are you looking for (str)
    :param page: how many page to check (str)
    :param per_page: number of images (str)
    :path_to_file: where save all images (str)
    :return: save images in folder
    """
    r=requests.get('https://api.unsplash.com/search/collections?query={}&page={}&per_page={}&client_id=_xLRfYsPm2TAK5iZ8of4YszoUtaSQo0urSTENrvDi-A'.format(query,page,per_page))
    data = r.json()
    data.keys()
    for img_data in data['results']:
        file_name = path_to_file +'/'+str(img_data['id']) + ".jpg"
        print(file_name)
        img_url = img_data['cover_photo']['urls']['raw']
        suffix = '&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1920&fit=max'
        img_url = img_url + suffix
        print(img_url)
        url.urlretrieve(img_url, file_name)

save_image('sea','1','3','/Users/dariavolkova/Desktop/koo')
