# AWS-rekogntion-smart-shelf
## how I use deeplens connect to the lambda and store picture in S3.
  當本研究中所使用的DeepLens攝影機一旦偵測到有人時，即會啟動人臉辨識系統，此辨識系統可以辨識性別為男性或女性，或是穿著打扮、心情狀態…等標籤，將每位顧客的來訪做紀錄，透過網路傳輸，會先經由AWS Lambda來進行偵測並擷取具有臉部特徵的影像，再來則會將擷取到的臉部照片放到S3內儲存，同時將S3作為觸發Lambda的媒介，一旦有照片輸入，Lambda便會開始執行程式。因此，使用這些照片能同時觸發AWS Lambda並使用AWS Rekognition做辨識，接下來將這些資料以無記名式的方式來為每位顧客都設置一個不重複的編號標籤(FaceId)，並將已辨認且加上標籤後的結果儲存。
當下次有顧客造訪時，則透過下述的系統運作流程來對拍攝到的臉部照片進行辨識，如果辨識此顧客為第一次造訪，則將其照片進行標籤並儲存；如果辨識結果為此顧客曾經造訪過，也就是資料庫中已有此人的標籤化資料時，則會觸發AWS連結至Firebase的程式並以簡訊的方式依照男性或女性進行推播顧客商品之廣告訊息。

![flippers](https://yhc-website.s3.ap-northeast-1.amazonaws.com/images/aws_01.png) 
## 步驟說明
### 1.使用Deeplesns套用AWS的Templeate來偵測特定圖像
新增專案==>選擇Use a project template==>Face detection==>創立新專案

### 2.將偵測到的圖像儲存在S3
修改放在Deeplens放在Lambda裡的程式(greengrassHelloWorld.py)
可以參考我的程式碼[greengrassHelloWorld.py](https://github.com/echo04100/aws-rekognition-smart-shelf/blob/7496e1a095815b2977fc1eefc124d4ffac3ee549/deeplens-face-detection/greengrassHelloWorld.py)

### 3.透過Lambda來將S3裡的照片用rekognition來做辨識
創建一個新的Lambda程式，並使用S3做觸發，來讓照片一但被偵測到便可以做辨識

### 4.將辨識出來的結果用邏輯判斷，並依據判斷結果將結果發送至特定人的手機App上
在同樣的Lambda程式裡做邏輯判斷，並串AWS SNS來將結果發送至特定手機上
可參考我的程式碼[lambda_handler.py](https://github.com/echo04100/aws-rekognition-smart-shelf/blob/087d61feb79b00b831a3b671c45ba4078046a401/lambda_handler.py)
