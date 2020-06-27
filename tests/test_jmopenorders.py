#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Jürgen Mülbert. All rights reserved.
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
"""Tests for `jmopenorders` package."""
import pytest

from jmopenorders.__main__ import main


@pytest.fixture
def response() -> None:
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # noqa  import requests
    # noqa return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument.

    Args:
        response: The Response String
    """
    # noqa from bs4 import BeautifulSoup
    # noqa assert 'GitHub' in BeautifulSoup(response.content).title.string


@pytest.mark.parametrize(
    ("input_path", "output_path", "person_file", "data_file", "expected"),
    [("~/test/data", "~/test/output", "person.csv", "data.csv", "good")],
)
def test_command_line_interface(
    input_path: str, output_path: str, person_file: str, data_file: str, expected: bool
) -> None:
    """Test the CLI.

    Args:
        input_path: The path to the directory for input data files.
        output_path: The path to the directory for the generated files.
        person_file: The data_file that holds the service persons.
        data_file: The file with all ordersdata to split off.
        expected: The expected result.
    """
    assert main(input_path, output_path, person_file, data_file) == expected
