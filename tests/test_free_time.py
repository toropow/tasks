import pytest
from main import get_free_time


class TestFreeTime:
    @pytest.mark.parametrize(
        "busy, start_work, end_work, windows_size, expected_result",
        [
            [
                [{"start": "10:30", "stop": "10:50"}],
                "11:00",
                "12:00",
                "00:30",
                [{"start": "11:00", "stop": "11:30"}, {"start": "11:30", "stop": "12:00"}],
            ],
            [[{"start": "11:35", "stop": "11:45"}], "11:00", "12:00", "00:30", [{"start": "11:00", "stop": "11:30"}]],
            [[{"start": "10:30", "stop": "11:00"}], "11:00", "12:00", "00:30", [{"start": "11:30", "stop": "12:00"}]],
            [[{"start": "12:00", "stop": "12:05"}], "11:00", "12:00", "00:30", [{"start": "11:00", "stop": "11:30"}]],
            [[{"start": "11:10", "stop": "11:35"}], "11:00", "12:00", "00:20", [{"start": "11:40", "stop": "12:00"}]],
        ],
        ids=["No cross", "Cross inside", "Cross left border", "Cross right border", "Cross 2 range"],
    )
    def test_free_time(self, busy, start_work, end_work, windows_size, expected_result):
        assert (
            get_free_time(busy_time=busy, start=start_work, end=end_work, window_size=windows_size)
            == expected_result
        )
