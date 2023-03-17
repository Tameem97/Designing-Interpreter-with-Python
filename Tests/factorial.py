['begin', 
        ['var', 'fact', 9],
        ['var', 'result', 1], 
            ['while', ['>=', 'fact', 1],
            ['begin', 
            ['set', 'result', ['*', 'result', 'fact']], 
            ['set', 'fact', ['-', 'fact', 1]],
            ]],
            'result']