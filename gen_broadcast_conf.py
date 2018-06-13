import sys

LOCALHOST = "127.0.0.1"
BASEPORT = 5000
FILENAME = "broadcast.json"


def write_to_file(config):
    with open(FILENAME, 'wb') as f:
        f.write(config)


def gen_tty(i):
    pid = i*10
    res = []
    res.append("\t{}: {{".format(pid))
    res.append("\t\ttype: tty")
    res.append("\t\tbox: \"{}:{}\"".format(LOCALHOST, BASEPORT+i))
    res.append("\t\tattrs: {}")
    res.append("\t\troutes: {\n" + 
        "\t\t\t2: {}\n".format(pid+1) +
        "\t\t}"
        )
    res.append("\t}")
    return "\n".join(res)


def gen_id(i):
    pid = i*10+1
    res = []
    res.append("\t{}: {{".format(pid))
    res.append("\t\ttype: id")
    res.append("\t\tbox: \"{}:{}\"".format(LOCALHOST, BASEPORT+i))
    res.append("\t\tattrs: {\n" +
        "\t\t\tprefix: \"node{}: \"\n".format(i) +
        "\t\t}"
        )
    res.append("\t\troutes: {\n" + 
        "\t\t\t2: {}\n".format(pid+1) +
        "\t\t}"
        )
    res.append("\t}")
    return "\n".join(res)


def gen_broadcast(i, clusters):
    pid = i*10+2
    res = []
    clients = [str(c*10) for c in clusters if c != i]
    routes = ["{}:{}".format(c, c) for c in clients]
    res.append("\t{}: {{".format(pid))
    res.append("\t\ttype: broadcast")
    res.append("\t\tbox: \"{}:{}\"".format(LOCALHOST, BASEPORT+i))
    res.append("\t\tattrs: {\n" +
        "\t\t\tclients: [{}]\n".format(" ".join(clients)) +
        "\t\t}"
        )
    res.append("\t\troutes: {\n" + 
        "\t\t\t{}\n".format("\n\t\t\t".join(routes)) +
        "\t\t}"
        )
    res.append("\t}")
    return "\n".join(res)



def main(numClients):
    clusters = range(1, numClients+1)
    res = ['{']
    for i in clusters:
        res.append(gen_tty(i))
        res.append(gen_id(i))
        res.append(gen_broadcast(i, clusters))
    res.append('}')
    config = "\n".join(res)
    write_to_file(config)


if __name__== "__main__":
    numClients = int(sys.argv[1])
    main(numClients)


