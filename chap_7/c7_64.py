import sys
import redis
import json

def set_redis_hash(kv_data):
    conn = redis.Redis()
    for key,value in kv_data.items():
        l = []
        v = {}
        n = 0
        for val in value:
            l.append(val['value'])
            n += int(val['count'])
        v['value'] = l
        v['count'] = n
        print(v)
        conn.hmset(key,v)
    
def main():
    json_datas = []
    kv_data = {}
    
    with open('artist.json','r') as f:
        for line in f:
            json_data = json.loads(line)
            json_datas.append(json_data)

    for data in json_datas:
        key = data['name']
        if 'tags' in data:
            print(data['tags'])
            value = data['tags']
        else:
            val = {}
            val['value'] = 'None'
            val['count'] = 0
            value = [val]
        

        kv_data[key] = value

#    print(kv_data)
    set_redis_hash(kv_data)

    return(json_datas)

if __name__ == '__main__':
    json_datas = main()
