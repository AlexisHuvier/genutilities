def __to_xml_list(root_name, element_name, liste):
    xml = ["<{}>".format(root_name)]
    for i in liste:
        if isinstance(i, dict):
            for k in __to_xml(element_name, element_name, i):
                xml.append("   "+k)
        elif isinstance(i, list):
            for k in __to_xml_list(element_name, element_name, i):
                xml.append("   "+k)
        else:
            xml.append("   <{0}>{1}</{0}>".format(element_name, i))
    xml.append("</{}>".format(root_name))
    return xml

def __to_xml(root_name, element_name, dic):
    xml = ["<{}>".format(root_name)]
    for k, v in dic.items():
        if isinstance(v, dict):
            for i in __to_xml(k, element_name, v):
                xml.append("   "+i)
        elif isinstance(v, (list, tuple)):
            for i in __to_xml_list(k, element_name, v):
                xml.append("   "+i)
        else:
            xml.append("   <{0}>{1}</{0}>".format(k, str(v)))
    xml.append("</{}>".format(root_name))
    return xml
        
def to_xml(dic: dict, root_name: str = "root", element_name: str = "element"):
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.extend(__to_xml(root_name, element_name, dic))
    return "\n".join(xml)

def flatten(d: dict, separator: str = ".", list_flatten=True):
    final_d = {}
    for k, v in d.items():
        if list_flatten:
            if isinstance(v, (dict, list, tuple)):
                if isinstance(v, (list, tuple)):
                    v = dict(enumerate(v))
                for k2, v2 in flatten(v, separator).items():
                    final_d[str(k)+separator+str(k2)] = v2
            else:
                final_d[k] = v
        else:
            if isinstance(v, dict):
                for k2, v2 in flatten(v, separator).items():
                    final_d[str(k)+separator+str(k2)] = v2
            else:
                final_d[k] = v
    return final_d

def unflatten(d: dict, separator: str = "."):
    final_d = {}
    for k, v in d.items():
        keys = k.split(separator)
        dic = final_d
        for i in keys:
            if i == keys[-1]:
                dic[i] = v
            else:
                try:
                    dic = dic[i]
                except KeyError:
                    dic[i] = {}
                    dic = dic[i]
    return final_d

def substract(d1: dict, d2: dict):
    final_d = {}
    for k in d1:
        if k not in d2:
            final_d[k] = d1[k]
    return final_d
