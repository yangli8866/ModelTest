import yaml


class Paser:
    def paser_test_file(self, api_list):
        '''
        paser 解析json文件为生产pytest文件

        '''
        # 根据api_list解析生成对应的test case
        pass

    def parser_yaml(self, yaml_url):
        with open(yaml_url, 'r') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        r = result['paths']
        keys = []
        for key, value in r.items():
            keys.append(key)
        return keys

    @classmethod
    def parse_url(cls, path, case):
        for key, value in case["params"].items():
            path = path.replace("{" + key + "}", value)
        # subscription_name = case["params"]['subscription_name']
        # resource_group_name = case["params"]['resource_group_name']
        # zone = case["params"]['zone']
        # telemetry_station_name = case["params"]['telemetry_station_name']
        # case_path = path.format(subscription_name=subscription_name, resource_group_name=resource_group_name, zone=zone,
        #                         telemetry_station_name=telemetry_station_name)
        print(path)
        return path


if __name__ == '__main__':
    pass
