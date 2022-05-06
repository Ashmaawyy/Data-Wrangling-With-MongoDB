import xml.etree.ElementTree as ET
import pprint
import collections

file_name = 'giza_osm_data.xml'
giza_osm_dict = collections.defaultdict(list)

for index, (event, elem) in enumerate(ET.iterparse(file_name)):
    if elem.tag != 'tag' or 'nd':
        giza_osm_dict[elem.tag].append(elem.attrib)
    else:
        giza_osm_dict['node'][-1].update(elem.attrib)
        giza_osm_dict['way'][-1].update(elem.attrib)
        giza_osm_dict['relation'][-1].update(elem.attrib)

pprint.pprint(giza_osm_dict['relation'])
print(
    '\n',
    'Number of nodes found: ', len(giza_osm_dict['node']), '\n',
    'Number of members found: ', len(giza_osm_dict['member']), '\n',
    'Number of relations found: ', len(giza_osm_dict['relation']), '\n',
    'Number of ways found: ', len(giza_osm_dict['way']),
    '\n')