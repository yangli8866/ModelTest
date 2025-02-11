# 接口地址；
https://gitlab.bj.***.com/elementary/workspace/v1/workspace.openapi.yaml
框架设计模式： key-word drive model
2种自动化实现：
- 接口自动化
- 解析接口配置文件自动生成testcase文件

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
- 非算力池case：用户A
- 算力池case：用户B

# api列表如下：（共40个）
***

