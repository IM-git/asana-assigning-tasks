from enum import Enum


class AsanaData(Enum):

    TEAM = '1202795154711346'
    WORKSPACE = '1202795154711344'
    PROJECTS = {
        'Plan IM test': {
            'gid': '1202795250106664',
            'sections': {
                'TC': '1202795250106667',
                'Complite_im': '1202795250106668'
            },
            'branches': []
        },
        'Programming': {
            'gid': '1204208718664599',
            'sections': {
                'In progress': '1204208718664604'
            },
            'branches': ['dev/match3', 'dev/events', 'dev/utils', 'dev/room_design']
        },
        'VSO': {
            'gid': '1204208718664606',
            'sections': {
                'In progress': '1204208718664611'
            },
            'branches': ['vso/match3', 'vso/room_design']
        },
        'VFX': {
            'gid': '1204208718664613',
            'sections': {
                'In progress': '1204208719439037'
            },
            'branches': ['vfx/match3', 'vfx/room_design']
        }
    }
    PROJECTS_GID = {
        'Plan IM test': '1202795250106664',
        'Programming': '1204208718664599',
        'VSO': '1204208718664606',
        'VFX': '1204208718664613'
    }
    PROJECTS_SECTIONS = {
        'Plan IM test': {
            'TC': '1202795250106667',
            'Complite_im': '1202795250106668'
        },
        'Programming': {
            'In progress': '1204208718664604',
        },
        'VSO': {
            'In progress': '1204208718664611',
        },
        'VFX': {
            'In progress': '1204208719439037',
        }
    }
    DICT_PROJECTS_BRANCHES = {
        'Programming': ['dev/match3', 'dev/events', 'dev/utils', 'dev/room_design'],
        'VSO': ['vso/match3', 'vso/room_design'],
        'VFX': ['vfx/match3', 'vfx/room_design']
    }
    PROJECT_GID = '1202879111319679'
    SECTION_GID = '1202879111319684'
    TASK_GID = '1204208460071853'
    STORY_GID = '1203171330497940'
