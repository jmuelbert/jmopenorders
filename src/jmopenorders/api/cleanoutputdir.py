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
"""Clean the Directory.

Remove the generated files
"""
import os

from ..core.logger import logger


class CleanOutputDir:
    """Clean the output directory."""

    def __init__(self, outdir: str = "") -> None:
        """Init the CleanOutputDir Class.

        Args:
            outdir: The name of the output directory.
        """
        self.out_dir = os.path.abspath(outdir)

    def clean(self) -> None:
        """Before write the new excel files, remove the old ones."""
        if os.path.isdir(self.out_dir):
            files = os.listdir(self.out_dir)
            for file in files:
                if ".xlsx" in file:
                    os.remove(file)
                    logger.debug(f"Remove File: {file}")
        else:
            logger.warn(f"The Outdir {self.out_dir} does not exists")
