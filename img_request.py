# 基于图像id获取图像元数据
import requests
import json
# 访问令牌
access_token = 'MLYARAZAEl0kv3LZAW5IZAG0D5TOda4f1kKL2kJEGGNSW0tyxwtWWqBYBnesBLbCp5OjmG6mZCoDuMvtwWKuskD5QzW4CMwetrmdsDKZCkx4F9ZCvgQ3zu4s8Eq1wZCQT4KAZDZD'
# 该图像是武汉街景
image_id = '819055155387633'

# 获取图像元数据所有字段
url = 'https://graph.mapillary.com/{}?access_token={}&fields=altitude,atomic_scale,camera_parameters,camera_type,compass_angle,computed_altitude,computed_compass_angle,id,computed_geometry,thumb_256_url,thumb_1024_url,thumb_2048_url,thumb_original_url,sequence,mesh,sfm_cluster'.format(image_id,access_token)

proxy = {
    'http':'http://127.0.0.1:59527',
    'https':'http://127.0.0.1:59527'
}
# 返回值是json对象
r = requests.get(url=url,proxies=proxy)

# 把元数据保存成json格式
with open('wuhan.json', 'w') as f:
    json.dump(r.json(),f)
print('success')
