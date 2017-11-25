import logging
import django.utils.log
import logging.handlers


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    # 配置打印日志格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },

    """
    格式             描述
    %(name)s	    记录器的名称
    %(levelno)s	    数字形式的日志记录级别
    %(levelname)s	日志记录级别的文本名称
    %(filename)s	执行日志记录调用的源文件的文件名称
    %(pathname)s	执行日志记录调用的源文件的路径名称
    %(funcName)s	执行日志记录调用的函数名称
    %(module)s	    执行日志记录调用的模块名称
    %(lineno)s	    执行日志记录调用的行号
    %(created)s	    执行日志记录的时间
    %(asctime)s	    日期和时间
    %(msecs)s	    毫秒部分
    %(thread)d	    线程ID
    %(threadName)s	线程名称
    %(process)d	    进程ID
    %(message)s	    记录的消息
    """

    'filters': {
    },

    # 定义具体处理日志的方式
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/project/Blog/log/all.log',  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/project/Blog/log/error.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/project/Blog/log/script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/project/Blog/log/script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },

    # 1.loggers类型为"django"这将处理所有类型日志。
    # 2.sourceDns.webdns.views 应用的py文件
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'sourceDns.webdns.views': {
            'handlers': ['default', 'error'],
            'level': 'INFO',
            'propagate': True
        },
        'sourceDns.webdns.util': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}
