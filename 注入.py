import sys
if sys.argv == ['']:
    import os
    import code
    def p(x):
        q = input(x)
        if q.strip() == '0x0':
            return '可可萝()'
        return q
    class 可可萝:
        def __repr__(self):
            return '可可萝'
    cprt = 'Type "help", "copyright", "credits" or "license" for more information.'
    banner = "Python %s on %s\n%s" % (sys.version, sys.platform, cprt)
    try:
        code.interact(readfunc=p, banner=banner, local={'可可萝': 可可萝}, exitmsg='')
    except SystemExit as e:
        if e.code:
            os._exit(e.code)
    os._exit(0)
