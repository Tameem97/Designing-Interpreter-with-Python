['begin', 
        ['def', 'square', ["callback"], ["begin", 
                                        ["var", "x", 10], 
                                        ["var", "y", 20],
                                        ["callback", ["+", "x", "y"]]]],
        ["square", ["lambda", ["data"], ["*", "data", 10]]]]