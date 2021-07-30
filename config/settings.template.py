DATABASES = { 
    'default': {},
    'template1': {  
        'NAME': 'DB_NAME', 
        'ENGINE': 'db.backends.oracle',
        'USER' : 'USER_NAME', 
        'PASSWORD' : 'PASSWORD', 
        'HOST': 'DB_HOST', 
        'PORT': 'PORT',
        'POOL_SIZE' : 'POOL_SIZE',
        'POOL_MAX_OVERFLOW' : 'POOL_MAX_OVERFLOW',
        'POOL_RECYCLE' : 'POOL_RECYCLE'
    },
    'template2': {
        'failover' : [{  
            'NAME': 'DB_NAME1', 
            'ENGINE': 'db.backends.mysql',
            'USER' : 'USER_NAME', 
            'PASSWORD' : 'PASSWORD', 
            'HOST': 'DB_HOST', 
            'PORT': 'PORT1' ,
        }, {  
            'NAME': 'DB_NAME2', 
            'ENGINE': 'db.backends.mysql',
            'USER' : 'USER_NAME', 
            'PASSWORD' : 'PASSWORD', 
            'HOST': 'DB_HOST', 
            'PORT': 'PORT2' ,
        }]
    },
}

CACHES = {  
    "default": {
        "BACKEND": "redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1", # 1번 DB
        "OPTIONS": {
            "CLIENT_CLASS": "redis.client.DefaultClient",
        }
    }
}

REDIS_IGNORE_EXCEPTIONS = True
REDIS_LOG_IGNORED_EXCEPTIONS = True
SESSION_ENGINE = "contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

SECRET_KEY = 'SECRET_KEY'

LOGGING_LEVEL = "INFO"
