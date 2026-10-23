# Borneo HazeWatch 🌿

**A Python-based hotspot monitoring and reporting tool for parts of Borneo, Indonesia.**

Borneo HazeWatch retrieves hotspot data from NASA's Fire Information for Resource Management System (FIRMS), processes the data within a configured geographic area, calculates monitoring metrics, and generates daily summaries.

The project aims to provide a structured foundation for monitoring hotspot activity and supporting further analysis of potential fire events.

# Features

- **Hotspot data retrieval** — Retrieves hotspot observations from NASA FIRMS.
- **Data processing** — Cleans hotspot records, validates coordinates, and filters observations to the configured geographic boundaries.
- **Monitoring metrics** — Calculates hotspot totals, high-confidence observations, total Fire Radiative Power (FRP), the most concentrated hotspot area, and changes relative to previous metrics when available.
- **Daily summaries** — Generates human-readable reports from calculated metrics.
- **Local storage** — Saves metrics and reports for later reference.
- **Data validation** — Uses Pydantic models to validate monitoring metrics.
- **Automated testing** — Runs the Python test suite through GitHub Actions.

## Tech Stack

- Python 3.13
- Pandas
- Requests
- Pydantic
- python-dotenv
- Pytest
- GitHub Actions

# Project Structure

```text
borneo-hazewatch/
├── .github/
│   └── workflows/
│       └── tests.yml
├── data/
│   ├── metrics/
│   └── reports/
├── hazewatch/
│   ├── __init__.py
│   ├── config.py
│   ├── fetch_hotspot.py
│   ├── main.py
│   ├── models.py
│   ├── process.py
│   ├── storage.py
│   └── summarize.py
├── test/
├── .env
├── .gitignore
├── CONTRIBUTING.md
├── README.md
└── requirements.txt
```

Runtime data and environment files should remain local and must not be committed unless explicitly required.

# Requirements

- Python 3.13 or a compatible Python version supported by the project dependencies.
- A NASA FIRMS API key for retrieving hotspot data.
- Git.

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/Rey759/borneo-hazewatch.git
cd borneo-hazewatch
```

## 2. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install the test dependency:

```bash
python -m pip install pytest
```

## 4. Configure Environment Variables

Create a `.env` file in the project root and add your NASA FIRMS API key:

```dotenv
FIRMS_MAP_KEY=your_firms_api_key_here
```

The application uses the `FIRMS_MAP_KEY` environment variable to access NASA FIRMS hotspot data from the `VIIRS_SNPP_NRT` source.

Replace `your_firms_api_key_here` with your own API key.

**Security note:** Never commit your `.env` file or share your API key publicly.

# Running the Project

Run the main application from the project root:

```bash
python -m hazewatch.main
```

The application retrieves and processes hotspot data, calculates monitoring metrics, validates the results, and saves the generated metrics and report according to the project configuration.

Check `hazewatch/config.py` for the required environment variables and `hazewatch/main.py` for the application entry point.

# Running Tests

Run the test suite from the project root:

```bash
python -m pytest -v
```

GitHub Actions also runs the test suite when changes are pushed to `main` or `dev`, and when pull requests target those branches.

# Contribution Workflow

We use the following branch strategy:

- `main` — Stable branch protected by repository rules.
- `dev` — Integration branch for ongoing development.
- `feature/<name>` — New features.
- `fix/<name>` — Bug fixes.
- `docs/<name>` — Documentation changes.

Contributors should submit pull requests instead of pushing directly to `main`.

For detailed instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).

# Data Source

Hotspot observations are retrieved from NASA's Fire Information for Resource Management System (FIRMS).

- [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/)

Hotspot detections indicate potential fire activity and should not automatically be interpreted as confirmed fires.

# Project Status

Borneo HazeWatch is under active development. Features, monitoring methods, and reporting capabilities may evolve as the project grows.

# License

No license has been specified yet. Until a license is added to this repository, reuse and redistribution permissions should not be assumed.