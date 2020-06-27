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
"""Generator for fake data for testing."""
import csv
import os
from datetime import date
from typing import List

from faker import Factory
from openpyxl import Workbook


class CreateFakeOrders:
    """Fake-Data creator data for testing."""

    def __init__(self, my_data_path: str, l18n: str) -> None:
        """Init for the fake-data-generator.

        Args:
            my_data_path: the path to store the fake data
            l18n: the localization for the fake data
        """
        self.data_path = my_data_path
        self.part_person: List[str] = []
        self.service_person: List[str] = []
        self.order_list: List[List[str]] = []
        self.workshop_count: int = 0
        self.part_count: int = 0

        if l18n == "":
            l18n = "de_DE"

        self.fake = Factory.create(l18n)

    def generate_part_person(self, count: int) -> None:
        """Generate random names for parts-person.

        Args:
            count: Count of parts persons to generate.
        """
        for _ in range(0, count):
            self.part_person.append(
                self.fake.first_name() + " " + self.fake.last_name(),
            )

    def generate_service_person(self, count: int) -> None:
        """Generate random names for service persons.

        Args:
            count: Count of parts persons to generate.
        """
        for _ in range(0, count):
            self.service_person.append(
                self.fake.last_name() + ", " + self.fake.first_name(),
            )

    def generate_header(self) -> None:
        """Generate Headers."""
        line = ["", "", "", "", "", "", "OFFENE AUFTRÄGE"]
        self.order_list.append(line)
        line = ["MANDANT", ""]
        self.order_list.append(line)
        line = ["Filiale", "", self.fake.random_int(1, 10)]
        self.order_list.append(line)
        line = ["BENUTZER-ID", ""]
        self.order_list.append(line)
        line = ["Bereich", "Wekstatt & Teile"]
        self.order_list.append(line)
        self.order_list.append([""])
        line = [
            "",
            "Auftrag Nr.",
            "Hauptbereich",
            "Auftragsdatum",
            "Tage offen",
            "Deb.-Nr.",
            "Deb.-Name",
            "Verkäufer Serviceberater",
            "Arbeitswert",
            "Teile",
            "Fremdleistung",
            "Andere",
            "Gesamt",
            "Auftragswert bereits geliefert",
        ]

        self.order_list.append(line)

    def generate_orders(self, count: int = 20, workshop: bool = True) -> None:
        """Generate workshop orders.

        Args:
            count: The count of fake datalines.
            workshop: Is true when tha dataline should generated for the workshop.
        """
        for _ in range(0, count):
            if workshop is True:
                self.workshop_count = count
                line = [
                    "",
                    "WK" + self.fake.numerify(text="######"),
                    "Werkstatt",
                ]
            else:
                self.part_count = count
                line = ["", "ET" + self.fake.numerify(text="######"), "Teile"]
            fake_date = self.fake.date_between(start_date="-2y", end_date="+1y")
            line.append(fake_date.strftime("%d.%m.%Y"))
            date_now = date.today()
            delta = date_now - fake_date
            line.append(delta.days)
            line.append(self.fake.numerify(text="######"))
            line.append(self.fake.name())
            if workshop is True:
                line.append(
                    self.service_person[
                        self.fake.random_int(0, len(self.service_person) - 1,)
                    ],
                )
            else:
                line.append(
                    self.part_person[
                        self.fake.random_int(0, len(self.part_person) - 1,)
                    ],
                )
            if workshop is True:
                line.append(self.fake.numerify(text="####,##"))
            else:
                line.append("0,00")
            line.append(self.fake.numerify(text="####,##"))
            if workshop is True:
                line.append(self.fake.numerify(text="####,##"))
                line.append(self.fake.numerify(text="####,##"))
            else:
                line.append("0,00")
                line.append("0,00")
            line.append(self.fake.numerify(text="####,##"))
            line.append(self.fake.numerify(text="####,##"))
            self.order_list.append(line)

    def generate_splitter(self, workshop: bool = True) -> None:
        """Generate a sub header.

        Args:
            workshop: True when generate the header for the workshop
        """
        self.order_list.append([""])
        if workshop is True:
            line: List[str] = ["Gesamt Werkstatt", str(self.workshop_count)]
        else:
            line = ["Gesamt Teile", str(self.part_count)]
        self.order_list.append(line)
        if workshop is True:
            line = [
                "Durchschnitt Werkstatt",
                str(self.fake.random_int(1, self.workshop_count)),
            ]
        else:
            line = [
                "Durchschnitt Werkstatt",
                str(self.fake.random_int(1, self.part_count)),
            ]

        self.order_list.append(line)
        self.order_list.append([""])

    def csv_output(self, name: str) -> None:
        """Write the data to a csv file.

        Args:
            name: The name for the output file.
        """
        with open(os.path.join(self.data_path, name), "w", newline="",) as csvfile:
            orderswriter = csv.writer(csvfile, delimiter=";")
            for row in self.order_list:
                orderswriter.writerow(row)

    def xlsx_output(self, name: str) -> None:
        """Write the data to a excel file.

        Args:
            name: The name for the output file.
        """
        wb = Workbook()
        ws = wb.active
        column_num = 1
        row_num = 1

        for row in self.order_list:
            for cell in row:
                ws.cell(row_num, column_num).value = cell
                column_num += 1
            row_num += 1
            column_num = 1

        wb.save(os.path.join(self.data_path, name))


def main() -> None:
    """Entrypoint to generate test data."""
    orders = CreateFakeOrders(".", "de_DE")
    orders.generate_part_person(20)
    orders.generate_service_person(50)
    orders.generate_header()
    orders.generate_orders(count=1000, workshop=True)
    orders.generate_splitter(workshop=True)
    orders.generate_orders(count=200, workshop=False)
    orders.generate_splitter(workshop=False)
    orders.csv_output("orders.csv")
    orders.xlsx_output("orders.xlsx")


if __name__ == "__main__":
    main()
