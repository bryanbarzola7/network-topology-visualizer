#!/usr/bin/env python3
"""
Network Topology Visualizer

This script reads a network edge list from a CSV or JSON file and displays the network graph using networkx and matplotlib.
"""

import argparse
import json
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def load_graph(file_path: str) -> nx.Graph:
    """
    Load a graph from a CSV or JSON file. The CSV should have two columns representing the source and target of each edge.
    The JSON should be a list of dictionaries with 'source' and 'target' keys.
    """
    if file_path.lower().endswith('.csv'):
        df = pd.read_csv(file_path)
        if df.shape[1] < 2:
            raise ValueError("CSV must contain at least two columns representing source and target nodes.")
        edges = df.iloc[:, :2].values.tolist()
    elif file_path.lower().endswith('.json'):
        with open(file_path, 'r') as f:
            data = json.load(f)
        edges = [(item['source'], item['target']) for item in data]
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or JSON file.")
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def main():
    parser = argparse.ArgumentParser(description="Visualize network topology from a CSV or JSON file.")
    parser.add_argument("file", help="Path to the CSV or JSON file containing the edge list.")
    args = parser.parse_args()

    # Load graph and visualize
    graph = load_graph(args.file)
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, font_size=10)
    plt.title("Network Topology")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
