[![Actions Tools](https://img.shields.io/badge/python-actions_toolkit-4584b6?logo=python&logoColor=ffde57)](https://actions-tools.cssnr.com/)
[![GitHub Tag Major](https://img.shields.io/github/v/tag/cssnr/create-files-action?sort=semver&filter=!v*.*&logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/create-files-action/tags)
[![GitHub Tag Minor](https://img.shields.io/github/v/tag/cssnr/create-files-action?sort=semver&filter=!v*.*.*&logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/create-files-action/releases)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/create-files-action?logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/create-files-action/releases/latest)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/create-files-action/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/create-files-action/actions/workflows/test.yaml)
[![Workflow Lint](https://img.shields.io/github/actions/workflow/status/cssnr/create-files-action/lint.yaml?logo=cachet&label=lint)](https://github.com/cssnr/create-files-action/actions/workflows/lint.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_create-files-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_create-files-action)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/create-files-action?logo=github&label=updated)](https://github.com/cssnr/create-files-action/pulse)
[![Codeberg Last Commit](https://img.shields.io/gitea/last-commit/cssnr/create-files-action/master?gitea_url=https%3A%2F%2Fcodeberg.org%2F&logo=codeberg&logoColor=white&label=updated)](https://codeberg.org/cssnr/create-files-action)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/create-files-action?logo=bookstack&logoColor=white&label=repo%20size)](https://github.com/cssnr/create-files-action?tab=readme-ov-file#readme)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/create-files-action?logo=htmx)](https://github.com/cssnr/create-files-action)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/create-files-action?logo=github)](https://github.com/cssnr/create-files-action/graphs/contributors)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/create-files-action?logo=github)](https://github.com/cssnr/create-files-action/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/create-files-action?style=flat&logo=github)](https://github.com/cssnr/create-files-action/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/create-files-action?style=flat&logo=github)](https://github.com/cssnr/create-files-action/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# Create Files Action

- [Inputs](#Inputs)
- [Outputs](#Outputs)
- [Types](#Types)
- [Examples](#Examples)
- [Contributing](#Contributing)

Easily create various file [types](#Types) with custom options.
Write the data to a file or use the [output](#Outputs).

## Inputs

| Input         |  Default   | Input&nbsp;Description |
| :------------ | :--------: | :--------------------- |
| [type](#type) | _Required_ | Type of File to Create |
| [file](#file) |     -      | Output File to Create  |
| [data](#data) |     -      | File Data for `type`   |

#### type

Currently only supports [redirect](#redirect) html file.

#### file

Output file path to write file; otherwise use the [output](#Outputs).

#### data

[Type](#Types) specific data in YAML format.

<details><summary>How to Pass Data</summary>

```yaml
data: |
  url: https://smashedr.github.io/github-projects/
  text: /github-projects
  title: Ralf Broke It
  timer: 5
```

</details>

## Outputs

| Output  | Description  |
| :------ | :----------- |
| content | File Content |

```yaml
- name: 'Create Files Action'
  id: files
  uses: cssnr/create-files-action@master

- name: 'Echo Output'
  run: |
    echo "content: '${{ steps.files.outputs.content }}'"
```

## Types

### redirect

Creates an HTML redirect page with timer and link.

| Data  | Default&nbsp;Value | Description&nbsp;of&nbsp;Input |
| :---- | :----------------- | :----------------------------- |
| url   | -                  | URL to Redirect too            |
| text  | _url_              | Text for URL link              |
| title | `Redireting`       | Title of the page              |
| timer | `5`                | Redirect timer seconds         |

<details><summary>View Step Example</summary>

```yaml
- name: 'Redirect'
  id: redirect
  uses: cssnr/create-files-action@master
  with:
    type: 'redirect'
    file: 'index.html'
    data: |
      url: https://smashedr.github.io/github-projects/
      text: /github-projects
      title: Rolf Broke
      timer: 3
```

</details>

### robots

Creates a robots.txt to block all robots.

<details><summary>View Step Example</summary>

```yaml
- name: 'Robots'
  id: robots
  uses: cssnr/create-files-action@master
  with:
    type: 'robots'
    file: 'robots.txt'
```

</details>

## Examples

💡 _Click on an example heading to expand or collapse the example._

Coming soon.

For more examples, you can check out other projects using this action:  
https://github.com/cssnr/create-files-action/network/dependents

# Support

For general help or to request a feature see:

- Q&A Discussion: https://github.com/cssnr/create-files-action/discussions/categories/q-a
- Request a Feature: https://github.com/cssnr/create-files-action/discussions/categories/feature-requests

If you are experiencing an issue/bug or getting unexpected results you can:

- Report an Issue: https://github.com/cssnr/create-files-action/issues
- Chat with us on Discord: https://discord.gg/wXy6m2X8wY
- Provide General Feedback: [https://cssnr.github.io/feedback/](https://cssnr.github.io/feedback/?app=Stack%20Deploy)

For more information, see the CSSNR [SUPPORT.md](https://github.com/cssnr/.github/blob/master/.github/SUPPORT.md#support).

# Contributing

If you would like to submit a PR, please review the [CONTRIBUTING.md](#contributing-ov-file).

Please consider making a donation to support the development of this project
and [additional](https://cssnr.com/) open source projects.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cssnr)

[![Actions Tools](https://raw.githubusercontent.com/smashedr/repo-images/refs/heads/master/actions/actions-tools.png)](https://actions-tools.cssnr.com/)

Additionally, you can support other [GitHub Actions](https://actions.cssnr.com/) I have published:

- [Stack Deploy Action](https://github.com/cssnr/stack-deploy-action?tab=readme-ov-file#readme)
- [Portainer Stack Deploy Action](https://github.com/cssnr/portainer-stack-deploy-action?tab=readme-ov-file#readme)
- [Docker Context Action](https://github.com/cssnr/docker-context-action?tab=readme-ov-file#readme)
- [Actions Up Action](https://github.com/cssnr/actions-up-action?tab=readme-ov-file#readme)
- [Zensical Action](https://github.com/cssnr/zensical-action?tab=readme-ov-file#readme)
- [VirusTotal Action](https://github.com/cssnr/virustotal-action?tab=readme-ov-file#readme)
- [Mirror Repository Action](https://github.com/cssnr/mirror-repository-action?tab=readme-ov-file#readme)
- [Update Version Tags Action](https://github.com/cssnr/update-version-tags-action?tab=readme-ov-file#readme)
- [Docker Tags Action](https://github.com/cssnr/docker-tags-action?tab=readme-ov-file#readme)
- [TOML Action](https://github.com/cssnr/toml-action?tab=readme-ov-file#readme)
- [Update JSON Value Action](https://github.com/cssnr/update-json-value-action?tab=readme-ov-file#readme)
- [JSON Key Value Check Action](https://github.com/cssnr/json-key-value-check-action?tab=readme-ov-file#readme)
- [Parse Issue Form Action](https://github.com/cssnr/parse-issue-form-action?tab=readme-ov-file#readme)
- [Cloudflare Purge Cache Action](https://github.com/cssnr/cloudflare-purge-cache-action?tab=readme-ov-file#readme)
- [Mozilla Addon Update Action](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
- [Package Changelog Action](https://github.com/cssnr/package-changelog-action?tab=readme-ov-file#readme)
- [NPM Outdated Check Action](https://github.com/cssnr/npm-outdated-action?tab=readme-ov-file#readme)
- [Label Creator Action](https://github.com/cssnr/label-creator-action?tab=readme-ov-file#readme)
- [Algolia Crawler Action](https://github.com/cssnr/algolia-crawler-action?tab=readme-ov-file#readme)
- [Upload Release Action](https://github.com/cssnr/upload-release-action?tab=readme-ov-file#readme)
- [Check Build Action](https://github.com/cssnr/check-build-action?tab=readme-ov-file#readme)
- [Web Request Action](https://github.com/cssnr/web-request-action?tab=readme-ov-file#readme)
- [Get Commit Action](https://github.com/cssnr/get-commit-action?tab=readme-ov-file#readme)

<details><summary>❔ Unpublished Actions</summary>

These actions are not published on the Marketplace, but may be useful.

- [cssnr/create-files-action](https://github.com/cssnr/create-files-action?tab=readme-ov-file#readme) - Create various files from templates.
- [cssnr/draft-release-action](https://github.com/cssnr/draft-release-action?tab=readme-ov-file#readme) - Keep a draft release ready to publish.
- [cssnr/env-json-action](https://github.com/cssnr/env-json-action?tab=readme-ov-file#readme) - Convert env file to json or vice versa.
- [cssnr/push-artifacts-action](https://github.com/cssnr/push-artifacts-action?tab=readme-ov-file#readme) - Sync files to a remote host with rsync.
- [smashedr/update-release-notes-action](https://github.com/smashedr/update-release-notes-action?tab=readme-ov-file#readme) - Update release notes.
- [smashedr/combine-release-notes-action](https://github.com/smashedr/combine-release-notes-action?tab=readme-ov-file#readme) - Combine release notes.

---

</details>

<details><summary>📝 Template Actions</summary>

These are basic action templates that I use for creating new actions.

- [javascript-action](https://github.com/smashedr/javascript-action?tab=readme-ov-file#readme) - JavaScript
- [typescript-action](https://github.com/smashedr/typescript-action?tab=readme-ov-file#readme) - TypeScript
- [py-test-action](https://github.com/smashedr/py-test-action?tab=readme-ov-file#readme) - Dockerfile Python
- [test-action-uv](https://github.com/smashedr/test-action-uv?tab=readme-ov-file#readme) - Dockerfile Python UV
- [docker-test-action](https://github.com/smashedr/docker-test-action?tab=readme-ov-file#readme) - Docker Image Python

Note: The `docker-test-action` builds, runs and pushes images to [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

---

</details>

For a full list of current projects visit: [https://cssnr.github.io/](https://cssnr.github.io/)
