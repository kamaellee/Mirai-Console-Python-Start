# Mirai-Console-Python-Start
Mirai-Console 衍生应用，python脚本一键启动mirai



Mirai-Console-Python-Start（以下皆统称：本项目）遵从源项目采用`AGPLv3`协议开源。

## 本项目介绍：

本项目设计初衷是某强迫症（本人）觉得 **[*Mirai*OK](https://github.com/LXY1226/MiraiOK)** 多一个弹窗看不顺眼，想把`mirai`也放在python后端运行，故诞生了此项目。
### 本项目暂停更新，因发现前人已有写好的功能 **[ MiraiN](https://github.com/WDFunction/MiraiN)** ，所以弃坑了。

## 本项目测试环境：

### Windows：

> ###  Win10 - 专业版
>
> ### python 3.8.5
>
> ### Java 14.0.1



## 本项目依赖：

### [`Mirai`](https://github.com/mamoe/mirai) ：高效率 QQ 机器人框架

### [`Mirai-Console`](https://github.com/mamoe/mirai-console) ：高效率 QQ 机器人控制台



## 本项目相关项目：

### [`Mirai-Api-Http`](https://github.com/project-mirai/mirai-api-http) ：提供HTTP API供所有语言使用mirai

### [`Graia Application for mirai-api-http`](https://github.com/GraiaProject/Application)：基于 mirai-api-http 的即时聊天软件自动化框架（PYTHON）



## 本项目所需模块：

`os` 、`subprocess`、`hashlib` 、`yaml`

**<u>`致萌新`</u>**：使用`win` + `r`  输入 `cmd` 输入 `pip list` 查看已有包名，缺少的使用 `pip install 模块名` 安装



## 本项目使用方法：

需要有一定的pyton基础，包括但不限于部署环境、安装使用IDE、手敲代码等。

### 方法1（适用于win）：

`Download` 或 `Clone`本项目至本地，采用python IDE 运行其中的 `start_mirai.py`文件，即可实现

### 方法2（适用于win）：

截取其中的 `start_mirai.py`文件，在同级目录创建 `libs`文件，分别放入三个必须项目`mirai-console`、`mirai-console-terminal`、`mirai-core-qqandroid`，再采用python IDE 运行其中的 `start_mirai.py`文件

mirai 在版本发布时会同时发布打包依赖的 Shadow JAR，存放在 [`mirai-repo`](https://github.com/project-mirai/mirai-repo/tree/master/shadow)。

### 方法3（待测试，适用于linux）：

此方法测试完成后会更新。



## To Do List：

- [ ] 修改初次启动程序中断，需要再次重启的bug
- [x] ~~Linux版运行~~ 使用bash script或者miraiOK就好
- [ ] 可选择性更新Mirai
- [ ] 代码逻辑优化
- [ ] 一键启动mirai及graia bot
- [ ] ~~待补充…~~



## 特别鸣谢：

### [`Him188`](https://github.com/Him188) 及 [`Karlatemp`](https://github.com/Karlatemp) 贡献的 [`Mirai Console - Run`](https://github.com/mamoe/mirai-console/blob/master/docs/Run.md) ,是本项目的思路启发。



## 贡献：

本项目接受来自代码上的建议，包括但不限于修改/新增/补全`相关功能`，具体可在`issue`或我本人处反馈（找得到我的话）。

您的 `star` 是对我们最大的鼓励(点击项目右上角)



## 许可证：

我们使用 [`GNU AGPLv3`](https://choosealicense.com/licenses/agpl-3.0/) 作为本项目的开源许可证.
