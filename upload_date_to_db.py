import requests
import ijson
import uuid
import re
from fake_useragent import UserAgent
import datetime
from datetime import date
import json

now = datetime.datetime.now()

url = 'http://api-v1.onlinewebshop.net/'

data = ijson.parse(open(r'C:\Users\ramyg\Downloads\products2 (1).json', encoding="utf8"))
n = 1
items = []
item = []


# executable_path = r'C:\Users\ramyg\Downloads\chromedriver.exe'
# os.environ['webdriver.chrome.driver'] = executable_path
#
# driver = webdriver.Chrome(executable_path=executable_path)
#
# driver.get('https://supportindeed.com/phpMyAdmin4/?db=2757812_bprice')
# driver.find_element_by_xpath('//*[@id="input_username"]').send_keys('2757812_bprice')
# driver.find_element_by_xpath('//*[@id="input_password"]').send_keys('offer0000')
# driver.find_element_by_xpath('//*[@id="input_go"]').submit()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="topmenu"]/li[2]/a').click()
# time.sleep(2)
#
# driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_xpath(
#     '//*[@id="sqlquerycontainerfull"]'),
#                       'SELECT count(*) FROM products')
#
# driver.find_element_by_xpath('//*[@id="button_submit_query"]').click()
# time.sleep(6)

def user_agent():
    return re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 12;)"


for prefix, event, value in data:
    
    if prefix == 'item.data.item.Unique_Product_Code':
        Unique_Product_Code = value
        item.append(Unique_Product_Code)
    elif prefix == 'item.data.item.Website_Name':
        Website_Name = value
        item.append(Website_Name)
    elif prefix == 'item.data.item.UIC':
        UIC = 'A' + str(uuid.uuid4())[-5:] + str(uuid.uuid4())[:4]
        item.append(UIC)
    # elif prefix == 'item.data.item.URL_EN':
    #     URL_EN = value
    #     item.append(URL_EN)
    # elif prefix == 'item.data.item.URL_AR':
    #     URL_AR = value
    #     item.append(URL_AR)
    # elif prefix == 'item.data.item.Cate_URL_EN':
    #     Cate_URL_EN = value
    #     item.append(Cate_URL_EN)
    # elif prefix == 'item.data.item.Cate_URL_AR':
    #     Cate_URL_AR = value
    #     item.append(Cate_URL_AR)
    elif prefix == 'item.data.item.Country':
        Country = 'eg'
        item.append(Country)
    # elif prefix == 'item.data.item.sub_category_URL_EN':
    #     sub_category_URL_EN = value
    #     item.append(sub_category_URL_EN)
    elif prefix == 'item.data.item.sub_category_en':
        sub_category_en = value
        item.append(sub_category_en)
    elif prefix == 'item.data.item.sub_category_ar':
        sub_category_ar = value
        item.append(sub_category_ar)
    elif prefix == 'item.data.item.Item_Type_EN':
        Item_Type_EN = value
        item.append(Item_Type_EN)
    elif prefix == 'item.data.item.Item_Type_AR':
        Item_Type_AR = value
        item.append(Item_Type_AR)
    elif prefix == 'item.data.item.Title_EN':
        Title_EN = value
        item.append(Title_EN)
    elif prefix == 'item.data.item.Title_AR':
        Title_AR = value
        item.append(Title_AR)
    elif prefix == 'item.data.item.Brand_EN':
        Brand_EN = value
        item.append(Brand_EN)
    elif prefix == 'item.data.item.Brand_AR':
        Brand_AR = value
        item.append(Brand_AR)
    # elif prefix == 'item.data.item.Description_EN':
    #     Description_EN = value
    #     item.append(Description_EN)
    # elif prefix == 'item.data.item.Description_AR':
    #     Description_AR = value
    #     item.append(Description_AR)
    elif prefix == 'item.data.item.Item_Specs_en':
        Item_Specs_en = value
        att = re.findall(r'dt>(.*?)<.dt', Item_Specs_en)
        att_values = re.findall(r'dd>(.*?)<.dd', Item_Specs_en)
        specs = str(dict(zip(att, att_values)))
        item.append(re.sub(r"'", r'"', specs))
    elif prefix == 'item.data.item.Item_Specs_ar':
        Item_Specs_ar = value
        att = re.findall(r'dt>(.*?)<.dt', Item_Specs_ar)
        att_values = re.findall(r'dd>(.*?)<.dd', Item_Specs_ar)
        specs_ar = str(dict(zip(att, att_values)))
        item.append(re.sub(r"'", r'"', specs_ar))
    elif prefix == 'item.data.item.Images_URL':
        Images_URL = value
        item.append(Images_URL)
    elif prefix == 'item.data.item.Product_Direct_Link_EN':
        Product_Direct_Link_EN = value
        item.append(Product_Direct_Link_EN)
    elif prefix == 'item.data.item.Product_Direct_Link_AR':
        Product_Direct_Link_AR = value
        item.append(Product_Direct_Link_AR)
    elif prefix == 'item.data.item.Price_eg':
        Price_eg = value
        if Price_eg == 'None':
            Price_eg = ''

        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        price_dict = {
            'egp': {
                date_time: {
                    'date_time': date_time,
                    'price': str(Price_eg),
                    'currency': 'egp'
                }
            }
        }
        # print(json.dumps(price_dict))
        item.append(json.dumps(price_dict))
        # print(json.dumps(price_dict))
    elif prefix == 'item.data.item.Item_UPC':
        Item_UPC = value
        item.append(Item_UPC)
    elif prefix == 'item.data.item.Sold_Out':
        Sold_Out = value
        item.append(Sold_Out)
    elif prefix == 'item.data.item.link_en':
        link_en = value
        item.append(link_en)
    elif prefix == 'item.data.item.link_ar':
        link_ar = value
        item.append(link_ar)
    elif prefix == 'item.data.item.item_date':
        item_date = re.search(r'item.(\d+.\d+.\d+)', Images_URL)
        try:
            item.append(item_date.group(1))
        except AttributeError:
            item.append(date.today())
        # print("', '".join(map(str, item)))
        if n > 7098:
            items.append("('" + "', '".join(map(str, item)) + "')")
            # print("('" + "', '".join(map(str, item)) + "')")
            if 340000 <= len(', '.join(items) + ';') <= 390000:
                # if len(items) == 1:
                items_to_set = ', '.join(items) + ';'
                query_string = "INSERT INTO products ( Unique_Product_Code, Website_Name, UIC," \
                               " Country, price_data, sub_category_en, sub_category_ar, Item_Type_EN," \
                               " Item_Type_AR, Title_EN, Title_AR, Brand_EN, Brand_AR," \
                               " Item_Specs_en, Item_Specs_ar, Images_URL, Product_Direct_Link_EN, Product_Direct_Link_AR,"\
                               " Item_UPC, Sold_Out, link_en, link_ar, item_date) " \
                               "VALUES {}".format(items_to_set)

                my_item = {'query': query_string}
                # print(query_string)
                print(str(len(query_string)) + '-' + str(n))
                # print(query_string)
                # header = {
                #     "User-Agent": user_agent(),
                #     "Accept": "*/*",
                #     "Accept-Language": "*/*",
                #     "Accept-Charset": "*/*",
                #     "Connection": "keep-alive",
                #     "Keep-Alive": "300"
                # }
                response = requests.post(url, data=my_item)
                print(str(Unique_Product_Code) + '-' + response.text + '-' + str(n))
                items = []

        n += 1
        item = []
        # 1108522 award space



        # update price important
        # souq sitemap https://egypt.souq.com/eg-en/sitemaps/sitemap-products-eg-en-16.xml

        # UPDATE
        # `products`
        # SET
        # `price_data` = JSON_INSERT(
        #     `price_data`,
        #     '$.egp."2021-04_22:14:17"',
        #     JSON_OBJECT("price", "300", "currency", "egp", "date_time", "2021-04-18 22:14:17")
        # )
        # WHERE
        # `Product_ID` = 6;
