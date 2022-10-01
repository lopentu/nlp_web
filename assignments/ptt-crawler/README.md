# **批踢踢爬蟲 ptt-crawler**
### 學術研究用途，請勿不當使用。


This project scrapes/crawls post content and comments from the website [PTT](https://term.ptt.cc/), and writes the scraped items to csv and json files. 


## **說明**
### 1. Installation

1. Python version
   * `python >= 3.9`

2. Clone repository

    ```bash
    git clone git@github.com:lopentu/nlp_web.git
    ```

3. Install Requirement
    ```bash
    cd nlp_web/assignments/ptt-crawler && pip install -r requirements.txt      
    ```
    

### 2. 使用方式

1. Commands
```
scrapy crawl ptt -a boards=BOARDS [-a scrap_all=BOOLEAN] 
            [-a index_from=NUMBER -a index_to=NUMBER]   
            [-a since=YEAR] [-a data_dir=PATH]
            [-a ip_cache=BOOLEAN]

positional arguments:
-a boards=BOARDS                          ptt board name (e.g. Soft_Job)
-a index_from=NUMBER -a index_to=NUMBER   html index number from a ptt board
-a scrap_all=BOOLEAN                      scrap all posts if true
-a since=YEAR                             scrap all posts from a given year
-a data_dir=PATH                          output file path (default: ./data)
-a ip_cache=BOOLEAN                       enable redis service to cache ip if true
```

> If you enable `ip_cache`, please make sure you have Redis on your local machine. Otherwise, you can use `docker-compose` to run the crawler.


* Crawl all the posts of a board:
  ```bash
  scrapy crawl ptt -a boards=Soft_Job -a scrap_all=True
  ```

* Crawl all the posts of a board from a year in the past:
  ```bash
  scrapy crawl ptt -a boards=Soft_Job -a since=2020
  ```

* Crawl the posts of a board based on html indexes:
  ```bash
  scrapy crawl ptt -a boards=Soft_Job -a index_from=1722 -a index_to=1723
  ```

  > Please make sure the number of `index_from` is greater than `index_to`.

* Crawl the posts of multiple boards. For example:
  ```bash
  scrapy crawl ptt -a boards=Soft_Job,Gossiping -a index_from=1722 -a index_to=1723
  ```

  >Note: the comma in the argument `boards` cannot have spaces. It cannot be `boards=Soft_Job, Baseball` or  `boards=["Soft_Job", "Baseball"]`.


2. The scraped data will be saved as csv and json files, and has the following format:

* csv

  | author |  alias |title | date | ip | city | country  | ups | downs | comments | url |
  |----|----|----|----|----|----|----|----|----|----|----|
  | Tesarus | 提姆休斯 | \[問卷\] 居家工作者睡眠研究	 | 2022-09-27 17:38:10 | 122.116.101.218 | New Taipei | Taiwan | 0 | 0 | 2	 | https://www.ptt.cc/bbs/Soft_Job/M.1664271492.A.42E.html |
  | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |


* json
  
  ```json
  {
    "board": "Soft_Job",
    "post_id": "M.1664271492.A.42E",
    "author": "Tesarus",
    "alias": "提姆休斯",
    "title": "[問卷] 居家工作者睡眠研究",
    "date": "2022-09-27 17:38:10",
    "ip": "122.116.101.218",
    "city": "New Taipei",
    "country": "Taiwan",
    "url": "https://www.ptt.cc/bbs/Soft_Job/M.1664271492.A.42E.html",
    "body": "大家好，...",
    "post_vote": { "ups": 0, "downs": 0, "comments": 2 },
    "comments": [
      {
        "type": "comments",
        "author": "keel90135",
        "content": "看標題以為是抓上班偷睡覺",
        "order": "1"
      },
      {
        "type": "comments",
        "author": "ainori520",
        "content": "我有認識幾個居家無工作者",
        "order": "2"
      }
    ]
  }
  ```


### 3. 使用 Docker
A Docker setup is provided for the crawler.

To run the crawler, go to the `docker-compose.yml` file to edit the command:

```yaml
version: "3"

services:
  scraptt:
    build: .
    environment:
      - PYTHON_ENV=production
    depends_on:
      - redis
    links:
      - redis

    # define your crawler here!
    command: bash -c "scrapy crawl ptt -a boards=Soft_Job,Gossiping -a index_from=1722 -a index_to=1723 -a ip_cache=True"
```
> Feel free to change the command as long as it follows the command format as stated above.

Now start the crawler:

```bash
docker-compose up
```

We suggest setting the argument `ip_cache` to `true` when you run the crawler via Docker. The reason is that the crawler will connect to Redis container, and there is no need for you to have Redis on your local machine. Most importantly, the performance of the crawler will be increased! 



## Contact
If you have any suggestion or question, please do not hesitate to email us at  shukai@gmail.com or philcoke35@gmail.com
