<!--
 Copyright (c) 2019-2020 Jürgen Mülbert. All rights reserved.

 Licensed under the EUPL, Version 1.2 or – as soon they
 will be approved by the European Commission - subsequent
 versions of the EUPL (the "Licence");
 You may not use this work except in compliance with the
 Licence.
 You may obtain a copy of the Licence at:

 https://joinup.ec.europa.eu/page/eupl-text-11-12

 Unless required by applicable law or agreed to in
 writing, software distributed under the Licence is
 distributed on an "AS IS" basis,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 express or implied.
 See the Licence for the specific language governing
 permissions and limitations under the Licence.

 Lizenziert unter der EUPL, Version 1.2 oder - sobald
 diese von der Europäischen Kommission genehmigt wurden -
 Folgeversionen der EUPL ("Lizenz");
 Sie dürfen dieses Werk ausschließlich gemäß
 dieser Lizenz nutzen.
 Eine Kopie der Lizenz finden Sie hier:

 https://joinup.ec.europa.eu/page/eupl-text-11-12

 Sofern nicht durch anwendbare Rechtsvorschriften
 gefordert oder in schriftlicher Form vereinbart, wird
 die unter der Lizenz verbreitete Software "so wie sie
 ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
 ausdrücklich oder stillschweigend - verbreitet.
 Die sprachspezifischen Genehmigungen und Beschränkungen
 unter der Lizenz sind dem Lizenztext zu entnehmen.
 -->

# Docker for jmopenorders

## Installation

To create Docker you need to run:

```bash
make docker
```

which is equivalent to:

```bash
make docker VERSION=latest
```

You could also provide name and version for the image itself.
Default name is `IMAGE := {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}`.
Default version is `VERSION := latest`.

```bash
make docker IMAGE=some_name VERSION={{ cookiecutter.version }}
```

## Usage

```bash
docker run -it --rm \
   -v $(pwd):/workspace \
   {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} bash
```

## How to clean up

To uninstall docker image run `make clean_docker` with `VERSION`:

```bash
make clean_docker VERSION={{ cookiecutter.version }}
```

like in installation, you can also choose the image name

```bash
make clean_docker IMAGE=some_name VERSION=latest
```

If you want to clean all, including `build` run `make clean`
