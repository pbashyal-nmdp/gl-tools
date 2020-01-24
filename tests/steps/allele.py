from gltools.allele import Allele, InvalidAlleleError
from hamcrest import assert_that, is_

@given('the allele name is {allele_name}')
def step_impl(context, allele_name):
    context.allele_name = allele_name

@when(u'I ask if it\'s an allele name')
def step_impl(context):
    try:
        context.allele = Allele(context.allele_name) 
        context.valid_allele = True
    except InvalidAlleleError:
        context.valid_allele = False

@then(u'the allele should be a {valid} allele name')
def step_impl(context, valid):
    assert_that(str(context.valid_allele),is_(valid))