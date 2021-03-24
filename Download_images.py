from concurrent.futures import ThreadPoolExecutor
import requests
import os
import ijson


def save_image(url, name, i):
    try:
        res = requests.get(url)
        directory = r'D:\Images\{}\XXL'.format(name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = open(directory + '\\' + name + '-' + str(i) + r".jpg", "wb")
        file.write(res.content)
        file.close()
    except requests.exceptions.MissingSchema:
        pass


data = ijson.parse(open(r'C:\products\products.json', encoding="utf8"))
item = []
num = 1
for prefix, event, value in data:
    if prefix == 'item.data.item.Unique_Product_Code' or prefix == 'item.data.item.Images_URL':
        item.append(value)
        if num > 38327:
            if len(item) == 2:
                images = item[1].split('\n')
                if len(images) == 1:
                    save_image(''.join(images), item[0], 1)
                else:
                    n = 1
                    for img in images:
                        save_image(img, item[0], n)
                        n = n + 1
                print(str(num) + '- ' + str(item[0]))
                num = num + 1
                item = []
        else:
            if len(item) == 2:
                item = []
                print('pass- ' + str(num))
                num = num + 1
