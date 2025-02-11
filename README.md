# 接口地址；
https://gitlab.bj.sensetime.com/elementary/telemetry/telemetry-apis/-/blob/master/pb/telemetry/workspace/v1/workspace.openapi.yaml
框架设计模式： key-word drive model

# 模块
- main.py：登录,记录token
- testcases：接口自动化
- data：接口参数以及assert
- config：配置
- util：工具类
- allure-resoult：allure报告

# todo：
优化项：
- api层：封装每个request api接口
- testcases_new:组装多个api为一个业务功能case


# 说明
使用的测试租户为：
- 非算力池case：code1030 liyang
- 算力池case：code1030 yglroot

# api列表如下：（共40个）

- ~~/v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/alerts
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/alerts/histogram
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/alerts/line
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/alerts/pie~~
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/dashboards~~
未调通
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/dashboards/{dashboard_name}/filters
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/dashboards/{dashboard_name}/panels 
未调通
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/dashboards/{dashboard_name}/panels/{panel_name}/metrics
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/exportLog/products/{product_name}/exportJob
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/exportLog/products/{product_name}/exportJob/list
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/exportLog/products/{product_name}/exportJob/{export_job_id}/status
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/exportLog/products/{product_name}/logOssConfig
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/exportLog/products/{product_name}/logOssConfig/{log_oss_config_id}
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/levelAlerts
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/logLivestream/filters
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/logLivestream/token
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/logStream/products
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/logStream/products/{product_name}/customFilterValues
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/logStream/products/{product_name}/customFilters
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/logStream/products/{product_name}/logSurround
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/logStream/products/{product_name}/logs
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/operationLog/products
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/operationLog/products/{product_name}/operationFilterValues
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/operationLog/products/{product_name}/operationFilters
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/operationLog/products/{product_name}/operationLogs
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/products/{product}/ruleTemplates
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/resources
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/ruleTemplates
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/ruleTemplates/{rule_template_id}
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/rules
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/rules/products
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/rules/templates
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/rules/{rule_id}
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/rules:bulk
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/user:search
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/userGroup/{user_group_id}/rules
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/usergroups
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/usergroups/create
- /v1/subscriptions/{subscription_name}/resourceGroups/{resource_group_name}/zones/{zone}/telemetryStations/{telemetry_station_name}/usergroups/{group_id}