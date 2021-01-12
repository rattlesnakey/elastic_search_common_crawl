from elasticsearch import Elasticsearch
from basic_operation import insert_data, search_by_bool_method, search_by_neibor_method,search_by_precise_method,search_by_subtle_method
import fire 
es = Elasticsearch(timeout=30)
if __name__ =="__main__":
    #fire会把函数return的结果返回
    fire.Fire({
        # "return_all":return_all_indexes,
        "bool":search_by_bool_method,
        "precise":search_by_precise_method,
        "subtle":search_by_subtle_method,
        "neibor":search_by_neibor_method
    })