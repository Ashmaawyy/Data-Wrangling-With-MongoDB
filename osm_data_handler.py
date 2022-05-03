import xml.etree.ElementTree as ET
import pprint

file_name = 'giza_osm_data.xml'
keys = set()
values = []
giza_osm_dict = {}

for event, elem in ET.iterparse(file_name, events = ('start',)):
    giza_osm_dict[elem.tag] = [elem.attrib].append(elem.attrib)
    print('adding attribute: ', elem.attrib, ' to key: ', elem.tag)

pprint.pprint(list(giza_osm_dict.items())[:11])
print('Lengh of the generated dict is: ', len(giza_osm_dict))