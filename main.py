import json
import os
from renew import init_driver, login, borrow

def main():
    f = open('software.json')
    data = json.load(f)

    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']  

    driver = init_driver() 

    login(driver, USERNAME, PASSWORD)
    for i in data:
        borrow(driver, i['value'])
        print(f'Successfully borrowed {i["name"]}')

    driver.quit()

if __name__ == '__main__':
    main()