#Generates an nodes.json file to map placeholders to actual IPs

SOURCE = "/etc/hosts"
FILENAME = "nodes.json"


def write_to_file(nodes):
    """Writes config string to FILENAME.json in current working directory"""
    with open(FILENAME, 'wb') as f:
        f.write(nodes)


def main(numClients):
    """Generates the nodes.json file for the current experiment network"""
    res = ['{']
    i = 0
    with open(SOURCE, 'r') as f:
        l = f.readline()
        while l:
            if "node" in l:  #ignore localhost, for instance
                ip = l.split(1)[0]
                res.append("\t@node{}: {}".format(i, ip))
                i += 1
            l = f.readline()
    res.append('}')
    write_to_file('\n'.join(res))


if __name__== "__main__":
    main()

