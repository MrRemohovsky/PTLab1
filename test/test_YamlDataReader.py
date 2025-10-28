import pytest

from YamlDataReader import YamlDataReader
from src.Types import DataType


class TestYamlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = (
            "- Иванов Иван Иванович:\n"
            "    математика: 97\n"
            "    литература: 100\n"
            "    программирование: 91\n"
            "- Петров Петр Петрович:\n"
            "    математика: 78\n"
            "    химия: 87\n"
            "    социология: 61\n"
            "- Григорьев Анатолий Иванович:\n"
            "    математика: 37\n"
            "    литература: 100\n"
            "    программирование: 91\n"
            "- Григорьев Петр Петрович:\n"
            "    математика: 90\n"
            "    химия: 97\n"
            "    социология: 91\n"
        )
        data = {
            "Иванов Иван Иванович": [
                ("математика", 97),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ],
            "Григорьев Анатолий Иванович": [
                ("математика", 37),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Григорьев Петр Петрович": [
                ("математика", 90),
                ("химия", 97),
                ("социология", 91)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YamlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
