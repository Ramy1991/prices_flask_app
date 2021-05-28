from concurrent.futures import ThreadPoolExecutor
import requests
import os
import ijson


def save_image(url):
    # try:

    images = url[1].split('\n')

    if len(images) == 1:
        res = requests.get(url[1])
        # return res, url[0]
        directory = r'F:\images\{}\XXL'.format(url[0])
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = open(directory + '\\' + url[0] + '-1' + r".jpg", "wb")
        file.write(res.content)
        file.close()
    else:
        n = 1
        for img_link in images:
            res = requests.get(img_link)
            directory = r'F:\images\{}\XXL'.format(url[0])
            if not os.path.exists(directory):
                os.makedirs(directory)
            file = open(directory + '\\' + url[0] + '-1' + r".jpg", "wb")
            file.write(res.content)
            file.close()

    # except requests.exceptions.MissingSchema:
    #     pass


data = ijson.parse(open(r'C:\Users\ramyg\Downloads\products_ (1).json', encoding="utf8"))
item = []
num = 1
images_batch = []
for prefix, event, value in data:
    if prefix == 'item.data.item.unique_product_code' or prefix == 'item.data.item.images_url':
        item.append(value)

        # if num > 38327:
        if len(item) == 2:
            images_batch.append(item)
            item = []
            # print(len(images_batch))
            if len(images_batch) == 1000:
                with ThreadPoolExecutor(max_workers=20) as executor:
                    results = executor.map(save_image, images_batch)
                    for r in results:
                        print(r)
                images_batch = []
            num = num + 1
            # print(num)

            # if len(images) == 1:
            #     save_image(''.join(images), item[0], 1)
            # else:
            #     n = 1
            #     for img in images:
            #         save_image(img, item[0], n)
            #         n = n + 1
            # print(str(num) + '- ' + str(item[0]))
            # num = num + 1
            # item = []
        # else:
        #     if len(item) == 2:
        #         item = []
        #         print('pass- ' + str(num))
        #         num = num + 1
