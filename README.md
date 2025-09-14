# Network Topology Visualizer

Network Topology Visualizer helps you map out and visualize complex networks using Python. It's designed for students and professionals who want to quickly see how devices connect in a network, highlight paths, and spot potential bottlenecks.

> "A picture is worth a thousand routers."

## Features

- **Build network graphs** from CSV or JSON input.
- Visualize nodes and links with customizable layouts.
- Calculate basic metrics like degree centrality and path lengths.
- Export diagrams as PNG or interactive HTML for presentations.

### Getting Started

1. Clone this repository.
2. Install the required packages: `pip install networkx matplotlib`.
3. Run the visualization script with your data file.


```

### Data Formats

You can provide network data in **CSV** (source,destination) or **JSON** formats. See the examples folder for templates.

---

### Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve features, documentation, or add support for additional file formats.

### License

This project is licensed under the MIT License.

![Network diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Computer_network_diagram.jpg/640px-Computer_network_diagram.jpg)

    import pandas as pd
    import networkx as nx
    import matplotlib.pyplot as plt

    edges = [('RouterA', 'Switch1'), ('Switch1', 'PC1'), ('Switch1', 'PC2')]
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()
