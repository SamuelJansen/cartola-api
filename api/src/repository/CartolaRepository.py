from python_helper import Constant as c
from python_helper import ObjectHelper, FileHelper, StringHelper, EnvironmentHelper, log
from python_framework import Repository


def overrideFileLines(filePath: str, lines: list, encoding: str = c.UTF_8):
    try:
        with open(filePath, c.OVERRIDE, encoding=encoding) as writer:
            writer.writelines(lines)
    except Exception as exception:
        log.error(overrideFileLines, f'Not possible to override lines of {filePath}', exception, muteStackTrace=True)
        raise exception

FileHelper.overrideFileLines


@Repository(model = dict)
class CartolaRepository:

    def saveAll(self, jsonResponseDictionary):
        for key, jr in jsonResponseDictionary.items():
            FileHelper.overrideFileLines(
                f'api{EnvironmentHelper.OS_SEPARATOR}src{EnvironmentHelper.OS_SEPARATOR}static{EnvironmentHelper.OS_SEPARATOR}files{EnvironmentHelper.OS_SEPARATOR}{key}{c.DOT}json',
                StringHelper.prettyJson(jr).split(c.NEW_LINE)
            )
