## Install

* pip install -r requirements.txt
* wget to download the edition of linux elasticsearch, the specific step could refer to the link below  
  * https://www.cnblogs.com/weibanggang/p/11589464.html
* in /elastic_search to  execute "export_environment.sh" to set java environment
* in /elastic_search/elasticsearch-7.10.1-linux-x86_64/elasticsearch-7.10.1 execute "bin/elasticsearch" to start the server 
* execute "curl http://localhost:9200" to check if you can see the "you know, for search" or you could execute "ss -tanl" to see 9200 port is listening

## Usage

* in /elastic_search execute "python main.py num", num means the indexes you want to build, for example, "python main.py 1000" means create 1000 indexes
*  after executing "python main.py 1000"，remember not to close 9200 port server
*  in /elastic_search excute 'python try_query.py bool "play basketball" 1' is to achieve the bool search of  'paly AND basketball' and show the content of the web, if you don't want to get the content back, just delete the "1"
* in /elastic_search execute 'python try_query.py precise "play basketball" 1' is to achieve the precise search of "play basketball"
* in /elastic_search execute 'python try_query.py neibor "play basketball" 1' is to achieve the neighbor search of "play basketball"



