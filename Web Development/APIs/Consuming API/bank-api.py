import requests
import copy
import json


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.access_token = None
        self.refresh_token = None
        self.token_timeout = None
        self.logged_in = False
        self.header = {
            "content-type": 'application/json'
        }

    def login(self, url, header = None):
        # anytime the user logs in to the system, a post request will be made to the url that is provided by the user using the username and password
        data = {
            'username': self.__username,
            'password': self.__password
        }
        header = self.header if not header else header
        try:
            response = requests.post(url=url, data=json.dumps(data), headers=header)
            if response.status_code == 200:
                self.access_token = response.json()['access']
                self.refresh_token = response.json()['refresh']
                print('[+] successfully logged in...')
                self.logged_in = True
            else:
                print(response.text)
        except Exception as err:
            pass
    
    def get_dashboard_summary(self, url_path=None):
        if not url_path:
            print('please provide a url path to fetch dashboard data from')
            return None
        if not self.logged_in:
            print('please login to access transaction summary')
            return None
        
        header = copy.deepcopy(self.header)
        header.update({"Authorization": f'Bearer {self.access_token}'})
        response = requests.get(url=url_path, headers=header)
        if response.status_code == 200:
            data = response.json()
            username = data['username']
            balance = data['balance']
            recent_transactions = data['recent_transactions']
            print("[*] Username", username)
            print("[*] Balance", balance)
            print('recent transaction:')
            if recent_transactions:
                for tnx in recent_transactions:
                    print(tnx)
            else:
                print('No recent transaction')
    

    def get_transactions(self, url_path=None):
        if not url_path:
            print('please provide a url path to fetch dashboard data from')
            return None
        if not self.logged_in:
            print('please login to access transaction summary')
            return None
        
        header = copy.deepcopy(self.header)
        header.update({"Authorization": f'Bearer {self.access_token}'})
        response = requests.get(url=url_path, headers=header)
        if response.status_code == 200:
            data = response.json()
            transactions = data['transactions']
            print('All transactions:')
            if transactions:
                for tnx in transactions:
                    print(tnx)
            else:
                print('No transaction found')
        else:
            print(response.text)
    
    def __str__(self) -> str:
        return self.__username
    
    def __repr__(self) -> str:
        return f"self.__class__.__name__({self.__username, self.__password})"


user = User(username='user2011', password='amotMan2000')
user.login(url='http://127.0.0.1:8000/api/v1/users/auth/login')
user.get_dashboard_summary('http://127.0.0.1:8000/api/v1/users/dashboard')
user.get_transactions('http://127.0.0.1:8000/api/v1/users/transactions')
