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
    }

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


    "something": {
        "requirements": {"flower": 1, "grass": 1},

        "position": [
            [["flower", None, None], [None, None, "grass"], [None, None, None]]
        ],

        "output": ("dirt", 1)
    }
}

