# -*- coding : utf-8 -*-
from lxml import etree

def get_predicate_tuple(nsubj_list, dobj_list):
    predicates = list(set([nsubj[0] for nsubj in nsubj_list]) & set([dobj[0] for dobj in dobj_list]))
    #print(predicates)
    for predicate in predicates:
        subj = None
        obj = None
        for nsubj in nsubj_list:
            if nsubj[0]==predicate:
                subj = nsubj[1]
        for dobj in dobj_list:
            if dobj[0]==predicate:
                obj = dobj[1]
        if subj and obj:
            yield [subj,obj,predicate]


def main():
    tree = etree.parse('data/nlp_coref.txt.xml')
    dependency_triples = []
    for depend in tree.getroot().findall(".//dependencies[@type='collapsed-dependencies']"):
        nsubj_list = []
        dobj_list = []
        for dep in depend.findall(".//dep"):
            # nsubj,dobjを探す
            dep_type = dep.attrib.get('type')
            if "dobj" in dep_type:
                dobj_list.append([dep.find(".//governor").text, dep.find(".//dependent").text])
            elif "nsubj" in dep_type:
                nsubj_list.append([dep.find(".//governor").text, dep.find(".//dependent").text])
        # print("nsubj {}, dobj {}".format(len(nsubj_list),len(dobj_list)))
        dep_triple = [triple for triple in get_predicate_tuple(nsubj_list, dobj_list)]
        if len(dep_triple) > 0:
            dependency_triples.extend(dep_triple)
    print(dependency_triples[:50])


if __name__ == '__main__':
    main()