class Graph:

    def __init__(self, size):
        self.size = size  # Μέγεθος γράφου
        self.edges = []  # Για την αποθήκευση των ακμών (u, v, weight)
        self.vertex_data = [''] * size  # Για την αποθήκευση των κορυφών

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:  # Αν το u και το v είναι μη αρνητικό και μικρότερο του μεγέθους του γράφου
            self.edges.append((u, v, weight))  # Προσθέτουμε την ακμή

    def add_vertex_data(self, vertex, data):  # Όμοια συνάρτηση για την προσθήκη των κορυφών
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def find_parent(self, parent, i):  # Συνάρτηση εύρεσης κορυφής-γονέα
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):  # Βοηθητική συνάρτηση για την εύρεση κύκλων στο γράφημα
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):  # Συνάρτηση εφαρμογής του αλγορίθμου Kruskal
        result = []  # Ελάχιστο δένδρο ζεύξης
        i = 0  # Μετρητής ακμών
        total_weight = 0  # Συνολικό βάρος

        self.edges = sorted(self.edges, key=lambda item: item[2])  # Ταξινόμηση ακμών

        parent, rank = [], []

        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        while i < len(self.edges):
            u, v, weight = self.edges[i]  # Φροντίζουμε πάντοτε να επιλέγεται η επόμενη ακμή (για αυτό χρησιμοποιείται ο μετρητής και γίνεται ταξινόμηση)
            i += 1

            x = self.find_parent(parent, u)  # Έλεγχος ύπαρξης κύκλου
            y = self.find_parent(parent, v)
            if x != y:  # Αν δεν υπάρχει κύκλος προσθέτουμε στο αποτέλεσμα την ακμή και ενημερώνουμε το συνολικό βάρος
                result.append((u, v, weight))
                total_weight += weight
                self.union(parent, rank, x, y)

        print("Ακμή \tΒάρος")  # Εκτύπωση αποτελεσμάτων. Αρχικά σε επανάληψη τις ακμές του ελάχιστου δένδρου ζεύξης και στο τέλος το συνολικό βάρος
        for u, v, weight in result:
            print(f"{self.vertex_data[u]}-{self.vertex_data[v]} \t{weight}")
        print("Συνολικό βάρος: " + total_weight.__str__())


graph = Graph(9)  # Δημιουργία του γραφήματος της εκφώνησης
graph.add_vertex_data(0, '1')
graph.add_vertex_data(1, '2')
graph.add_vertex_data(2, '3')
graph.add_vertex_data(3, '4')
graph.add_vertex_data(4, '5')
graph.add_vertex_data(5, '6')
graph.add_vertex_data(6, '7')
graph.add_vertex_data(7, '8')

graph.add_edge(0, 1, 3)  # 1-2,  3
graph.add_edge(0, 2, 2)  # 1-3,  2
graph.add_edge(0, 3, 6)  # 1-4,  6
graph.add_edge(1, 3, 4)  # 2-4,  4
graph.add_edge(2, 3, 5)  # 3-4,  5
graph.add_edge(3, 4, 5)  # 4-5,  5
graph.add_edge(3, 5, 4)  # 4-6,  4
graph.add_edge(4, 5, 6)  # 5-6,  6
graph.add_edge(4, 6, 5)  # 5-7,  5
graph.add_edge(5, 6, 4)  # 6-7,  4
graph.add_edge(5, 7, 2)  # 6-8,  2
graph.add_edge(6, 7, 3)  # 7-8,  3

print("Ελάχιστο δένδρο ζεύξης:")
graph.kruskal()