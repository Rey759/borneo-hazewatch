# Contribution Workflow Test

This file verifies the contribution workflow for Borneo HazeWatch.

## Objectives

- Verify that contributors can work on separate branches.
- Verify that pull requests can target the `dev` branch.
- Verify that GitHub Actions runs automated tests for pull requests.
- Keep the `main` branch protected from unreviewed changes.

## Expected Workflow

1. Create a dedicated feature or documentation branch.
2. Commit and push changes to that branch.
3. Open a pull request targeting `dev`.
4. Confirm that the automated test workflow completes successfully.
5. Review and merge the pull request.