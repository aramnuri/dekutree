import yaml

def getProperty():
    properties = None
    activeType = None
    activeMain = 'deku'
    activeConfig ='config'
    yamlLocation = '.\\dekutree\\config\\settings.template.yaml'
    # yamlLocation = '.\\dekutree\\config\\settings.yaml'

    with open(yamlLocation) as setting:
        enumYaml = list(enumerate(yaml.load_all(setting, Loader = yaml.FullLoader)))
        active = enumYaml[0][1][activeMain][activeConfig]['active']
        
        for idx, data in enumYaml:
            if idx > 0 and data != None and activeMain in data.keys() and active == data[activeMain][activeConfig]:
                activeType = idx

    if activeType != None:
        properties = enumYaml[activeType][1]

    return properties
