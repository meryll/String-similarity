def setup_path():
    """ Quick hack to starting application form linux terminal. """
    import os
    import sys
    current_dir = os.path.dirname(os.path.realpath(__file__))
    dir_above = os.path.abspath(os.path.join(current_dir, '..'))
    root_dir = os.path.abspath(os.path.join(dir_above, '..'))
    if dir_above not in sys.path:
        sys.path.append(dir_above)
    if root_dir not in sys.path:
        sys.path.append(root_dir)


setup_path()
import sys, getopt
from textkernel.core.C import C
from textkernel.core.T import T
from textkernel.core import algorithm
from textkernel.data_io import data_writer


def get_filepaths():
    if len(sys.argv[1:]) < 2:

        filepaths = ['../data/test2.normalized4',
                     '../data/test1.normalized4']

        filepaths = ['../data/manpower_experience_enriched.xml',
                     '../data/experience.normalized4']

        # filepaths = ['../data/manpower_experience_enriched.xml',
        #              '../data/experience.normalized4',
        #              '../data/part.all.jobtitle_enriched.xml']

        to_enrich_file = '../data/valid1.normalized4'
        to_enrich_file = '../data/all.jobtitle_enriched.xml'

    else:
        filepaths = sys.argv[1:-1]
        to_enrich_file = sys.argv[-1]

    return filepaths, to_enrich_file


if __name__ == '__main__':
    filepaths, to_enrich_file = get_filepaths()

    confidence_threshold = 0.3
    manual_confidence_threshold = 0.5

    print('Starting to get T.')
    T = T(file_paths=filepaths)
    print('Starting to get C')
    C = C(file_path=to_enrich_file)
    print('Starting to enrich')
    C = algorithm.enrich(T=T, C_original=C, confidance_threshold=confidence_threshold)

    data_writer.save(C=C, manual_confidence_threshold=manual_confidence_threshold, original_filepath=to_enrich_file)
