import xml.etree.ElementTree as ET
import pprint
import collections
import re

file_name = 'giza_osm_data.xml'
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
giza_osm_dict = collections.defaultdict(list)
street_types = collections.defaultdict(set)
expected = ['Street', 'Avenue', 'Boulevard', 'Drive']

def build_dict():
    for event, elem in ET.iterparse(file_name, events = ('start',)):
        giza_osm_dict[elem.tag].append(elem.attrib)

    return giza_osm_dict
    print(
        '\n',
        'Number of nodes found: ', len(giza_osm_dict['node']), '\n',
        'Number of members found: ', len(giza_osm_dict['member']), '\n',
        'Number of relations found: ', len(giza_osm_dict['relation']), '\n',
        'Number of ways found: ', len(giza_osm_dict['way']),
        '\n')

def audit_street_type(street_types, street_name):
    match = street_type_re.search(street_name)
    if match:
        street_type = match.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == 'addr:street')

def audit_street_name():
    for event, elem in ET.iterparse(file_name, events = ('start',)):
        if elem.tag == 'way':
            for tag in elem.iter('tag'):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    pprint.pprint(dict(street_types))

if __name__ == '__main__':
    audit_street_name()