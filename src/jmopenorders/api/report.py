# -*- coding: utf-8 -*-
#
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
#  diese von der Europäischen Kommission genehmigt wurden -
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
#
"""Generate the output in a xlsx file."""
import os

from . import cleanoutputdir
from . import generateorders
from . import getdata
from . import getserviceperson
from jmopenorders.core.logger import logger


def report(
    personfile: str = "names.csv",
    datafile: str = "data.csv",
    inputpath: str = "home",
    outputpath: str = "out",
) -> None:
    """Generate the report.

    The report function is the entrypoint for reporting.

    Args:
        personfile: the csv-file with the names of the servicepersons
        datafile: the csv-file with the orders of all servicepresons
        inputpath: the path where stored the datafiles
        outputpath: the path to stored the xlsx-files.
    """
    logger.debug("executing report command")

    # combine the inputpath with the personfile name
    persondata_file = os.path.join(os.path.abspath(inputpath), personfile)

    logger.debug(f"Personfile= {persondata_file}")

    # Get the names of the persons to an arrary
    names = getserviceperson.GetServicePerson(persondata_file)
    berater = names.get()

    # Get the data
    data_file = os.path.join(os.path.abspath(inputpath), datafile)
    data = getdata.GetData(data_file)
    orders = data.get()

    cleanoutputdir.CleanOutputDir(os.path.abspath(outputpath))

    if type(berater) is list:
        for actual_berater in berater:
            logger.debug("actual_berater: " + actual_berater)
            berater_name = actual_berater
            logger.debug("Berater Name: " + berater_name)
            create_table = generateorders.GenerateOrders(outputpath)
            create_table.create(
                actual_name=berater_name, actual_content=orders,
            )
    else:
        logger.critical("Berater file is empty or not exist")
