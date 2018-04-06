# Making a new release

The following steps will create a new release:

1. Bump version in [setup.py](./setup.py)
2. Create a PR
3. Merge PR
4. Go to [GitHub release](https://github.com/freelancer/freelancer-sdk-python/releases/new)
5. Create a new tag pointing to the latest commit from `master` (the commit which bumped the version)
6. Add the release notes (as per existing ones)
7. Publish release
8. The above will trigger a new Travis CI build and deploy the new release to PyPi
