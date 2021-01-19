diuretic = {
    'efficiency': 'diuretic',
    'animal': 'Тварина',
    'count_animals': 7,
    'decimal_point': 1,
    'type': float,
    'control': {
        'name': 'Контроль',
        'minimum': 1.0,
        'maximum': 1.8,
    },
    'references': {
        'reference1': {
            'name': 'Фуросемід',
            'minimum': 3.5,
            'maximum': 4.4,
            'min_percentage_efficiency': 269,
            'max_percentage_efficiency': 287,
        },
        'reference2': {
            'name': 'Гіпотіазид',
            'minimum': 2.0,
            'maximum': 3.0,
            'min_percentage_efficiency': 162,
            'max_percentage_efficiency': 170,
        }
    },
    'specimens': {
        'specimens_positive1': {
            'name': 'Зразок+',
            'minimum': 2.5,
            'maximum': 3.4,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'specimens_positive2': {
            'name': 'Зразок+:',
            'minimum': 4.5,
            'maximum': 5.4,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'specimens_negative1': {
            'name': 'Зразок-',
            'minimum': 0.4,
            'maximum': 1.5,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'specimens_negative2': {
            'name': 'Зразок-:',
            'minimum': 0.4,
            'maximum': 2.5,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'specimens_inert': {
            'name': 'Зразок',
            'minimum': 0.9,
            'maximum': 2.5,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        }
    },

    'timeline': {
        'timeline0': {
            'name' : 'дві години'},
        'timeline1': {
            'name': 'чотири години',
            'control': {
                'name': 'Контроль',
                'minimum': +0.4,
                'maximum': +0.9,
            },
            'references': {
                'reference1': {
                    'name': 'Фуросемід',
                    'minimum': +1.5,
                    'maximum': +2.6,
                    'min_percentage_efficiency': None,
                    'max_percentage_efficiency': None,
                },
                'reference2': {
                    'name': 'Гіпотіазид',
                    'minimum': +0.8,
                    'maximum': +1.4,
                    'min_percentage_efficiency': None,
                    'max_percentage_efficiency': None,
                },
            },
            'specimens': {
                'specimens_positive1': {
                    'name':'Зразок+:',
                    'minimum': +2.0,
                    'maximum': +2.5,
                    'min_percentage_efficiency': None,
                    'max_percentage_efficiency': None,
                },
                'specimens_positive2': {
                    'name': 'Зразок+:',
                    'minimum': +1.5,
                    'maximum': +2.0,
                    'min_percentage_efficiency': None,
                    'max_percentage_efficiency': None,
                },
                'specimens_negative1': {
                    'name': 'Зразок-',
                    'minimum': +0.5,
                    'maximum': +1.4,
                    'min_percentage_efficiency': None,
                    'max_percentage_efficiency': None,
                },
                'specimens_negative2': {
                    'name': 'Зразок-:',
                    'minimum': +0.5,
                    'maximum': +1.4,
                    'min_percentage_efficiency': None,
                    'max_percentage_efficiency': None,
                },
                'specimens_inert': {
                    'name': 'Зразок',
                    'minimum': +0.4,
                    'maximum': +0.9,
                    'min_percentage_efficiency': None,
                    'max_percentage_efficiency': None,
                }
            }
        }
    }
}


diuretic_four = {
    'efficiency': 'diuretic',
    'animal': 'Тварина',
    'count_animals': 7,
    'decimal_point': 1,
    'type': float,
    'control': {
        'name': 'Контроль',
        'minimum': +0.4,
        'maximum': +0.9,
    },
    'references': {
        'reference1': {
            'name': 'Фуросемід',
            'minimum': +1.5,
            'maximum': +2.6,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'reference2': {
            'name': 'Гіпотіазид',
            'minimum': +0.8,
            'maximum': +1.4,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        }
    },
    'specimens': {
        'specimens_positive1': {
            'name': 'Зразок+',
            'minimum': +2,
            'maximum': +2.5,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'specimens_positive2': {
            'name': 'Зразок+:',
            'minimum': +1.5,
            'maximum': +2,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'specimens_negative1': {
            'name': 'Зразок-',
            'minimum': +0.5,
            'maximum': +1.4,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'specimens_negative2': {
            'name': 'Зразок-:',
            'minimum': +0.4,
            'maximum': +0.9,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        },
        'specimens_inert': {
            'name': 'Зразок',
            'minimum': +0.2,
            'maximum': +0.5,
            'min_percentage_efficiency': None,
            'max_percentage_efficiency': None,
        }
    }
}