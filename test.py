
# import sys
# sys.path.append("/Users/taylor/Create/projects/CWR-DataApi/cwr")

import codecs
import os

from cwr.parser.decoder.file import default_file_decoder
from cwr.parser.encoder.cwrjson import JSONEncoder

if __name__ == '__main__':

    # path = '/Users/taylor/Downloads/CW180001000_000.V21'
    # path = '/Users/taylor/Create/projects/CWR-DataApi/tests/examples/ackexample.V21'
    path = '/Users/taylor/Downloads/CW200090UN_PEX.V21'

    data = {}
    data['filename'] = os.path.basename(path)
    data['contents'] = codecs.open(path, 'r', 'latin-1').read()

    data = default_file_decoder().decode(data)

    print(JSONEncoder().encode(data))
    
