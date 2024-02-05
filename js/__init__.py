import pyjs.js as js


def __getattr__(attr):
    return js.__getattr__(attr)
