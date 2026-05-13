import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._nodes = DAO.getNodes()
        self._mappa = {}
        for n in self._nodes:
            self._mappa[n.CCode] = n

    def buildGraph(self, anno):
        self._grafo.clear()
        for n in DAO.getNodes2(anno):
            c = self._mappa[n[0]]
            self._grafo.add_node(c)

        self.addEdges(anno)

    def addEdges(self, anno):
        archi = DAO.getEdges(anno)      #tupla
        for elem in archi:
            stato1 = self._mappa[elem[0]]
            stato2 = self._mappa[elem[1]]
            self._grafo.add_edge(stato1, stato2)

    def getComponentiConn(self):
        return nx.number_connected_components(self._grafo)


