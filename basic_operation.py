from elasticsearch import Elasticsearch
es = Elasticsearch(timeout=30)
# 插入数据
def insert_data(id_num, web_content):
    # 默认host为localhost,port为9200.但也可以指定host与port
    es.index(index="def-gen", doc_type="test_type", id=id_num, body={"content": web_content})
# def return_all_indexes(show = 0):
#     query_result = es.search(index="def-gen", body={"query":{"match_all":{}}})
#     print("result_num:{}".format(len(query_result)))
#     if show == 1:
#         print("result:\n",query_result)
# return query_result

def search_by_subtle_method(query,show = 0):
    query_result = es.search(index = "def-gen", body = {"query":{"wildcard":{"content":query}}})
    print("result_num:{}".format(len(query_result['hits']['hits'])))
    if show == 1:
        print("result:\n",query_result['hits']['hits'])
    # return query_result['hits']['hits']

def search_by_precise_method(query,show = 0):
    query_result = es.search(index = "def-gen", body = {"query":{"match_phrase":{"content":query}}})
    print("result_num:{}".format(len(query_result['hits']['hits'])))
    if show == 1:
        print("result:\n",query_result['hits']['hits'])
    # return query_result['hits']['hits']

def search_by_bool_method(query,show = 0):
    #一个词
    if " " not in query:
        query_result = es.search(index = "def-gen", body = {"query":{"bool":{"should":[{'match':{'content':query}}]}}})
    else:
        query_word_list = query.split(" ")
        print(query_word_list)
        query_bool_list = [{"match":{"content":word}}for word in query_word_list]
        query_result = es.search(index = "def-gen", body = {"query":{"bool":{"should":query_bool_list}}})
    print("result_num:{}".format(len(query_result['hits']['hits'])))
    if show == 1:
        print("result:\n",query_result['hits']['hits'])
    # return query_result['hits']['hits']

#近邻查询
def search_by_neibor_method(query,show = 0):
    query_result = es.search(index = "def-gen", body = {"query":{"multi_match":{"query":query,"slop":1}}})
    print("result_num:{}".format(len(query_result['hits']['hits'])))
    if show == 1:
        print("result:\n",query_result['hits']['hits'])
    # return query_result['hits']['hits']
    #es.create(index="def-gen",doc_type="test_type",id=id_num,ignore=[400,409],body={"name":"python","addr":'四川省'}, timeout = 30)
    #    query_result = es.search(index = "def-gen", body = {"query":{"bool":{"should":[{"match":{"content":"hold"}},{"match":{"content":"cheap"}}]}}})