# AWS-rekogntion-smart-shelf
## how I use deeplens connect to the lambda and store picture in S3.
| ![flippers](https://yhc-website.s3.ap-northeast-1.amazonaws.com/images/image+1.png) |
*1.使用deeplesns套用AWS的Templeate來偵測特定圖像
Firstly, I use deeplens model which AWS have already provided in deeplens services.It can help us to capture the pciture we need.|
AWS provid some template project that we don't really need to just click 
2.將偵測到的圖像儲存在S3
3.透過Lambda來將S3裡的照片用rekognition來做辨識
4.將辨識出來的結果用邏輯判斷，並依據判斷結果將結果發送至特定人的信箱
