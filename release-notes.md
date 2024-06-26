# Release Notes

## Latest Changes

* ✨ Initialize project. PR [#17](https://github.com/khulnasoft/readyapi-cli/pull/17) by [@gitworkflows](https://github.com/gitworkflows).

### Refactors

* ♻️ Simplify code in `src/readyapi_cli/discover.py`. PR [#22](https://github.com/khulnasoft/readyapi-cli/pull/22) by [@pedroimpulcetto](https://github.com/pedroimpulcetto).

### Internal

* ⬆ Bump ruff from 0.4.3 to 0.4.4. PR [#23](https://github.com/khulnasoft/readyapi-cli/pull/23) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Enable CI tests for Python 3.12. PR [#27](https://github.com/khulnasoft/readyapi-cli/pull/27) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update Upload/Download artifacts GitHub Actions. PR [#26](https://github.com/khulnasoft/readyapi-cli/pull/26) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.4

### Fixes

* 🔧 Make ReadyAPI and Uvicorn optional dependencies, to avoid circular dependencies. PR [#25](https://github.com/khulnasoft/readyapi-cli/pull/25) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* ⬆ Bump actions/cache from 3 to 4. PR [#5](https://github.com/khulnasoft/readyapi-cli/pull/5) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pypa/gh-action-pypi-publish from 1.8.11 to 1.8.14. PR [#2](https://github.com/khulnasoft/readyapi-cli/pull/2) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.0.3

### Features

* ✨ Add optional `--workers` CLI option, and fix CI for test-redistribute. PR [#12](https://github.com/khulnasoft/readyapi-cli/pull/12) by [@PokkaKiyo](https://github.com/PokkaKiyo).

### Upgrades

* ➖ Relax Uvicorn pin. PR [#16](https://github.com/khulnasoft/readyapi-cli/pull/16) by [@khulnasoft](https://github.com/khulnasoft).

### Docs

* 📝 Add note about Uvicorn as the high-performance server running underneath. PR [#9](https://github.com/khulnasoft/readyapi-cli/pull/9) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* ⬆ Bump ruff from 0.2.0 to 0.4.3. PR [#14](https://github.com/khulnasoft/readyapi-cli/pull/14) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pytest requirement from <8.0.0,>=4.4.0 to >=4.4.0,<9.0.0. PR [#4](https://github.com/khulnasoft/readyapi-cli/pull/4) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mypy from 1.4.1 to 1.10.0. PR [#7](https://github.com/khulnasoft/readyapi-cli/pull/7) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.0.2

First public working version. 🚀

### Fixes

* 👷 Tweak CI testing and fix import error detection for Python 3.8. PR [#8](https://github.com/khulnasoft/readyapi-cli/pull/8) by [@khulnasoft](https://github.com/khulnasoft).
