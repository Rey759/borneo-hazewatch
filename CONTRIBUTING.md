# Contributing to Borneo HazeWatch

Thank you for your interest in contributing to Borneo HazeWatch!

Borneo HazeWatch is a Python project that collects, processes, and summarizes hotspot data for parts of Borneo using NASA FIRMS data.

We welcome bug reports, feature suggestions, documentation improvements, and code contributions.

# 1. Branching Strategy

We use the following branches:

- `main`: Stable branch. Changes must be submitted through a pull request.
- `dev`: Integration branch for ongoing development.
- `feature/<name>`: New features.
- `fix/<name>`: Bug fixes.
- `docs/<name>`: Documentation changes.

Do not push changes directly to `main`.

# 2. Getting Started

1. Fork the repository if you are an external contributor.
2. Clone your fork:

   ```bash
   git clone https://github.com/YOUR_USERNAME/borneo-hazewatch.git
   cd borneo-hazewatch
   ```

3. Create and activate a virtual environment.

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

4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   python -m pip install pytest
   ```

5. Configure environment variables as required by the project. Never commit API keys, credentials, or `.env` files.

# 3. Create a Branch

Create a descriptive branch for your changes.

Examples:

```bash
git switch -c feature/hotspot-map
git switch -c fix/invalid-coordinates
git switch -c docs/update-installation-guide
```

External contributors should work in their forks and submit pull requests to this repository.

# 4. Make and Test Changes

- Keep changes focused and easy to review.
- Follow the existing project structure and coding style.
- Add or update tests when changing application behavior.
- Run the test suite before submitting a pull request:

  ```bash
  python -m pytest -v
  ```

- Make sure the GitHub Actions workflow passes.

# 5. Pull Request Process

1. Push your branch to your fork or authorized remote.
2. Open a pull request targeting `dev` for ongoing development.
3. Explain what changed and why.
4. Include relevant test results.
5. Respond to review feedback and update your branch when needed.

Changes intended for a stable release can be proposed from `dev` to `main` after they have been reviewed and tested.

All pull requests targeting `main` must pass the required status checks configured by the repository.

# 6. Data and Secrets

- Never commit API keys, access tokens, passwords, or private credentials.
- Do not commit `.env` files.
- Do not commit generated runtime data or reports unless explicitly requested by a maintainer.
- Verify `git status` before committing.

# 7. Reporting Bugs and Suggesting Features

When reporting a bug, include:

- A clear description of the problem.
- Steps to reproduce it.
- Expected and actual behavior.
- Relevant error messages or logs, with secrets removed.

For feature requests, explain the use case and the expected benefit.

Thank you for helping improve Borneo HazeWatch!