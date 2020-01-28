import json
import redis
import random
import os

redis_host = os.environ['REDIS_HOST']
redis_port = os.environ['REDIS_PORT']


r = redis.Redis(host=redis_host,port=redis_port)

def getUsers():
    keys = []
    for key in r.scan_iter():
        value = r.get(key)
        keys.append({'id': key.decode('ascii'),
                    'user': value.decode('ascii')})
    return {users: keys}, 200

def getUser(id)
    try:
        user = r.get(id)
        if user:
            return {'id': id,
                    'user': user.decode('ascii')
            }, 200
        else:
            return {'message': 'User not found!'}, 404
    except Exception as e:
        return {'message': str(e)}, 500

def setUser(user, id)
    try:
        r.set(id, user)
        return {'id': id,
                'user': user}, 201
    except Exception as e:
        return {'message': str(e)}, 500
        

def lambda_handler(event, context):
    id = random.randint(0, 1000000)
    if event['httpMethod'] == 'POST' and event['path'] == '/users':
        user = json.loads(event['body'])["user"]
        data,status = setUser(user, id)
    elif event['httpMethod'] == 'GET' and event['path'] != '/users':
        id = event['pathParameters']['id']
        data,status = getUser(id)
    elif event['httpMethod'] == 'GET' and event['path'] == '/users':
        data,status = getUsers()
    return {
        'statusCode': status,
        'body': json.dumps(data)
    }
