# 我的博客
## 起風了
![Blog](http://aibeta.oss-cn-beijing.aliyuncs.com/markdown_img/blog%281%29.png)

### 启动项目
1.启动nginx服务  
    sudo sbin/nginx （或使用nginx -c /usr/local/nginx/conf/nginx.conf）  
    当有静态文件更新时  
    收集所有静态文件到static_root指定目录  
    python manage.py collectstatic  

2.启动uwsgi  
    uwsgi --ini uwsgi.ini

3.启动redis  
    $ sudo service redis start  
    $ ps aux|grep redis         查看redis是否在6379端口监听

4.启动celery的worker  
    celery -A Celery_Task worker -l info
    
5.运行supervisor  
/usr/bin supervisord -c /project/Blog/supervisord.conf  
（该运行命令根据你的安装路径为准，安装目录为你所使用的python安装目录下的bin目录内，如果有使用virtualenv请自行区分）  

6.启动sentry  
docker-compose up -d  

# 版本说明

## 1.0 版本  
百分之八十功能已经完成  
### 前端页面  
手机页面布局错位未修复  

### 评论模块  
目前只支持一级评论,用户头像等功能未加入  

### 用户模块  
登录注册完成  
微博登录接口已写好(等重写用户模型接入第三方登录)  
个人中心未开始  

### 后台管理  
xadmin  

## 1.2版本  
修复BUG以及增加新功能  

### logging  
LOGGING模块设置在setting中

### sentry线上日志警告系统  

