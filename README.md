# Constrution_Daily
网页版，施工日志，采用Django框架编写，学习Python的练习项目。

如何下载本地运行？

克隆项目到本地
git clone https://github.com/zmscgsf/Constrution_Daily.git

安装虚拟环境Pipenv
pip install pipenv

安装项目依赖库，启动虚拟环境
cd Constrution_Daily
pipenv install --dev
pipenv shell

迁移项目数据库
python manage.py migrate

运行Django服务器
python manage.py runserver

浏览进入日志主页
http://127.0.0.1:8000

创建用户进行填报

优化继续中。。。