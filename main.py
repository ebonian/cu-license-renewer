import json
import os
from renew import init_driver, borrow

def main():
    f = open('software.json')
    data = json.load(f)

    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']  

    driver = init_driver() 

    for i in data:
        borrow(driver, USERNAME, PASSWORD, i['value'])
        print(f'Successfully borrowed {i["name"]}')

    driver.quit()

if __name__ == '__main__':
    main()