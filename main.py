from basic_operation import insert_data
from get_common_crawl_data import get_plain_text, get_wet_url, get_records
import logging 
import fire
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] '
                           '- %(levelname)s: %(message)s',level=logging.INFO)
def main(num):
    wet_files = open("available.paths","r")
    count_content = 0
    flag = 0
    for wet_file in wet_files:
        wet_file = wet_file.strip()
        wet_url = get_wet_url(wet_file)
        try:
            records = get_records(wet_url)
            while True:
                try:
                    text = get_plain_text(records)
                    if text == 'not-eng':
                        continue
                    else: 
                        count_content += 1
                        insert_data(count_content, text.replace("\n"," "))
                        logging.info("{} index has been created".format(count_content))
                    if count_content == num:
                        flag = 1
                        logging.info("{} indexes have been created!".format(num))
                        break
                except StopIteration as e:
                    logging.info("{} wet_url all done".format(wet_url))
                    break
            if flag:
                break
        except Exception:
            logging.info("{} has something wrong.".format(wet_file))
            continue              
if __name__ =='__main__':
    fire.Fire(main)
