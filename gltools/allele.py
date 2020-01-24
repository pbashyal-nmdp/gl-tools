import re
from typing import List, Any

class Allele(object):
    invalid_allele_chars_regex: str = r'[|+~/^]'

    def __init__(self, allele_name: str):
       self.name = allele_name
       if not self._is_valid():
           raise InvalidAlleleError(allele_name, "Allele contains GL String delimiter character")

    def _is_valid(self):
        """
        If GL String delimiters are found, it's an invalid allele name
        :return: True or False to indicate if the allele is valid
        """
        found_invalid_chars: List[Any] = re.findall(Allele.invalid_allele_chars_regex, self.name)
        # If no invalid chars in allele, it's a valid allele
        return not found_invalid_chars
        

class InvalidAlleleError(Exception):
    pass
