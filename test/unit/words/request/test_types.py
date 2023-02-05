import pytest

from cornerstone.words.request.types import VowelCountRequestApiType, SortWordsRequestApiType


@pytest.mark.parametrize('words, expected_result', [
    pytest.param(
        {"words": ["bátmãn", "róbin", "côringá"]}, {"bátmãn": 2, "róbin": 2, "côringá": 3},
        id="with diacritics"
    ),
    pytest.param(
        {"words": ["batman", "robin", "coringa"]}, {"batman": 2, "robin": 2, "coringa": 3},
        id="without diacritics"
    ),
    pytest.param(
        {"words": ["BATMAN", "ROBIN", "CORINGA"]}, {"BATMAN": 2, "ROBIN": 2, "CORINGA": 3},
        id="capitalized"
    ),
    pytest.param(
        {"words": ["QWRT"]}, {"QWRT": 0},
        id="without vowel"
    ),
])
def test_vowel_count_run(words, expected_result):
    # when
    vowel_count = VowelCountRequestApiType(words)

    # then
    result = vowel_count.run()
    assert result == expected_result


@pytest.mark.parametrize('words, expected_result', [
    pytest.param(
        {"words": ["batman", "robin", "coringa"], "order": "asc"}, ["batman", "coringa", "robin"],
        id="asc"
    ),
    pytest.param(
        {"words": ["batman", "robin", "coringa"], "order": "desc"}, ["robin", "coringa", "batman"],
        id="desc"
    ),
])
def test_sort_words_run(words, expected_result):
    # when
    sorted_words = SortWordsRequestApiType(words)

    # then
    result = sorted_words.run()
    assert result == expected_result
