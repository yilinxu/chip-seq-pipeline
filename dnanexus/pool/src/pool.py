#!/usr/bin/env python
# pool 0.0.1
# Generated by dx-app-wizard.
#
# Basic execution pattern: Your app will run on a single machine from
# beginning to end.
#
# See https://wiki.dnanexus.com/Developer-Portal for documentation and
# tutorials on how to modify this file.
#
# DNAnexus Python Bindings (dxpy) documentation:
#   http://autodoc.dnanexus.com/bindings/python/current/

from os.path import splitext
import dxpy
import common
import logging

logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False
logger.setLevel(logging.INFO)


@dxpy.entry_point('main')
def main(inputs):

    input_filenames = []
    for input_file in inputs:
        dxf = dxpy.DXFile(input_file)
        input_filenames.append(dxf.name)
        dxpy.download_dxfile(dxf.get_id(), dxf.name)

    # uses last extension - presumably they are all the same
    extension = splitext(splitext(input_filenames[-1])[0])[1]
    pooled_filename = \
        '-'.join([splitext(splitext(fn)[0])[0] for fn in input_filenames]) + "_pooled%s.gz" % (extension)
    out, err = common.run_pipe([
        'gzip -dc %s' % (' '.join(input_filenames)),
        'gzip -cn'],
        outfile=pooled_filename)

    pooled = dxpy.upload_local_file(pooled_filename)

    output = {
        "pooled": dxpy.dxlink(pooled)
    }

    return output

dxpy.run()
