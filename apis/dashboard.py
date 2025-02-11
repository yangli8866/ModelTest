import time
import requests

from utils.case_utils import CaseHelper
from utils.parser import Paser
from utils.utils import Util

class Dashboards:

    @staticmethod
    def get_dashboards():
        json_path = "/data/get_dashboard.json"
        path, ids, case_list = CaseHelper.load_case_from_json(json_path)
        case_path = Paser.parse_url(path, case_list[0])
        header = {
            'Authorization': "bearer " + Util.get_token(),
            'Accept-Encoding': 'gzip, deflate, br'
        }
        start = int(time.time())
        payload = {
            "start": start,
            "end": start + 86400,
            "state": 0
        }
        print(case_path)
        res = requests.get(case_path, params=payload, headers=header)
        if case_list[0]["check"].get("code") == res.status_code:
            return res
        else:
            return 0

    @staticmethod
    def post_dashboards_filters():
        # 未调通
        json_path = "/data/post_dashboard_filters.json"
        path, ids, case_list = CaseHelper.load_case_from_json(json_path)
        case_path = Paser.parse_url(path, case_list[0])
        header = {
            'Authorization': "bearer " + Util.get_token(),
            'Accept-Encoding': 'gzip, deflate, br'
        }
        payload = {"start": 1688028323, "end": 1688633123,
                   "resource": [{"resource_id": "e5b99a06-fdcb-11ed-9fa4-ceece2e5afa3"}]}
        print(case_path)
        res = requests.post(case_path, json=payload, headers=header)
        if case_list[0]["check"].get("code") == res.status_code:
            return res
        else:
            return 0

    @staticmethod
    def get_dashboards_panels():
        json_path = "/data/get_dashboard_panels.json"
        path, ids, case_list = CaseHelper.load_case_from_json(json_path)
        case_path = Paser.parse_url(path, case_list[0])
        header = {
            'Authorization': "bearer " + Util.get_token(),
            'Accept-Encoding': 'gzip, deflate, br'
        }
        start = int(time.time())
        payload = {
            "start": start,
            "end": start + 86400,
            "state": 0
        }
        print(case_path)
        res = requests.get(case_path, params=payload, headers=header)
        if case_list[0]["check"].get("code") == res.status_code:
            return res
        else:
            return 0

    @staticmethod
    def post_dashboards_metrics():
        # 未调通
        json_path = "/data/post_dashboard_metrics.json"
        path, ids, case_list = CaseHelper.load_case_from_json(json_path)
        case_path = Paser.parse_url(path, case_list[0])
        header = {
            'Authorization': "bearer " + Util.get_token(),
            'Accept-Encoding': 'gzip, deflate, br'
        }
        start = int(time.time())
        payload = {
            "start": start,
            "end": start + 86400,
            "state": 0
        }
        print(case_path)
        res = requests.post(case_path, params=payload, headers=header)
        if case_list[0]["check"].get("code") == res.status_code:
            return res
        else:
            return 0



if __name__=='__main__':
    res = Dashboards.get_dashboards_panels()
    print(res.json())

