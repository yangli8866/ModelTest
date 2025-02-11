import time
import requests

from utils.case_utils import CaseHelper
from utils.parser import Paser
from utils.utils import Util


class ExportLog:

    @staticmethod
    def post_export_job():
        # 【导出日志】——>【导出】
        json_path = "/data/post_export_job_list.json"
        path, ids, case_list = CaseHelper.load_case_from_json(json_path)
        case_path = Paser.parse_url(path, case_list[0])
        header = {
            'Authorization': "bearer " + Util.get_token(),
            'Accept-Encoding': 'gzip, deflate, br'
        }
        payload = {"page_size": 10, "offset": "0"}
        print(case_path)
        res = requests.post(case_path, json=payload, headers=header)
        if case_list[0]["check"].get("code") == res.status_code:
            return res
        else:
            return 0

    @staticmethod
    def get_alerts_hitsory():
        json_path = "/data/get_alerts_histogram.json"
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
    def get_alerts_line():
        json_path = "/data/get_alerts_line.json"
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
    def get_alerts_pie():
        json_path = "/data/get_alerts_pie.json"
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


if __name__ == '__main__':
    res = ExportLog.post_export_job()
    print(res)