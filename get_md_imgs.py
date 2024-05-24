import re
import os
import requests
from PIL import Image
from io import BytesIO

os.makedirs(exist_ok=True, name='./data/')

# todo 获取 md 中的图片
file = open("README.md", "r")

pattern = r'http[s]{0,1}://pic[a-z0-9.]*/\d+/(?P<img>.*)(?=\))'

lines = file.readlines()

for line in lines:
    match = re.search(pattern, line)
    if match:
        url = match.group(0)
        img_name = match.group("img")

        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content

            image = Image.open(BytesIO(image_data))

            # 保存图片为JPG格式
            image.save(f"./data/{img_name}", 'JPEG')
        else:
            print('error.code:', response.status_code)

    continue
