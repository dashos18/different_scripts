import time
from PIL import ImageFilter
from PIL import Image
import concurrent.futures


img_names = ['/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1549692520-acc6669e2f0c.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1550439062-609e1531270e.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1493976040374-85c8e12f0c0e.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1504198453319-5ce911bafcde.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1507143550189-fed454f93097.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1513938709626-033611b8cc03.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1516117172878-fd2c41f4a759.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1516972810927-80185027ca84.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1522364723953-452d3431c267.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1524429656589-6633a470097c.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1530122037265-a5f1f91d3b99.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1530224264768-7ff8c1789d79.jpg',
             '/Users/dariavolkova/PycharmProjects/Different_scripts/Threads/photo-1532009324734-20a7a5813719.jpg']


t1 = time.perf_counter()

size = (1200,1200)


def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'{img_name}')
    print(f'{img_name} was processed...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')