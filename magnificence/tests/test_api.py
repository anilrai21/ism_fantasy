from django.test import TestCase
from ninja.testing import TestClient

from magnificence.api.views import router as app_router
from magnificence.services import populate_data


class AppTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        populate_data()

    def test_magnificent_team_api(self):
        client = TestClient(app_router)
        response = client.get("/magnificent-team")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [
                {
                    "element_type": {
                        "singular_name": "Goalkeeper",
                        "singular_name_short": "GKP",
                    },
                    "first_name": "Mark",
                    "second_name": "Flekken",
                    "team": {
                        "code": 94,
                        "name": "Brentford",
                        "short_name": "BRE",
                    },
                    "goals_scored": 0,
                    "assists": 0,
                    "goals_conceded": 15,
                    "penalties_saved": 0,
                    "penalties_missed": 0,
                    "saves": 42,
                },
                {
                    "element_type": {
                        "singular_name": "Defender",
                        "singular_name_short": "DEF",
                    },
                    "first_name": "Nathan",
                    "second_name": "Collins",
                    "team": {
                        "code": 94,
                        "name": "Brentford",
                        "short_name": "BRE",
                    },
                    "goals_scored": 1,
                    "assists": 3,
                    "goals_conceded": 15,
                    "penalties_saved": 0,
                    "penalties_missed": 0,
                    "saves": 0,
                },
                {
                    "element_type": {
                        "singular_name": "Defender",
                        "singular_name_short": "DEF",
                    },
                    "first_name": "Rayan",
                    "second_name": "Aït-Nouri",
                    "team": {"code": 39, "name": "Wolves", "short_name": "WOL"},
                    "goals_scored": 2,
                    "assists": 2,
                    "goals_conceded": 22,
                    "penalties_saved": 0,
                    "penalties_missed": 0,
                    "saves": 0,
                },
                {
                    "element_type": {
                        "singular_name": "Midfielder",
                        "singular_name_short": "MID",
                    },
                    "first_name": "Bukayo",
                    "second_name": "Saka",
                    "team": {"code": 3, "name": "Arsenal", "short_name": "ARS"},
                    "goals_scored": 2,
                    "assists": 7,
                    "goals_conceded": 5,
                    "penalties_saved": 0,
                    "penalties_missed": 0,
                    "saves": 0,
                },
                {
                    "element_type": {
                        "singular_name": "Midfielder",
                        "singular_name_short": "MID",
                    },
                    "first_name": "Cole",
                    "second_name": "Palmer",
                    "team": {"code": 8, "name": "Chelsea", "short_name": "CHE"},
                    "goals_scored": 6,
                    "assists": 5,
                    "goals_conceded": 10,
                    "penalties_saved": 0,
                    "penalties_missed": 0,
                    "saves": 0,
                },
                {
                    "element_type": {
                        "singular_name": "Midfielder",
                        "singular_name_short": "MID",
                    },
                    "first_name": "Mohamed",
                    "second_name": "Salah",
                    "team": {
                        "code": 14,
                        "name": "Liverpool",
                        "short_name": "LIV",
                    },
                    "goals_scored": 5,
                    "assists": 5,
                    "goals_conceded": 3,
                    "penalties_saved": 0,
                    "penalties_missed": 0,
                    "saves": 0,
                },
                {
                    "element_type": {
                        "singular_name": "Forward",
                        "singular_name_short": "FWD",
                    },
                    "first_name": "Erling",
                    "second_name": "Haaland",
                    "team": {
                        "code": 43,
                        "name": "Man City",
                        "short_name": "MCI",
                    },
                    "goals_scored": 10,
                    "assists": 0,
                    "goals_conceded": 9,
                    "penalties_saved": 0,
                    "penalties_missed": 0,
                    "saves": 0,
                },
            ],
        )
