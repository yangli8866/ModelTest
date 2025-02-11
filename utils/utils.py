import os

class Util:
    def get_api_list(self,api_file_path):
        # 通过api_file_path遍历，找到所有的api_list

        api_list = []
        return api_list

    @classmethod
    def auto_login(cls):
        higgstoke_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/utils"
        # stmt = higgstoke_path + "/higgstoken0.1.0.darwin-amd64 login -t '' -u tsroottest -p '@Aa1234567' --apiDomain sensecoreapi.tech --signinDomain signin.sensecore.tech"
        stmt = higgstoke_path + "/higgstoken0.1.0.darwin-amd64 login -t 'code1030' -u liyang -p '@Aa123456' --apiDomain sensecoreapi.tech --signinDomain signin.sensecore.tech"
        res = os.popen(stmt).readlines()
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config/auth.json",'w') as f:
            f.writelines(res)
        stmt2 = higgstoke_path + "/higgstoken0.1.0.darwin-amd64 login -t 'code1030' -u yglroot -p 'Sensecore@2022' --apiDomain sensecoreapi.tech --signinDomain signin.sensecore.tech"
        res2 = os.popen(stmt2).readlines()
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config/acp_auth.json", 'w') as f:
            f.writelines(res2)


    @classmethod
    def get_token(cls, acp=False):
        if acp:
            auto_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config/acp_auth.json"
        else:
            auto_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config/auth.json"
        print(auto_path)
        with open(auto_path,'r') as f:
            r = f.readlines()
        token = r[1].split('"')[-2]
        print("token:",token)
        return token


if __name__=='__main__':
    Util.auto_login()
    # Util.get_token()
