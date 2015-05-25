import ConfigParser
import string
_ConfigDefault = {
    "rdb.dbms": "mysql",
    "rdb.name": "",
    "rdb.user": "root",
    "rdb.password": "",
    "rdb.host": "127.0.0.1"
    }
def LoadConfig(file = 'config.ini', config={}):
    """
    returns a dictionary with keys of the form
    <section>.<option> and the corresponding values
    """
    config = config.copy( )
    cp = ConfigParser.ConfigParser( )
    cp.read(file)
    for sec in cp.sections( ):
        name = string.lower(sec)
        for opt in cp.options(sec):
            config[name + "." + string.lower(opt)] = string.strip(cp.get(sec, opt))
    return config
if __name__=="__main__":
    config = LoadConfig("config.ini", _ConfigDefault)
    print(config['settings.hostip'])
