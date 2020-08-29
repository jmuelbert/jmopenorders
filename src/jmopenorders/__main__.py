#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019-2020 Jürgen Mülbert. All rights reserved.
#
# Licensed under the EUPL, Version 1.2 or – as soon they
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
#
# Lizenziert unter der EUPL, Version 1.2 oder - sobald
# diese von der Europäischen Kommission genehmigt wurden -
# Folgeversionen der EUPL ("Lizenz");
# Sie dürfen dieses Werk ausschließlich gemäß
# dieser Lizenz nutzen.
# Eine Kopie der Lizenz finden Sie hier:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Sofern nicht durch anwendbare Rechtsvorschriften
# gefordert oder in schriftlicher Form vereinbart, wird
# die unter der Lizenz verbreitete Software "so wie sie
# ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
# ausdrücklich oder stillschweigend - verbreitet.
# Die sprachspezifischen Genehmigungen und Beschränkungen
# unter der Lizenz sind dem Lizenztext zu entnehmen.
"""Console script for jmopenorders."""
import sys

import click

from jmopenorders.api.report import report


@click.command()
@click.version_option()
@click.option("-i", "--inputpath", default="input", help="The Inputpath for the data")
@click.option(
    "-o",
    "--outputpath",
    default="output",
    help="The Outputpath for the data",
)
@click.option(
    "-p", "--personfile", default="persons.csv", help="The Name of the personfile"
)
@click.option("-d", "--datafile", default="orders.csv", help="The Name of the datafile")
def main(inputpath: str, outputpath: str, personfile: str, datafile: str) -> int:
    r"""jmopenorders, generate separate files from datafile.

    \f
    Todo: Change the paths to the click Type Path integrate config.

    Args:
        inputpath: The path to the inputdata.
        outputpath: The path for write the generated data.
        personfile: the name for the personfile.
        datafile: the name for the datafile.

    Returns:
        Status as int (0 is good)
    """
    report(personfile, datafile, inputpath, outputpath)

    return 0


# Make the module executable.
if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
