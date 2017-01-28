import json
import redis

def set_redis_st(kv_data):
    conn = redis.Redis()
    for k,v in kv_data.items():
         conn.hmset(k,v)

def 

    
def main():
    json_datas = []
    kv_data = {}
    
    with open('artist.json','r') as f:
        for line in f:
            json_data = json.loads(line)
            json_datas.append(json_data)

    for data in json_datas:
        key = data['name']
        if 'area' in data:
            print(data['area'])
            value = data['area']
        else:
            value = "No Info"

        kv_data[key] = value

    print(kv_data)
    set_redis_st(kv_data)

    return(json_datas)

if __name__ == '__main__':
    json_datas = main()
#    print(json_datas)
