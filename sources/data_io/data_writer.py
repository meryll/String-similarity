import xml.etree.ElementTree as ET
from xml.dom import minidom
import time
from os.path import basename
import os


def save(C, manual_confidence_threshold, original_filepath, file_path=None):
    if file_path is None:
        file_path = _get_filename(original_filepath=original_filepath)

    root = ET.Element("CodeTable")
    table_info = ET.SubElement(root, "CodeTableInfo")
    tree = ET.SubElement(root, "CodeRecordList")

    for code_id in C.code_ids:
        doc = ET.SubElement(tree, "CodeRecord")

        print("-------")
        print(C.new_code_to_old[code_id], C.code_ids[code_id], code_id)

        ET.SubElement(doc, "CodeID").text = C.new_code_to_old[code_id]
        ET.SubElement(doc, "CodeDescription").text = C.code_ids[code_id]
        ET.SubElement(doc, "CodeProperty", name='codeid').text = code_id

        instances_list = ET.SubElement(doc, "InstanceList")

        selected_attractors = C.new_attractors[code_id]
        for attractor in selected_attractors:
            instance = ET.SubElement(instances_list, "Instance")
            confidence = attractor.confidence

            ET.SubElement(instance, "InstanceDescription").text = attractor.synonym
            ET.SubElement(instance, "InstanceProperty", name='confidence').text = str(confidence)
            ET.SubElement(instance, "InstanceProperty", name='transfer').text = _get_transfer_type(
                confidence=confidence, threshold=manual_confidence_threshold)

            print(attractor.synonym, attractor.distance, attractor.shared_codes, confidence,
                  _get_transfer_type(confidence, threshold=manual_confidence_threshold))

    rough_string = ET.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="\t")

    with open(file_path, 'w') as file:
        file.write(pretty_xml)


def _get_transfer_type(confidence, threshold):
    if confidence >= threshold:
        return 'auto'
    return 'manual'


def _get_filename(original_filepath):
    file_basename = basename(original_filepath)
    enriched_dir = '../generated_files'
    current_timestamp = time.strftime("%Y%m%d-%H%M%S")
    enriched_filename = "{}_enriched_{}.xml".format(file_basename, current_timestamp)
    enriched_filepath = os.path.join(enriched_dir, enriched_filename)
    return enriched_filepath
