import json
import os
import renew

def main():
    f = open('software.json')
    data = json.load(f)

    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']   

    for i in data:
        renew(USERNAME, PASSWORD, i['value'])

if __name__ == '__main__':
    main()