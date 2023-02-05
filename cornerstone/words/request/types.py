import unicodedata

from choicesenum.schematics.types import ChoicesEnumType
from schematics import Model as SchematicModel
from schematics.types import StringType, ListType

from cornerstone.core.enums.order_by import OrderBy


class VowelCountRequestApiType(SchematicModel):
    words = ListType(StringType(), default=list)

    def run(self) -> dict[str, int]:
        self.validate()

        return {word: self._count_vowels(word) for word in self.words}

    @staticmethod
    def _count_vowels(word: str) -> int:
        vowels = 'AEIOU'

        # https://docs.python.org/3/library/unicodedata.html
        _word = unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8")

        return sum([_word.upper().count(char) for char in vowels])


class SortWordsRequestApiType(SchematicModel):
    words = ListType(StringType(), default=list)
    order = ChoicesEnumType(OrderBy)

    def run(self) -> list[str]:
        self.validate()
        self.words.sort(reverse=self.order.is_desc)
        return self.words
