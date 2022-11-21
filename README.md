# AWS-rekogntion-smart-shelf
## how I use deeplens connect to the lambda and store picture in S3.
![flippers](https://yhc-website.s3.ap-northeast-1.amazonaws.com/images/image+1.png) 

### 1.使用Deeplesns套用AWS的Templeate來偵測特定圖像
新增專案==>選擇Use a project template==>Face detection==>創立新專案

### 2.將偵測到的圖像儲存在S3
修改放在Deeplens放在Lambda裡的程式(greengrassHelloWorld.py)
可以參考我的程式碼

### 3.透過Lambda來將S3裡的照片用rekognition來做辨識
創建一個新的Lambda程式，並使用S3做觸發，來讓照片一但被偵測到便可以做辨識

### 4.將辨識出來的結果用邏輯判斷，並依據判斷結果將結果發送至特定人的信箱
在同樣的Lambda程式裡做邏輯判斷，並串AWS SNS來將結果發送至特定信箱
可參考我的程式碼lambda_handler.py
