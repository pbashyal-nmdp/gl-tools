Feature: Define Allele

    An **Allele** is a specific variation of a gene. Allele names are defined by the nomenclature of their gene system.

    For example, HLA alleles are described using [IMGT Nomenclature](http://hla.alleles.org/nomenclature/naming.html)

    Scenario Outline: Test Valid HLA Allele Names

        Given the allele name is <Allele>
        When I ask if it's an allele name
        Then the allele should be a <valid> allele name

        Examples: Valid Examples
            | Allele Name | Valid |
            | HLA-A*01:01 | True  |
            | DPBA*07:02  | True  |
            | 😄          | True  |
            | a1          | True  |

        Examples: Invalid Examples
            | Allele Name | Valid |
            | HLB/A*01:01 | False |
            | DPBA+07:02  | False |
