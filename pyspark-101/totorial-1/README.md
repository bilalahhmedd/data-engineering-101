## Remittance History Analysis using PySpark on EMR and Athena
Process and prepare raw transaction data by normalizing
the amounts involved to a standardized currency using API data of past
exchange rates


### Scope
to perform Spark Transformations on bank transactions using a real-time
currency ticker API and loading the processed data to Athena using Glue
Crawler.

### Data Description
Two sources of data
1. Exchange rates from api "Openexchangerates"
2. Static file of transactional data with following fields.

 &emsp; &emsp; ● Account_ID,<br />
 &emsp; &emsp; ● Value_date,<br />
 &emsp; &emsp; ● Transaction_details,<br />
 &emsp; &emsp; ● Withdrawal_amount,<br />
 &emsp; &emsp; ● Deposit_amount,<br />
 &emsp; &emsp; ● Currency,<br />
 &emsp; &emsp; ● Balance_amount<br />
  
### Tech Stack
Language: 	&emsp;	python <br />
Package:		&emsp;	 pyspark<br />
Services:		&emsp;	 ocker, Spark, AWS EMR, AWS S3, AWS Glue Crawler,<br />
						&emsp;&emsp; &emsp; &emsp;&emsp; AWS Athena, AWS EC2, Cron Job.
						
### Architecture

![alt text](https://github.com/bilalahhmedd/data-eng/blob/master/pyspark-101/totorial-1/resources/images/block_diagram_main.png?raw=true)

