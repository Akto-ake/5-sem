class Omnibus:
    omn_dict = {}
    
    def __setattr__(self, name, value):
        if name.startswith("_"):
            setattr(self, name, value)
        else:
            Omnibus.omn_dict.setdefault(name, set()).add(self)

    def __getattr__(self, name):
        if not name.startswith("_"):
            return len(Omnibus.omn_dict.get(name, 0))

    def __delattr__(self, name):
        if not name.startswith("_"):
            if name in Omnibus.omn_dict:
                if self in Omnibus.omn_dict[name]:
                    Omnibus.omn_dict[name].remove(self)
                    if not Omnibus.omn_dict.get(name):
                        del Omnibus.omn_dict[name]


import sys
exec(sys.stdin.read())