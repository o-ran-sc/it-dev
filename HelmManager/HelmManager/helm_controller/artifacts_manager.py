################################################################################
#   Copyright (c) 2019 AT&T Intellectual Property.                             #
#   Copyright (c) 2019 Nokia.                                                  #
#                                                                              #
#   Licensed under the Apache License, Version 2.0 (the "License");            #
#   you may not use this file except in compliance with the License.           #
#   You may obtain a copy of the License at                                    #
#                                                                              #
#       http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                              #
#   Unless required by applicable law or agreed to in writing, software        #
#   distributed under the License is distributed on an "AS IS" BASIS,          #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
#   See the License for the specific language governing permissions and        #
#   limitations under the License.                                             #
################################################################################

import os
import logging
import re
import glob
import threading
import shutil
from HelmManager import settings


log = logging.getLogger(__name__)

def get_dir_size(start_path = '.'):
    total_size = 0

    if os.path.isfile(start_path):
        total_size += os.path.getsize(start_path)

    if os.path.isdir(start_path):
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

    return total_size



def format_artifact_dir_size():
    """ Converts integers to common size units used in computing """
    artifact_dir_size_string = settings.CHART_WORKSPACE_SIZE
    size_unit = re.sub('[0-9\s\.]', '', artifact_dir_size_string)
    size_limit = re.sub('[A-Za-z\s\.]','',artifact_dir_size_string)

    bit_shift = {"B": 0,
            "kb": 7,
            "KB": 10,
            "mb": 17,
            "MB": 20,
            "gb": 27,
            "GB": 30,
            "TB": 40,}
    return float(size_limit) * float(1 << bit_shift[size_unit])


def trim_artifact_dir():
    artifact_dir_size = get_dir_size(start_path=settings.CHART_WORKSPACE_PATH)
    dir_limit = format_artifact_dir_size()

    if artifact_dir_size > dir_limit:
        dirs = sorted(glob.glob(settings.CHART_WORKSPACE_PATH+'/*'), key=os.path.getctime)
        trim_dir = list()
        remain_size = artifact_dir_size
        for dir in dirs:
            remain_size =  remain_size - get_dir_size(start_path = dir)
            trim_dir.append(dir)
            if remain_size < dir_limit:
                break
        log.info("Trimming artifact directories: " + str(trim_dir))
        for dir in trim_dir:
            if os.path.isfile(dir):
                os.remove(dir)
            else:
                shutil.rmtree(dir)

    threading.Timer(60.0, trim_artifact_dir).start()

def start_trim_thread():
    log.info("Artifact directory trimming thread started.")
    trim_artifact_dir()


