class Dict(dict):


    def __init__(self, names=(), values=(), **kwargs):
        super().__init__(**kwargs)
        for key, value in zip(names, values):
            self[key] = value

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('attribute {} not exist'.format(item))

    def __setattr__(self, key, value):
        self[key] = value