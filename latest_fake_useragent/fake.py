import re

import requests
from fake_useragent import FakeUserAgent, FakeUserAgentError

from latest_fake_useragent.models import LatestVersions, LatestVersion


class LatestFakeUserAgent(FakeUserAgent):
    latest_versions = LatestVersions

    @staticmethod
    def get_major_version(full_version: str) -> str:
        major = ''
        for i, number in enumerate(full_version.split('.')):
            if i:
                major += '.0'

            else:
                major += number

        return major

    def get_latest_version(self, browser) -> LatestVersion:
        if browser not in LatestVersions.version_dict:
            raise FakeUserAgentError(f"Getting the latest version of this browser isn't supported!")

        latest_version = self.latest_versions.version_dict[browser]
        if latest_version.full:
            return latest_version

        if browser == 'chrome':
            response = requests.get(
                url='https://raw.githubusercontent.com/GoogleChromeLabs/chrome-for-testing/main/data/last-known-good-versions-with-downloads.json'
            )
            full = response.json()['channels']['Stable']['version']
            self.latest_versions.chrome.full = full
            self.latest_versions.chrome.major = self.get_major_version(full_version=full)

        elif browser == 'firefox':
            response = requests.get(url='https://product-details.mozilla.org/1.0/firefox_versions.json')
            full = response.json()['LATEST_FIREFOX_VERSION']
            self.latest_versions.firefox.full = full
            self.latest_versions.firefox.major = self.get_major_version(full_version=full)

        return self.get_latest_version(browser=browser)

    @property
    def chrome(self):
        browser = 'chrome'
        user_agent: str = self.__getattr__(browser)
        try:
            generated_version = re.findall(r'Chrome/[0-9A-Za-z.]+', user_agent)[0]

        except IndexError:
            generated_version = 'Chrome/'

        latest_version = self.get_latest_version(browser=browser)
        return user_agent.replace(generated_version, f'Chrome/{latest_version.full}')

    @property
    def firefox(self):
        browser = 'firefox'
        user_agent: str = self.__getattr__(browser)
        try:
            generated_version = re.findall(r'Firefox/[0-9A-Za-z.]+', user_agent)[0]

        except IndexError:
            try:
                generated_version = re.findall(r'Firefox [0-9A-Za-z.]+', user_agent)[0]

            except IndexError:
                generated_version = 'Firefox'

        latest_version = self.get_latest_version(browser=browser)
        return user_agent.replace(generated_version, f'Firefox/{latest_version.full}')


UserAgent = LatestFakeUserAgent
