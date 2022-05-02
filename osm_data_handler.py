import xml.etree.ElementTree as ET
import pprint
import collections
import pandas as pd

file_name = 'giza_osm_data.xml'
keys = []
values = []
#giza_osm_dict = collections.defaultdict(list)
#giza_osm_df = pd.read_xml(file_name)
#for event, elem in ET.iterparse(file_name):
#    keys.append(elem.tag)
#    values.append(elem.attrib)

#for key in keys:
#    giza_osm_dict[key].append(str(values[i]) for i in range(len(values)))
#giza_osm_dict = {keys[i]: values[i] for i in range(len(keys))}
#pprint.pprint(giza_osm_df.head(10))
#print('Lengh of the generated dict is: ', len(giza_osm_dict))
print('Lengh of keys is: ', len(keys),', ', 'Lengh of values is: ', len(values))