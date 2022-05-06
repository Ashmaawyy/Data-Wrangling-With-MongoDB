import xml.etree.ElementTree as ET
import pprint
import collections

file_name = 'giza_osm_data.xml'
giza_osm_dict = collections.defaultdict(list)

for idx, (event, elem) in enumerate(ET.iterparse(file_name)):
    giza_osm_dict[elem.tag].append(elem.attrib)
    
    if elem.tag == 'tag':
        giza_osm_dict['node'][idx].update(elem.attrib)

    
pprint.pprint(giza_osm_dict['node'][-1])
print(
    '\n',
    'Number of nodes found: ', len(giza_osm_dict['node']), '\n',
    'Number of members found: ', len(giza_osm_dict['member']), '\n',
    'Number of relations found: ', len(giza_osm_dict['relation']), '\n',
    'Number of ways found: ', len(giza_osm_dict['way']),
    '\n')