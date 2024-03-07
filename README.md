# aws_services_crawler

This is a web crawler primarily powered by the **Selenium and BeautifulSoup (bs4)** Python packages.  
The crawler's task is **to crawl all AWS services** from the AWS official website and then write the data into a CSV file.  
The CSV file consists of four fields: service, category, URL, and description.  
- Service: The name of an AWS service, such as EC2, RDS, S3, etc.
- Category: The service's area group, as defined by AWS.
- URL: The official website of the service.
- Description: A brief introduction to the service.

Before executing the project, please ensure that **Python 3.8 or above, Selenium, and BeautifulSoup** have been installed on your computer.

***

這是一個主要由**Selenium和BeautifulSoup (bs4)** Python套件驅動的網路爬蟲。
該爬蟲的任務是從AWS官方網站**爬取所有AWS服務的資料**，然後將資料寫入一個CSV檔案。
CSV檔案包含四個欄位：服務、類別、URL和描述。

- 服務：AWS服務的名稱，例如EC2、RDS、S3等。
- 類別：服務的領域分組，由AWS定義。
- URL：服務的官方網站。
- 描述：對服務的簡短介紹。

在執行該項目之前，請確保您的電腦已**安裝Python 3.8或以上版本、Selenium和BeautifulSoup**。
