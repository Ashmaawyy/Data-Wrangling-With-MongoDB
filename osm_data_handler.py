import xml.etree.ElementTree as ET
import pprint
import collections

file_name = 'giza_osm_data.xml'
keys = set()
values = []
giza_osm_dict = collections.defaultdict(list)

for event, elem in ET.iterparse(file_name, events = ('start',)):
    giza_osm_dict[elem.tag].append(elem.attrib)
    print('adding attribute: ', elem.attrib, ' to key: ', elem.tag)

print('Number of nodes found: ', len(giza_osm_dict['node']), '\n',
'Number of members found: ', len(giza_osm_dict['member']))