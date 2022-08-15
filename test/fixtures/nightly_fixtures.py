import pytest

# Nightly fixtures
@pytest.fixture(scope="session")
def feature_smdebug_present():
    pass

@pytest.fixture(scope="session")
def feature_smddp_present():
    pass

@pytest.fixture(scope="session")
def feature_smmp_present():
    pass

@pytest.fixture(scope="session")
def feature_aws_framework_present():
    pass