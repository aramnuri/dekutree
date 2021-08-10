# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import yaml
from config import configuration


def getProperty():
    properties = None
    activeType = None
    activeMain = 'deku'
    activeConfig = 'config'
    yamlLocation = configuration.CONFIG_YAML

    with open(yamlLocation) as setting:
        enumYaml = list(enumerate(yaml.load_all(setting, Loader=yaml.FullLoader)))
        active = enumYaml[0][1][activeMain][activeConfig]['active']
        print(active)

        for idx, data in enumYaml:
            if idx > 0 and data is not None and activeMain in data.keys() and active == data[activeMain][activeConfig]:
                activeType = idx

    if activeType is not None:
        properties = enumYaml[activeType][1]

    return properties
