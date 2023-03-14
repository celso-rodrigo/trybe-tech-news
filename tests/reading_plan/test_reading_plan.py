# noqa: F401, E261, E501
from tech_news.analyzer.reading_plan import ReadingPlanService
from tests.assets.news import NEWS
from pytest import raises


def mock_find_news():
    return NEWS


def test_reading_plan_group_news(mocker):
    mocker.patch("tech_news.analyzer.reading_plan.find_news", mock_find_news)

    reading_plan = ReadingPlanService.group_news_for_available_time(6)

    assert len(reading_plan["readable"]) == 4
    assert len(reading_plan["unreadable"]) == 2

    with raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
