import inventory
crafting_2x2_table = {
    "planks": {
        "requirements": {"wood": 1},
        "position": "any",
        "output": ("plank", 4),
    },

    "crafting_table": {
        "requirements": {"plank": 1},

        "position": [
            [["plank", "plank"],
            ["plank", "plank"]]

        ],
        "output": ("crafting_table", 1),
    },

    "something": {
        "requirements": {"flower": 1, "grass": 1},

        "position": [
            [["flower", None], [None, "grass"]]
        ],

        "output": ("dirt", 1)
    },

}


crafting_3x3_table = {
    "planks": {
        "requirements": {"wood": 1},
        "position": "any",
        "output": ("plank", 4),
    },

    "door": {
        "requirements": {"plank": 1},

        "position": [
    [
        ["plank", "plank", None],
        ["plank", "plank", None],
        ["plank", "plank", None]
    ],

    [
        [None, "plank", "plank"],
        [None, "plank", "plank"],
        [None, "plank", "plank"]
    ]

    ],
        "output": ("door", 3),
    },

    "crafting_table": {
        "requirements": {"plank": 1},

        "position": [
            [
                ["plank", "plank", None],
                ["plank", "plank", None],
                [None, None, None]
            ],
            [
                [None, None, None],
                ["plank", "plank", None],
                ["plank", "plank", None]
            ],
            [
                [None, "plank", "plank"],
                [None, "plank", "plank"],
                [None, None, None]
            ],
            [
                [None, None, None],
                [None, "plank", "plank"],
                [None, "plank", "plank"]
            ]


        ],
        "output": ("crafting_table", 1),
    },

    "pick": {
        "requirements": {"plank": 1},
        "position": [
            [["plank", "plank", "plank"],
            [None, None, None],
            [None, None, None]]
        ],
        "output": ("pick", 1)
    },
    "wood_pickaxe": {
            "requirements": {"plank": 1, "stick" : 1},
            "position": [
                [["plank", "plank", "plank"],
                [None, "stick", None],
                [None, "stick", None]]
            ],
            "output": ("wood_pickaxe", 1)
        },
    "stone_pickaxe": {
                "requirements": {"stone": 1, "stick" : 1},
                "position": [
                    [["stone", "stone", "stone"],
                    [None, "stick", None],
                    [None, "stick", None]]
                ],
                "output": ("stone_pickaxe", 1)
            },
    "iron_pickaxe": {
                    "requirements": {"iron": 1, "stick" : 1},
                    "position": [
                        [["iron", "iron", "iron"],
                        [None, "stick", None],
                        [None, "stick", None]]
                    ],
                    "output": ("iron_pickaxe", 1)
                },
    "diamond_pickaxe": {
                        "requirements": {"diamond": 1, "stick" : 1},
                        "position": [
                            [["diamond", "diamond", "diamond"],
                            [None, "stick", None],
                            [None, "stick", None]]
                        ],
                        "output": ("diamond_pickaxe", 1)
                    },

    "stick": {
        "requirements": {"plank" : 1},
        "position": [
            [["plank", None, None],
            ["plank", None, None],
            ["plank", None, None]],

            [
                [None, "plank", None],
                [None, "plank", None],
                [None, "plank", None]
            ],

            [
                [None, None, "plank"],
                [None, None, "plank"],
                [None, None, "plank"]
            ]

        ],
        "output" : ("stick", 4)
    },

    "something": {
        "requirements": {"flower": 1, "grass": 1},

        "position": [
            [["flower", None, None], [None, None, "grass"], [None, None, None]]
        ],

        "output": ("dirt", 1)
    }
}

