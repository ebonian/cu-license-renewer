import json
import os
from renew import init_driver, login, borrow, logout

def main():
    f = open('software.json')
    data = json.load(f)

    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']  

    driver = init_driver() 

    for i in data:
        login(driver, USERNAME, PASSWORD)
        borrow(driver, i['value'])
        logout(driver)

    driver.quit()

if __name__ == '__main__':
    main()