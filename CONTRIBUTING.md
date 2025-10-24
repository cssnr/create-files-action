# Contributing

> [!WARNING]  
> This guide is a work in progress and may not be complete.

- [Workflow](#Workflow)
  - [Testing](#Testing)
- [Actions Development](#Actions-Development)
- [Old Development Section](#old-development-section)

This is a basic contributing guide and is a work in progress.

## Workflow

1. Fork the repository.
2. Create a branch in your fork!
3. Make your changes.
4. [Test](#Testing) your changes.
5. Commit and push your changes.
6. Create a PR to this repository.
7. Verify the tests pass, otherwise resolve.
8. Make sure to keep your branch up-to-date.

## Testing

GitHub is easier to set up, but you have to push your commits to test.  
Running locally is harder to set up, but it is much easier to test; and by far recommended!

### GitHub

Since `GITHUB_TOKEN` does NOT have to be added as a secret and is automatically generated every run there is nothing to do.

When you push your branch to your repository, the [test.yaml](.github/workflows/test.yaml) should run...

### Locally

To run actions locally you need to install act: https://nektosact.com/installation/index.html

1. Create a `.secrets` file with: `GITHUB_TOKEN="ghp_xxx"`
2. Run: `act -j test`

Note: You need to have your current commit pushed as this makes a tag on GitHub to the current sha.
This means the `test` will most likely fail on a third-party PR since the automatic GITHUB_TOKEN won't have write access to content.

The `test` ephemerally updates the [action.yml](action.yml) to use the [Dockerfile](Dockerfile).
This ensures the test will always use your local changes.

To test the docker image, you need to build an image with a tag matching the [action.yml](action.yml)
image and run act with `--action-offline-mode`. This script does it all for you, just run: [build.sh](build.sh)

To see all available jobs run: `act -l`

# Actions Development

A GitHub Actions Primer: https://docs.github.com/en/actions/sharing-automations/creating-actions

For other Action types, see:

- JavaScript: https://github.com/smashedr/js-test-action
- TypeScript: https://github.com/smashedr/ts-test-action
- Docker: https://github.com/cssnr/create-files-action
- Python: https://github.com/smashedr/py-test-action (DEPRECATED)

The heart of a GitHub Action is the [action.yml](action.yml) file. This describes everything about your action.

- https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions

JavaScript Actions must be fully built in the action's environment. See the `build` in [package.json](package.json) for details.

# Old Development Section

<!-- TODO: Update this section -->

If you would like to submit a PR, please review the [CONTRIBUTING.md](CONTRIBUTING.md).

You can test actions locally with: https://github.com/nektos/act

1. Install `act`: https://nektosact.com/installation/index.html
2. Create a `.secrets` file with: `GITHUB_TOKEN="ghp_xxx"`
3. Run `act -j test`

Note: You need to have a commit pushed as this makes a tag on GitHub for the current sha.

For advanced using with things like secrets, variables and context see: https://nektosact.com/usage/index.html

You should also review the options from `act --help`

Note, the `.env`, `.secrets` and `.vars` files are automatically sourced with no extra options.
To source `event.json` you need to run act with `act -e event.json`

To use a locally built image enable offline mode: `--action-offline-mode`
