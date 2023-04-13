
def command_format(d,s):
    l = (list(d.keys()))
    c = ""
    t = "{}='{}'"
    for i in l[1:]:
        b = "{}='{}'"
        b=b.format(i, d[i])
        c = c+ "," +b
    c = c[1:]
    t = t.format(l[0], d[l[0]])
    s = s.format(c,t)
    return s


def read_config(file='conf/config.json'):
    pass