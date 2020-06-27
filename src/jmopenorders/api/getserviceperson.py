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
"""Read the serviceperson csv-file."""
import csv
from typing import List

from jmopenorders.core.logger import logger


class GetServicePerson:
    """Get the service persion from csv-file."""

    def __init__(self, filename: str) -> None:
        """Init the GetServicePerson Class.

        Args:
            filename: The Filename for the datafile with the service persons.
        """
        self.file_name = filename

    def get(self) -> List[str]:
        """Get the Persons.

        Returns:
             List - the List of the Persons.

        Read the Service Person from csv-file.
        Then create a array and get this back
        """
        service_person = []
        try:
            with open(self.file_name) as berater_file:
                berater = csv.DictReader(berater_file, delimiter=";", quotechar='"',)

                for row in berater:

                    service_person.append(row["Name"])

                return service_person

        except OSError:
            logger.debug(
                "The File for the service persons {} does not exists".format(
                    self.file_name
                )
            )

            return []
