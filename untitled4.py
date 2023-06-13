import networkx as nx
import matplotlib.pyplot as plt

# Crear un nuevo grafo
taxonomia = nx.DiGraph()

# Agregar nodos (categorías o conceptos) a la taxonomía
taxonomia.add_node("Eukaryota")
taxonomia.add_node("Animalia")
taxonomia.add_node("Cnidaria")
taxonomia.add_node("Hydrozoa")
taxonomia.add_node("Sphonofora")
taxonomia.add_node("Physaliidae")
taxonomia.add_node("Felis")

# Establecer relaciones entre los nodos
taxonomia.add_edge("Animalia", "Chordata")
taxonomia.add_edge("Chordata", "Mammalia")
taxonomia.add_edge("Mammalia", "Carnivora")
taxonomia.add_edge("Carnivora", "Felidae")
taxonomia.add_edge("Felidae", "Felis")

# Visualizar la taxonomía
pos = nx.spring_layout(taxonomia)
nx.draw_networkx(taxonomia, pos=pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
plt.axis('off')
plt.show()