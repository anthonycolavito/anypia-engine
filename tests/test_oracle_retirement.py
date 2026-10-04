"""MILESTONE test: every retire_v1 golden must match penny-exact."""

import pytest

from anypia_engine import compute
from tests.oracle_util import assert_case_matches, load_sweep, worker_from_spec

SWEEP = load_sweep("retire_v1")


@pytest.mark.oracle
@pytest.mark.parametrize(
    "spec,expected", SWEEP, ids=[s["case_id"] for s, _ in SWEEP]
)
def test_retirement_case(spec: dict, expected: dict) -> None:
    assert "error" not in expected, "oracle rejected this case"
    r = compute(worker_from_spec(spec))
    assert_case_matches(r, expected)
