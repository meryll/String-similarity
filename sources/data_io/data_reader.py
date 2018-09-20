import os.path
from enum import Enum
from sources.data_io import _xml_reader, _normalized_file_reader


def get(file_path):
    extension = _get_extension(file_path=file_path)

    if extension == ExtensionType.XML.value:
        return _xml_reader.read(file_path)
    elif extension == ExtensionType.Normalized4.value:
        return _normalized_file_reader.read(file_path)
    else:
        raise NotImplementedError('Get file for {} is not implemented'.format(extension))


def _get_extension(file_path):
    return os.path.splitext(file_path)[1]


class ExtensionType(Enum):
    XML = '.xml'
    Normalized4 = '.normalized4'

