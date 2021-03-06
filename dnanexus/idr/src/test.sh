#!/bin/bash
# create_idr_venv 0.0.1
# Generated by dx-app-wizard.
#
# Basic execution pattern: Your app will run on a single machine from
# beginning to end.
#
# Your job's input variables (if any) will be loaded as environment
# variables before this script runs.  Any array inputs will be loaded
# as bash arrays.
#
# Any code outside of main() (or any entry point you may add) is
# ALWAYS executed, followed by running the entry point itself.
#
# See https://wiki.dnanexus.com/Developer-Portal for tutorials on how
# to modify this file.

main() {

    cd idr
    mkdir test
    cd test
    idr --plot --samples ../tests/data/peak1 ../tests/data/peak2
    ls -l

    # venv_tarfile=$(dx upload $venv_tarfile_name --brief)

    # # The following line(s) use the utility dx-jobutil-add-output to format and
    # # add output variables to your job's output as appropriate for the output
    # # class.  Run "dx-jobutil-add-output -h" for more information on what it
    # # does.

    # dx-jobutil-add-output venv_tarfile "$venv_tarfile" --class=file
}
