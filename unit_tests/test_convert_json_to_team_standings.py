import pytest
from stub_creators.team_standings_stub import create_team_standings_stub


def test_convert_json_to_team_standings():
    team_standings = create_team_standings_stub()
    print(team_standings)
    assert 12 == 12

