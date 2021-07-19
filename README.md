[![pyvrml-logo](./resource/logo.png)](./README.md)

PyVrml是基于python3的开发工具库

提供对各项通用工具的支持，例如Excel，文件操作，网络调用等

在数据查询方面，您可以通过API或者爬虫的方式，接入您所使用的各种平台

在数据输出方面，支持Excel、Image及各种自定义方式

基于PyVrml定制您的常用工具集，从而便捷的进行数据查询聚合和监控

用于实现各种工作中需要用到的自动化脚本，为自动化监控、大批量数据查询、问题排查等应用场景提供强有力的工具

## Modules

#### ai

封装了机器学习算法，方便快速上手使用。当然，仅供娱乐

#### excel

快速方便的生成excel文档，方便的进行数据统计和文档整理

#### file

简易的csv文件读取api，便于使用csv进行各项数据脚本的书写

#### gitlab

通过gitlab的api，获取gitlab上的各项数据

#### http

带有重试功能的http访问api，针对json的包装

#### login

用于通过登录进行验权，从而爬取受账号权限保护的页面数据

#### retry

调用重试功能，避免脚本进行远程调用时失败退出

#### time

常用时间工具，包括(实践对象)/(字符串)/(时间戳)之间的转换

## 使用示例

`pyvrml`目录下为工具包源码

`demo`目录下为一些自动化脚本demo

您可以参考和`pyvrml.py`文件中的api示例，也可以直接查看`demo`目录下的自动化脚本实例。

## 使用方式

请直接下载pyvrml的源码包，将`pyvrml`目录文件放在您自己的开发项目中使用。

### exe文件执行

```shell
pyinstaller -F xxx.py
```

直接运行dist/xxx.exe即可

##### 注意事项：要在虚拟环境里安装pyinstaller

> 如果你没有在虚拟环境中安装pyinstaller，你同样可以使用pyinstaller命令， 但是调用的是你系统原本的那个python编译器，内含很多关联库， 导致即使在虚拟环境中，你打包的exe文件仍然非常大。

##### 报错信息：build/warn日志

> 可以使用命令行执行exe，不然报错信息会一闪而过