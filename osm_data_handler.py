import xml.etree.ElementTree as ET
import pprint
import collections
import re

file_name = 'giza_osm_data.xml'
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
giza_osm_dict = collections.defaultdict(list)
streets, nodes, relations = collections.defaultdict(set)

def build_main_dict():
    for event, elem in ET.iterparse(file_name, events = ('start',)):
        streets = audit_street_name(elem)
    for street in streets.values():
        giza_osm_dict['ways'].append(street)

    print(
        '\n',
        'Number of nodes found: ', len(giza_osm_dict['nodes']), '\n',
        'Number of members found: ', len(giza_osm_dict['members']), '\n',
        'Number of relations found: ', len(giza_osm_dict['relations']), '\n',
        'Number of ways found: ', len(giza_osm_dict['ways']),
        '\n')
    return giza_osm_dict

def audit_street_type(street_types, street_name):
    match = street_type_re.search(street_name)
    if match:
        street_type = match.group()
        street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == 'addr:street')

def audit_street_name(elem):
        if elem.tag == 'way':
            for tag in elem.iter('tag'):
                if is_street_name(tag):
                    audit_street_type(streets, tag.attrib['v'])

        return streets

if __name__ == '__main__':
    pprint.pprint(build_main_dict())