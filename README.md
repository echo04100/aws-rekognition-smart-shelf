# AWS-rekogntion-smart-shelf
## how I use deeplens connect to the lambda and store picture in S3.
  本專題系統開發所使用的平台為AWS亞馬遜雲端平台(Amazon Web Service)，語言則是使用Python3.9來進行程式的撰寫，並且使用Boto3(適用於Python的AWS開發套件，可將Python程式、程式庫或是指令碼與AWS服務進行整合)裡的函式來做為驅動其他資源的接口，以下為本專題的系統架構圖，可以看到使用Lambda(即AWS Lambda，是亞馬遜雲端平台內的一種無伺服器運算服務)作為控制各項服務之間的觸發連結，並以S3 bucket作為照片的儲存位置，Amazon Rekognition(即SaaS之影像辨識服務，可透過自定Label進行自定義標籤辨識，目前進階到可以辨別出各類物品等級別)則是用來作為辨識由一開始DeepLens攝影機擷取之具有臉部特徵的照片。當今天顧客進入商店並進入攝影機拍攝範圍內，如果曾經來過且為女性，便會發送有關女性的廣告簡訊；如果為男性，便發送有關男性的廣告簡訊。下圖一則為本系統實作示意圖。
![flippers](https://yhc-website.s3.ap-northeast-1.amazonaws.com/images/aws_01.png) 
  
### 1.使用Deeplesns套用AWS的Templeate來偵測特定圖像
新增專案==>選擇Use a project template==>Face detection==>創立新專案

### 2.將偵測到的圖像儲存在S3
修改放在Deeplens放在Lambda裡的程式(greengrassHelloWorld.py)
可以參考我的程式碼[greengrassHelloWorld.py](https://github.com/echo04100/aws-rekognition-smart-shelf/blob/7496e1a095815b2977fc1eefc124d4ffac3ee549/deeplens-face-detection/greengrassHelloWorld.py)

### 3.透過Lambda來將S3裡的照片用rekognition來做辨識
創建一個新的Lambda程式，並使用S3做觸發，來讓照片一但被偵測到便可以做辨識

### 4.將辨識出來的結果用邏輯判斷，並依據判斷結果將結果發送至特定人的信箱
在同樣的Lambda程式裡做邏輯判斷，並串AWS SNS來將結果發送至特定信箱
可參考我的程式碼[lambda_handler.py](https://github.com/echo04100/aws-rekognition-smart-shelf/blob/087d61feb79b00b831a3b671c45ba4078046a401/lambda_handler.py)
