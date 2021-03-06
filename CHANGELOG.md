# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2019-07-04
### Added
- GeckoDriver Download Support. Check for geckodriver executable in current working directory. If unable to locate, then download the latest version from github.

## [1.2.0] - 2019-07-03
### Added
- Firebase Realtime Database Support. Tracking data will be pushed to the user's Realtime Database.
- Better Exception handling. 

## [1.1.1] - 2019-05-16
### Changed
- Explicit WebDriverWait from 12hrs to 24hrs. WhatsAppening will wait for 24hrs for the user to get Online before throwing a TimeoutException.

## [1.1.0] - 2019-05-15
### Added
- CSV Support. Tracking data will be written to a CSV file, 'WhatsAppening.csv'

## [1.0.0] - 2019-05-13
### Added
- Initial release.