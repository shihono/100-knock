# -*- coding : utf-8 -*-
from lxml import etree
import pydot


def make_dependency_graph(dep_edges, save_path='./data/sample.png'):
    # dep_edges : [(governor, dependent),(governor, dependent)]
    rg=pydot.graph_from_edges(dep_edges)
    rg.write_png(save_path,prog='dot')
    print("save into  {}".format(save_path))


def main():
    tree = etree.parse('./data/nlp_coref.txt.xml')
    dependency_edges = []
    for depend in tree.getroot().iterfind(".//document/sentences/sentence/dependencies"):
        sentence_dep_edge = []
        for dep in depend.iterfind(".//dep"):
            # ","を含めるとうまく graph_from_edgesできないので外す
            if dep.find("dependent").text.strip() != ",":
                sentence_dep_edge.append((dep.find("governor").text.strip(), dep.find("dependent").text.strip()))
        dependency_edges.append(sentence_dep_edge)
    # print(dependency_edges[:1])
    make_dependency_graph(list(set(dependency_edges[0])), "./data/dep_0.png")


if __name__ == '__main__':
    main()
