import logging
from sqlalchemy import pool, create_engine

## consider to make init file such as "main.py" or "__init__.py"
import os
import sys
sys.path.append(os.getcwd())
from dekutree.config.propertyResolver import getProperty
from dekutree.dbConnector.properties.sqlalchemy import arguments

### variables
RDBMS = ['oracle', 'mysql', 'maria']
NoSQL = ['redis', 'mongodb']
conn = None
properties = getProperty()

### set logging level (need to consider logging backend and same filename)
currentFile = os.path.splitext(os.path.basename(__file__))[0]
if currentFile in properties['logging']['level']:
    print(properties['logging']['level'][currentFile])
else:
    print(properties['logging']['level']['root'])
logger = logging.getLogger()
logger.setLevel(logging.INFO)

### class (test)
class Connector():

    engine = None

    def __init__(self, connect_info = None):
        print("### INIT")
        if "pool" in properties.keys():
            basicPool = properties["pool"]

        if "databases" in properties.keys():
            databases = properties["databases"]

        for db in databases.keys():
            if "failover" in databases[db].keys():
                print("failover")
                # failover db array
            else:
                connection, connArgs, dbInfo = setEngineProperty(basicPool, databases[db])
                engine = create_engine(connection, **connArgs)
                print(engine)
                # normal db array
                self.conn = engine
                ## consider dbms branch (rdbms, nosql, etc.)
                # if "oracle" in RDBMS:

    # need to modify
    def __enter__(self):
        print("### ENTER")
        pools = {}
        pools[0] = self.conn.connect()
        pools[1] = self.conn.connect()
        self.pools = pools
        print(self.conn.pool.status())
        return self

    # need to modify
    def __exit__(self, exc_type, exc_val, exc_tb):
        for pools in self.pools:
            self.pools[pools].close()
        print("### EXIT")

### functions
def setEngineProperty(poolArg, databaseArg):
    try:
        checkPoolArg = False
        checkDbArgOpt = False
        checkDbArgPool = False
        db_service = ''
        dbInfo = {}

        if not all (keys in databaseArg for keys in ('engine', 'user', 'password', 'host', 'port', 'name')):
            raise Exception('Essential DB info missing')
        
        if poolArg != None:
            checkPoolArg = True
            arguments['poolclass'] = pool.QueuePool

        if any (keys in databaseArg for keys in ('paramstyle', 'encoding', 'echo')):
            checkDbArgOpt = True

        if any (keys in databaseArg for keys in ('pool', 'poolclass', 'echo-pool', 'time-out', 
            'pool-size', 'pool-max-overflow', 'pool-recycle', 'pool-reset-on-return', 'pool-use-lifo')):
            checkDbArgPool = True
            arguments['poolclass'] = pool.QueuePool

        if checkPoolArg:
            for poolProp in poolArg:
                if 'pool' == poolProp: arguments['pool'] = poolArg[poolProp]
                if 'poolclass' == poolProp: arguments['poolclass'] = poolArg[poolProp]
                if 'echo-pool' == poolProp: arguments['echo_pool'] = poolArg[poolProp]
                if 'time-out' == poolProp: arguments['pool_timeout'] = poolArg[poolProp]
                if 'pool-size' == poolProp: arguments['pool_size'] = poolArg[poolProp]
                if 'pool-max-overflow' == poolProp: arguments['max_overflow'] = poolArg[poolProp]
                if 'pool-recycle' == poolProp: arguments['pool_recycle'] = poolArg[poolProp]
                if 'pool-reset-on-return' == poolProp: arguments['pool_reset_on_return'] = poolArg[poolProp]
                if 'pool-use-lifo' == poolProp: arguments['pool_use_lifo'] = poolArg[poolProp]

        for dbProp in databaseArg:
            # essential setting
            if 'engine' == dbProp: 
                db_engine = databaseArg[dbProp]
                dbInfo['engine'] = db_engine
                if db_engine == 'maria':
                    db_engine = 'mysql+pymysql'
            if 'user' == dbProp: db_user = databaseArg[dbProp]
            if 'password' == dbProp: db_pass = databaseArg[dbProp]
            if 'host' == dbProp: db_host = databaseArg[dbProp]
            if 'port' == dbProp: db_port = databaseArg[dbProp]
            if 'service-name' == dbProp: 
                db_service = '/' + databaseArg[dbProp]
            if 'name' == dbProp: dbInfo['name'] = databaseArg[dbProp]
            # option setting
            if checkDbArgOpt:
                if 'paramstyle' == dbProp: arguments['paramstyle'] = databaseArg[dbProp]
                if 'encoding' == dbProp: arguments['encoding'] = databaseArg[dbProp]
                if 'echo' == dbProp: arguments['echo'] = databaseArg[dbProp]
            # pool setting
            if checkDbArgPool:
                if 'pool' == dbProp: arguments['pool'] = databaseArg[dbProp]
                if 'poolclass' == dbProp: arguments['poolclass'] = databaseArg[dbProp]
                if 'echo-pool' == dbProp: arguments['echo_pool'] = databaseArg[dbProp]
                if 'time-out' == dbProp: arguments['pool_timeout'] = databaseArg[dbProp]
                if 'pool-size' == dbProp: arguments['pool_size'] = databaseArg[dbProp]
                if 'pool-max-overflow' == dbProp: arguments['max_overflow'] = databaseArg[dbProp]
                if 'pool-recycle' == dbProp: arguments['pool_recycle'] = databaseArg[dbProp]
                if 'pool-reset-on-return' == dbProp: arguments['pool_reset_on_return'] = databaseArg[dbProp]
                if 'pool-use-lifo' == dbProp: arguments['pool_use_lifo'] = databaseArg[dbProp]
        
        connection = "{0}://{1}:{2}@{3}:{4}{5}".format(db_engine, db_user, db_pass, db_host, db_port, db_service)

        return connection, arguments, dbInfo
    except Exception as e:
        print('Error occured while setting engine property.' + e)


## main logic (test)
# with Connector() as conn:
#     print("###")
