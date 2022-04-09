def network_init():
    #Read network topology from network.txt, which has an adjacency matrix
    network_file = open("network.txt", "r"); #open network.txt
    network_file.read(); #read network.txt

    adjMat = [];

    for i in range(5):
        temp = []; #temporary matrix

        for j in range(5):
            line = network_file.readline();
            node = line.split("\t")
            row = [];
            temp.append(j);

        adjMat.append(temp);

    print(adjMat);

    network_file.close(); #close network.txt

network_init();
