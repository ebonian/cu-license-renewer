import json
import os
from renew import init_driver, borrow

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']  

def main():
    f = open('software.json')
    data = json.load(f)

    driver = init_driver() 

    for software in data:
        borrow(driver, USERNAME, PASSWORD, software['value'])
        print(f'Successfully borrowed {software["name"]}')

    driver.quit()

if __name__ == '__main__':
    main()