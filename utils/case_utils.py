import json
import os


class CaseHelper:
    obs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def load_case_from_json(cls, path):
        with open(cls.obs_path + path, 'r') as f:
            values = json.load(f)
        cases = values["cases"]
        ids = [_c for _c in cases.keys()]
        case_list = [cases.get(i) for i in ids]
        path = cls.load_host_from_config() + values["path"]
        return path, ids, case_list

    @classmethod
    def load_host_from_config(cls):
        # 从config/config.ini文件中读取host配置
        file_path = "/config/config.ini"
        with open(cls.obs_path + file_path, 'r') as f:
            values = f.readlines()
        for h in values:
            if 'tech_host' in h:
                return h.split('=')[-1].split('\n')[0]


if __name__ == '__main__':
    # file_path = '/Users/liyang8/PycharmProjects/ModelTest/data/get_alerts.json'
    # path,cases = CaseHelper.load_case_from_json(file_path)
    # print(path)
    # print(cases)
    config_file_path = '/config/config.ini'
    path = CaseHelper.obs_path + config_file_path
    print(path)
    host = CaseHelper.load_host_from_config(path)
    print(host)
