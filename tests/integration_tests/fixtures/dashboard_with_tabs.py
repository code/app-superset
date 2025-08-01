# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import json  # noqa: TID251

import pytest

from tests.integration_tests.dashboard_utils import create_dashboard
from tests.integration_tests.test_app import app

MULTIPLE_TABS_TBL_NAME = "multiple_tabs"


@pytest.fixture(scope="session")
def load_mutltiple_tabs_dashboard():
    position_json = {
        "CHART--0GPGmD-pO": {
            "children": [],
            "id": "CHART--0GPGmD-pO",
            "meta": {
                "chartId": 91,
                "height": 56,
                "sliceName": "Current Developers: Is this your first development job?",
                "sliceNameOverride": "Is this your first development job?",
                "uuid": "bfe5a8e6-146f-ef59-5e6c-13d519b236a8",
                "width": 2,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-l_9I0aNYZ",
                "ROW-b7USYEngT",
            ],
            "type": "CHART",
        },
        "CHART--w_Br1tPP3": {
            "children": [],
            "id": "CHART--w_Br1tPP3",
            "meta": {
                "chartId": 85,
                "height": 51,
                "sliceName": "\u2708\ufe0f Relocation ability",
                "uuid": "a6dd2d5a-2cdc-c8ec-f30c-85920f4f8a65",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW-DR80aHJA2c",
            ],
            "type": "CHART",
        },
        "CHART-0-zzTwBINh": {
            "children": [],
            "id": "CHART-0-zzTwBINh",
            "meta": {
                "chartId": 72,
                "height": 55,
                "sliceName": "Last Year Income Distribution",
                "uuid": "a2ec5256-94b4-43c4-b8c7-b83f70c5d4df",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-l_9I0aNYZ",
                "ROW-b7USYEngT",
            ],
            "type": "CHART",
        },
        "CHART-37fu7fO6Z0": {
            "children": [],
            "id": "CHART-37fu7fO6Z0",
            "meta": {
                "chartId": 93,
                "height": 69,
                "sliceName": "Degrees vs Income",
                "uuid": "02f546ae-1bf4-bd26-8bc2-14b9279c8a62",
                "width": 7,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-l_9I0aNYZ",
                "ROW-kNjtGVFpp",
            ],
            "type": "CHART",
        },
        "CHART-5QwNlSbXYU": {
            "children": [],
            "id": "CHART-5QwNlSbXYU",
            "meta": {
                "chartId": 90,
                "height": 69,
                "sliceName": "Commute Time",
                "uuid": "097c05c9-2dd2-481d-813d-d6c0c12b4a3d",
                "width": 5,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-l_9I0aNYZ",
                "ROW-kNjtGVFpp",
            ],
            "type": "CHART",
        },
        "CHART-FKuVqq4kaA": {
            "children": [],
            "id": "CHART-FKuVqq4kaA",
            "meta": {
                "chartId": 50,
                "height": 50,
                "sliceName": "Work Location Preference",
                "sliceNameOverride": "Work Location Preference",
                "uuid": "e6b09c28-98cf-785f-4caf-320fd4fca802",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW-DR80aHJA2c",
            ],
            "type": "CHART",
        },
        "CHART-JnpdZOhVer": {
            "children": [],
            "id": "CHART-JnpdZOhVer",
            "meta": {
                "chartId": 51,
                "height": 50,
                "sliceName": "Highest degree held",
                "uuid": "9f7d2b9c-6b3a-69f9-f03e-d3a141514639",
                "width": 2,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW--BIzjz9F0",
                "COLUMN-IEKAo_QJlz",
            ],
            "type": "CHART",
        },
        "CHART-LjfhrUkEef": {
            "children": [],
            "id": "CHART-LjfhrUkEef",
            "meta": {
                "chartId": 86,
                "height": 68,
                "sliceName": "First Time Developer & Commute Time",
                "uuid": "067c4a1e-ae03-4c0c-8e2a-d2c0f4bf43c3",
                "width": 5,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-l_9I0aNYZ",
                "ROW-s3l4os7YY",
            ],
            "type": "CHART",
        },
        "CHART-Q3pbwsH3id": {
            "children": [],
            "id": "CHART-Q3pbwsH3id",
            "meta": {
                "chartId": 79,
                "height": 50,
                "sliceName": "Are you an ethnic minority in your city?",
                "sliceNameOverride": "Minority Status (in their city)",
                "uuid": "def07750-b5c0-0b69-6228-cb2330916166",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-mOvr_xWm1",
            ],
            "type": "CHART",
        },
        "CHART-QVql08s5Bv": {
            "children": [],
            "id": "CHART-QVql08s5Bv",
            "meta": {
                "chartId": 92,
                "height": 56,
                "sliceName": "First Time Developer?",
                "uuid": "edc75073-8f33-4123-a28d-cd6dfb33cade",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-l_9I0aNYZ",
                "ROW-b7USYEngT",
            ],
            "type": "CHART",
        },
        "CHART-UtSaz4pfV6": {
            "children": [],
            "id": "CHART-UtSaz4pfV6",
            "meta": {
                "chartId": 59,
                "height": 50,
                "sliceName": "Age distribution of respondents",
                "uuid": "5f1ea868-604e-f69d-a241-5daa83ff33be",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-UsW-_RPAb",
                "COLUMN-OJ5spdMmNh",
            ],
            "type": "CHART",
        },
        "CHART-VvFbGxi3X_": {
            "children": [],
            "id": "CHART-VvFbGxi3X_",
            "meta": {
                "chartId": 41,
                "height": 62,
                "sliceName": "Top 15 Languages Spoken at Home",
                "uuid": "03a74c97-52fc-cf87-233c-d4275f8c550c",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-UsW-_RPAb",
                "COLUMN-OJ5spdMmNh",
            ],
            "type": "CHART",
        },
        "CHART-XHncHuS5pZ": {
            "children": [],
            "id": "CHART-XHncHuS5pZ",
            "meta": {
                "chartId": 78,
                "height": 41,
                "sliceName": "Number of Aspiring Developers",
                "sliceNameOverride": "What type of work would you prefer?",
                "uuid": "a0e5329f-224e-6fc8-efd2-d37d0f546ee8",
                "width": 2,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW-DR80aHJA2c",
            ],
            "type": "CHART",
        },
        "CHART-YSzS5GOOLf": {
            "children": [],
            "id": "CHART-YSzS5GOOLf",
            "meta": {
                "chartId": 49,
                "height": 54,
                "sliceName": "Ethnic Minority & Gender",
                "uuid": "4880e4f4-b701-4be0-86f3-e7e89432e83b",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-mOvr_xWm1",
            ],
            "type": "CHART",
        },
        "CHART-ZECnzPz8Bi": {
            "children": [],
            "id": "CHART-ZECnzPz8Bi",
            "meta": {
                "chartId": 70,
                "height": 74,
                "sliceName": "Location of Current Developers",
                "uuid": "5596e0f6-78a9-465d-8325-7139c794a06a",
                "width": 7,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-l_9I0aNYZ",
                "ROW-s3l4os7YY",
            ],
            "type": "CHART",
        },
        "CHART-aytwlT4GAq": {
            "children": [],
            "id": "CHART-aytwlT4GAq",
            "meta": {
                "chartId": 83,
                "height": 30,
                "sliceName": "Breakdown of Developer Type",
                "uuid": "b8386be8-f44e-6535-378c-2aa2ba461286",
                "width": 6,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-y-GwJPgxLr",
            ],
            "type": "CHART",
        },
        "CHART-fLpTSAHpAO": {
            "children": [],
            "id": "CHART-fLpTSAHpAO",
            "meta": {
                "chartId": 60,
                "height": 118,
                "sliceName": "Country of Citizenship",
                "uuid": "2ba66056-a756-d6a3-aaec-0c243fb7062e",
                "width": 9,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-UsW-_RPAb",
            ],
            "type": "CHART",
        },
        "CHART-lQVSAw0Or3": {
            "children": [],
            "id": "CHART-lQVSAw0Or3",
            "meta": {
                "chartId": 94,
                "height": 100,
                "sliceName": "How do you prefer to work?",
                "sliceNameOverride": "Preferred Employment Style vs Degree",
                "uuid": "cb8998ab-9f93-4f0f-4e4b-3bfe4b0dea9d",
                "width": 4,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW--BIzjz9F0",
            ],
            "type": "CHART",
        },
        "CHART-o-JPAWMZK-": {
            "children": [],
            "id": "CHART-o-JPAWMZK-",
            "meta": {
                "chartId": 69,
                "height": 50,
                "sliceName": "Gender",
                "uuid": "0f6b447c-828c-e71c-87ac-211bc412b214",
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-mOvr_xWm1",
            ],
            "type": "CHART",
        },
        "CHART-v22McUFMtx": {
            "children": [],
            "id": "CHART-v22McUFMtx",
            "meta": {
                "chartId": 71,
                "height": 52,
                "sliceName": "How much do you expect to earn? ($0 - 100k)",
                "sliceNameOverride": "\ud83d\udcb2Expected Income (excluding outliers)",
                "uuid": "6d0ceb30-2008-d19c-d285-cf77dc764433",
                "width": 4,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW--BIzjz9F0",
                "COLUMN-IEKAo_QJlz",
            ],
            "type": "CHART",
        },
        "CHART-wxWVtlajRF": {
            "children": [],
            "id": "CHART-wxWVtlajRF",
            "meta": {
                "chartId": 82,
                "height": 104,
                "sliceName": "Preferred Employment Style",
                "uuid": "bff88053-ccc4-92f2-d6f5-de83e950e8cd",
                "width": 4,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW--BIzjz9F0",
            ],
            "type": "CHART",
        },
        "COLUMN-IEKAo_QJlz": {
            "children": ["CHART-JnpdZOhVer", "CHART-v22McUFMtx"],
            "id": "COLUMN-IEKAo_QJlz",
            "meta": {"background": "BACKGROUND_TRANSPARENT", "width": 4},
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW--BIzjz9F0",
            ],
            "type": "COLUMN",
        },
        "COLUMN-OJ5spdMmNh": {
            "children": ["CHART-VvFbGxi3X_", "CHART-UtSaz4pfV6"],
            "id": "COLUMN-OJ5spdMmNh",
            "meta": {"background": "BACKGROUND_TRANSPARENT", "width": 3},
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-UsW-_RPAb",
            ],
            "type": "COLUMN",
        },
        "DASHBOARD_VERSION_KEY": "v2",
        "GRID_ID": {
            "children": ["TABS-L-d9eyOE-b"],
            "id": "GRID_ID",
            "parents": ["ROOT_ID"],
            "type": "GRID",
        },
        "HEADER_ID": {
            "id": "HEADER_ID",
            "meta": {"text": "FCC New Coder Survey 2018"},
            "type": "HEADER",
        },
        "MARKDOWN-BUmyHM2s0x": {
            "children": [],
            "id": "MARKDOWN-BUmyHM2s0x",
            "meta": {
                "code": "# Aspiring Developers\n\nThe mission of FreeCodeCamp is to \"help people learn to code for free\". With this in mind, it's no surprise that ~83% of this survey's respondents fall into the **Aspiring Developer** category.\n\nIn this tab, we use visualization to explore:\n\n- Interest in relocating for work\n- Preferences around work location & style\n- Distribution of expected income\n- Distribution of highest degree held\n- Heatmap of highest degree held vs employment style preference",  # noqa: E501
                "height": 50,
                "width": 4,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-YT6eNksV-",
                "ROW-DR80aHJA2c",
            ],
            "type": "MARKDOWN",
        },
        "MARKDOWN-NQmSPDOtpl": {
            "children": [],
            "id": "MARKDOWN-NQmSPDOtpl",
            "meta": {
                "code": "# Current Developers\n\nWhile majority of the students on FCC are Aspiring developers, there's a nontrivial minority that's there to continue leveling up their skills (17% of the survey respondents).\n\nBased on how respondents self-identified in the start of the survey, they were asked different questions. In this tab, we use visualizations to explore:\n\n- The buckets of commute team these developers encounter\n- The proportion of developers whose current job is their first developer job\n- Distribution of last year's income\n- The geographic distribution of these developers\n- The overlap between commute time and if their current job is their first developer job\n- Potential link between highest degree earned and last year's income",  # noqa: E501
                "height": 56,
                "width": 4,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-l_9I0aNYZ",
                "ROW-b7USYEngT",
            ],
            "type": "MARKDOWN",
        },
        "MARKDOWN-__u6CsUyfh": {
            "children": [],
            "id": "MARKDOWN-__u6CsUyfh",
            "meta": {
                "code": "## FreeCodeCamp New Coder Survey 2018\n\nEvery year, FCC surveys its user base (mostly budding software developers) to learn more about their interests, backgrounds, goals, job status, and socioeconomic features. This dashboard visualizes survey data from the 2018 survey.\n\n- [Survey link](https://freecodecamp.typeform.com/to/S3UeD9)\n- [Dataset](https://github.com/freeCodeCamp/2018-new-coder-survey)\n- [FCC Blog Post](https://www.freecodecamp.org/news/we-asked-20-000-people-who-they-are-and-how-theyre-learning-to-code-fff5d668969/)",  # noqa: E501
                "height": 30,
                "width": 6,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-y-GwJPgxLr",
            ],
            "type": "MARKDOWN",
        },
        "MARKDOWN-zc2mWxZeox": {
            "children": [],
            "id": "MARKDOWN-zc2mWxZeox",
            "meta": {
                "code": "# Demographics\n\nFreeCodeCamp is a completely-online community of people learning to code and consists of aspiring & current developers from all over the world. That doesn't necessarily mean that access to these types of opportunities are evenly distributed. \n\nThe following charts can begin to help us understand:\n\n- the original citizenship of the survey respondents\n- minority representation among both aspiring and current developers\n- their age distribution\n- household languages",  # noqa: E501
                "height": 52,
                "width": 3,
            },
            "parents": [
                "ROOT_ID",
                "GRID_ID",
                "TABS-L-d9eyOE-b",
                "TAB-AsMaxdYL_t",
                "ROW-mOvr_xWm1",
            ],
            "type": "MARKDOWN",
        },
        "ROOT_ID": {"children": ["GRID_ID"], "id": "ROOT_ID", "type": "ROOT"},
        "ROW--BIzjz9F0": {
            "children": ["COLUMN-IEKAo_QJlz", "CHART-lQVSAw0Or3", "CHART-wxWVtlajRF"],
            "id": "ROW--BIzjz9F0",
            "meta": {"background": "BACKGROUND_TRANSPARENT"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b", "TAB-YT6eNksV-"],
            "type": "ROW",
        },
        "ROW-DR80aHJA2c": {
            "children": [
                "MARKDOWN-BUmyHM2s0x",
                "CHART-XHncHuS5pZ",
                "CHART--w_Br1tPP3",
                "CHART-FKuVqq4kaA",
            ],
            "id": "ROW-DR80aHJA2c",
            "meta": {"background": "BACKGROUND_TRANSPARENT"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b", "TAB-YT6eNksV-"],
            "type": "ROW",
        },
        "ROW-UsW-_RPAb": {
            "children": ["COLUMN-OJ5spdMmNh", "CHART-fLpTSAHpAO"],
            "id": "ROW-UsW-_RPAb",
            "meta": {"background": "BACKGROUND_TRANSPARENT"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b", "TAB-AsMaxdYL_t"],
            "type": "ROW",
        },
        "ROW-b7USYEngT": {
            "children": [
                "MARKDOWN-NQmSPDOtpl",
                "CHART--0GPGmD-pO",
                "CHART-QVql08s5Bv",
                "CHART-0-zzTwBINh",
            ],
            "id": "ROW-b7USYEngT",
            "meta": {"background": "BACKGROUND_TRANSPARENT"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b", "TAB-l_9I0aNYZ"],
            "type": "ROW",
        },
        "ROW-kNjtGVFpp": {
            "children": ["CHART-5QwNlSbXYU", "CHART-37fu7fO6Z0"],
            "id": "ROW-kNjtGVFpp",
            "meta": {"background": "BACKGROUND_TRANSPARENT"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b", "TAB-l_9I0aNYZ"],
            "type": "ROW",
        },
        "ROW-mOvr_xWm1": {
            "children": [
                "MARKDOWN-zc2mWxZeox",
                "CHART-Q3pbwsH3id",
                "CHART-o-JPAWMZK-",
                "CHART-YSzS5GOOLf",
            ],
            "id": "ROW-mOvr_xWm1",
            "meta": {"background": "BACKGROUND_TRANSPARENT"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b", "TAB-AsMaxdYL_t"],
            "type": "ROW",
        },
        "ROW-s3l4os7YY": {
            "children": ["CHART-LjfhrUkEef", "CHART-ZECnzPz8Bi"],
            "id": "ROW-s3l4os7YY",
            "meta": {"background": "BACKGROUND_TRANSPARENT"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b", "TAB-l_9I0aNYZ"],
            "type": "ROW",
        },
        "ROW-y-GwJPgxLr": {
            "children": ["MARKDOWN-__u6CsUyfh", "CHART-aytwlT4GAq"],
            "id": "ROW-y-GwJPgxLr",
            "meta": {"background": "BACKGROUND_TRANSPARENT"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b", "TAB-AsMaxdYL_t"],
            "type": "ROW",
        },
        "TAB-AsMaxdYL_t": {
            "children": ["ROW-y-GwJPgxLr", "ROW-mOvr_xWm1", "ROW-UsW-_RPAb"],
            "id": "TAB-AsMaxdYL_t",
            "meta": {"text": "Overview"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b"],
            "type": "TAB",
        },
        "TAB-YT6eNksV-": {
            "children": ["ROW-DR80aHJA2c", "ROW--BIzjz9F0"],
            "id": "TAB-YT6eNksV-",
            "meta": {"text": "\ud83d\ude80 Aspiring Developers"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b"],
            "type": "TAB",
        },
        "TAB-l_9I0aNYZ": {
            "children": ["ROW-b7USYEngT", "ROW-kNjtGVFpp", "ROW-s3l4os7YY"],
            "id": "TAB-l_9I0aNYZ",
            "meta": {"text": "\ud83d\udcbb Current Developers"},
            "parents": ["ROOT_ID", "GRID_ID", "TABS-L-d9eyOE-b"],
            "type": "TAB",
        },
        "TABS-L-d9eyOE-b": {
            "children": ["TAB-AsMaxdYL_t", "TAB-YT6eNksV-", "TAB-l_9I0aNYZ"],
            "id": "TABS-L-d9eyOE-b",
            "meta": {},
            "parents": ["ROOT_ID", "GRID_ID"],
            "type": "TABS",
        },
    }

    with app.app_context():
        dash = create_dashboard(
            "multi_tabs_test", "multiple tabs Test", json.dumps(position_json), None
        )
    return dash
