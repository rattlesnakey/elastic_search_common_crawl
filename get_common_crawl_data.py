from warcio import ArchiveIterator
import requests
import logging 
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] '
                           '- %(levelname)s: %(message)s',level=logging.INFO)
def get_wet_url(wet):
    return "https://commoncrawl.s3.amazonaws.com/{}".format(wet)
def get_records(wet_url):
    #wet_url = warc_url.replace('/warc/', '/wet/').replace('warc.gz', 'warc.wet.gz')#根据URL来进行替换的
    r = requests.get(wet_url, stream=True)
    records = ArchiveIterator(r.raw)
    record = next(records)
    #records的第一条是records的摘要信息
    assert record.rec_type == 'warcinfo'
    return records

def get_plain_text(records):
    record = next(records)
    header = dict(record.rec_headers.headers)
    language = header['WARC-Identified-Content-Language']
    target_url = header['WARC-Target-URI']
    #只含有英语
    if "," not in language and 'eng' in language:
        text = record.content_stream().read().decode('utf8')
        target_url = header['WARC-Target-URI']
        content_length = header['Content-Length']
        logging.info("target_url:{},text_length:{}".format(target_url,content_length))
        return text
    return "not-eng"
