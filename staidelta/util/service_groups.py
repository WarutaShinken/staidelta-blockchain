from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "staidelta_harvester staidelta_timelord_launcher staidelta_timelord staidelta_farmer staidelta_full_node staidelta_wallet".split(),
    "node": "staidelta_full_node".split(),
    "harvester": "staidelta_harvester".split(),
    "farmer": "staidelta_harvester staidelta_farmer staidelta_full_node staidelta_wallet".split(),
    "farmer-no-wallet": "staidelta_harvester staidelta_farmer staidelta_full_node".split(),
    "farmer-only": "staidelta_farmer".split(),
    "timelord": "staidelta_timelord_launcher staidelta_timelord staidelta_full_node".split(),
    "timelord-only": "staidelta_timelord".split(),
    "timelord-launcher-only": "staidelta_timelord_launcher".split(),
    "wallet": "staidelta_wallet staidelta_full_node".split(),
    "wallet-only": "staidelta_wallet".split(),
    "introducer": "staidelta_introducer".split(),
    "simulator": "staidelta_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
