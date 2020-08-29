 .. Copyright (c) 2019-2020 Jürgen Mülbert. All rights reserved.

 .. Licensed under the EUPL, Version 1.2 or – as soon they
    will be approved by the European Commission - subsequent
    versions of the EUPL (the "Licence");
    You may not use this work except in compliance with the
    Licence.

 .. You may obtain a copy of the Licence at:
    https://joinup.ec.europa.eu/page/eupl-text-11-12

 .. Unless required by applicable law or agreed to in
    writing, software distributed under the Licence is
    distributed on an "AS IS" basis,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
    express or implied.
    See the Licence for the specific language governing
    permissions and limitations under the Licence.

 .. Lizenziert unter der EUPL, Version 1.2 oder - sobald
    diese von der Europäischen Kommission genehmigt wurden -
    Folgeversionen der EUPL ("Lizenz");
    Sie dürfen dieses Werk ausschließlich gemäß
    dieser Lizenz nutzen.

 .. Eine Kopie der Lizenz finden Sie hier:
    https://joinup.ec.europa.eu/page/eupl-text-11-12

 .. Sofern nicht durch anwendbare Rechtsvorschriften
    gefordert oder in schriftlicher Form vereinbart, wird
    die unter der Lizenz verbreitete Software "so wie sie
    ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
    ausdrücklich oder stillschweigend - verbreitet.
    Die sprachspezifischen Genehmigungen und Beschränkungen
    unter der Lizenz sind dem Lizenztext zu entnehmen.

Contributor Guide
=================

Thank you for your interest in improving this project.
This project is open-source under the `EUPL-1.2 license`_ and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- `Source Code`_
- `Documentation`_
- `Issue Tracker`_
- `Code of Conduct`_

.. _EUPL-1.2 license: https://opensource.org/licenses/EUPL-1.2
.. _Source Code: https://github.com/jmuelbert/jmopenorders
.. _Documentation: https://jmopenorders.readthedocs.io/
.. _Issue Tracker: https://github.com/jmuelbert/jmopenorders/issues

How to report a bug
-------------------

Report bugs on the `Issue Tracker`_.

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.


How to request a feature
------------------------

Request features on the `Issue Tracker`_.


How to set up your development environment
------------------------------------------

You need Python 3.6+ and the following tools:

- Poetry_
- Nox_

Install the package with development requirements:

.. code:: console

   $ poetry install

You can now run an interactive Python session,
or the command-line interface:

.. code:: console

   $ poetry run python
   $ poetry run jmopenorders

.. _Poetry: https://python-poetry.org/
.. _Nox: https://nox.thea.codes/


How to test the project
-----------------------

Run the full test suite:

.. code:: console

   $ nox

List the available Nox sessions:

.. code:: console

   $ nox --list-sessions

You can also run a specific Nox session.
For example, invoke the unit test suite like this:

.. code:: console

   $ nox --session=tests

Unit tests are located in the ``tests`` directory,
and are written using the pytest_ testing framework.

.. _pytest: https://pytest.readthedocs.io/


How to submit changes
---------------------

Open a `pull request`_ to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

You can ensure that your changes adhere to the code style by reformatting with Black_:

.. code:: console

   $ nox --session=black

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.

.. _pull request: https://github.com/jmuelbert/jmopenorders/pulls
.. _Black: https://black.readthedocs.io/
.. github-only
.. _Code of Conduct: CODE_OF_CONDUCT.rst
