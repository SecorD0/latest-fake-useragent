from dataclasses import dataclass
from typing import Optional


@dataclass
class LatestVersion:
    full: str = ''
    major: str = ''


@dataclass
class LatestVersions:
    chrome: Optional[LatestVersion] = LatestVersion()
    firefox: Optional[LatestVersion] = LatestVersion()

    version_dict = {
        'chrome': chrome,
        'firefox': firefox
    }
