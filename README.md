# Behave + Selenium POM Starter

A clean, opinionated **BDD test automation framework** built with [Behave](https://behave.readthedocs.io/) and Selenium WebDriver, using the Page Object Model. Ships with a parameterised test runner, HTML reports with failure screenshots, and a Jenkins pipeline definition.

## What this framework demonstrates

- **Behave BDD** with Gherkin feature files and step definitions
- **Page Object Model** for clean separation of test logic and page structure
- **Parameterised runner** (`runner.py`) that accepts tags, output format, and a target test directory
- **HTML reports** via [behave-html-pretty-formatter](https://github.com/bhavin192/behave-html-pretty-formatter) with screenshots automatically embedded on failures
- **Jenkins pipeline** (`Jenkinsfile`) ready to drop into a freestyle or multi-branch job
- **URL-agnostic** — point it at any web app by editing `config.ini`

## Example target

The default `config.ini` points at [**osdatahub.os.uk**](https://osdatahub.os.uk/) — Ordnance Survey's public open-data portal — because it's a real, free-to-access website with a rich navigation tree (Home, API Dashboard, Download, Docs, Support, Plans) that exercises Page Objects properly rather than a toy login form. Swap in any other URL without touching framework code.

## Quick start

```bash
git clone https://github.com/afridiharis/behave-selenium-pom-starter.git
cd behave-selenium-pom-starter

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Run all tests

```bash
python runner.py --test_dir=Features
```

### Run a single tagged scenario

```bash
python runner.py --behave_options='--tags=download_page' --test_dir=Features
```

### Run and generate an HTML report

```bash
python runner.py --behave_options='--tags=download_page' --output_html=yes --test_dir=Features
```

Reports are written to `reports/behave-report.html`.

## Project layout

```
.
├── CommonFuncs/              # Shared helpers used by page objects
│   ├── ConfigReader.py       # Reads config.ini
│   └── WebCommon.py          # Selenium wrappers: waits, clicks, asserts, screenshots
├── Features/                 # Gherkin feature files, step defs, page objects
│   ├── environment.py        # Behave hooks (before/after scenario, failure screenshots)
│   ├── OS_data_hub.feature   # Example scenarios against the OS Data Hub
│   ├── Pages/                # Page Object Model classes
│   │   ├── BasePage.py
│   │   ├── HomePage.py
│   │   ├── APIDashboardPage.py
│   │   ├── DownloadPage.py
│   │   ├── DocsPage.py
│   │   ├── SupportPage.py
│   │   └── PlansPage.py
│   └── steps/                # Step definitions, one file per feature area
├── behave.ini                # Behave formatter + reporter config
├── config.ini                # Target URL + browser
├── requirements.txt          # Python dependencies
├── runner.py                 # Parameterised test runner
└── Jenkinsfile               # Jenkins pipeline
```

## Jenkins integration

The included `Jenkinsfile` uses `checkout scm` so it works with any Jenkins job that points at this repository — no hardcoded URLs. Parameterise your job with `tags` and `test_dir` string parameters to control which tests run. The pipeline:

1. Checks out the repo
2. Creates a Python virtualenv and installs requirements
3. Runs `runner.py` with the supplied tag filter
4. Archives `reports/*.html` as build artefacts

## Configuration

`config.ini` is the single source of truth for the target URL and browser:

```ini
[test config]
url=https://osdatahub.os.uk/
browser=chrome
```

Supported browsers: `chrome`, `firefox` (extend `Features/environment.py` to add more).

## Requirements

- Python 3.10+
- Chrome or Firefox installed locally (Selenium 4 manages the driver binary automatically)
- `pip`

## Why this exists

Most open-source BDD framework examples target toy demo sites (SauceDemo, the-internet.herokuapp.com). This one targets a real, production, publicly-accessible website so the page objects and selectors reflect the kind of noise, timing, and structural variance you hit in real work.

## License

MIT — see [LICENSE](LICENSE).
