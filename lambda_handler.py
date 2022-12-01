import boto3
import json
import time
import dateutil.tz
import datetime

#辨識副程式
def face_recognition(bucket,fileName):
    Female=male=gender=count2=0
    fobject=['pen', 'glasses', 'doll']
    bobject=['car','plane','cup']
    client=boto3.client('rekognition')
    object02=client.detect_labels(
         Image={
            'S3Object': {
            'Bucket': bucket,
            'Name': fileName,
                        }
                    },
                    MaxLabels=5,
                    MinConfidence=0.9
                )
    
    tz = dateutil.tz.gettz('Asia/Taipei')
    timestr = datetime.datetime.now(tz).strftime("%Y/%m/%d/ %H:%M:%S")
    #偵測label跟發送SNS
    print("Time is: "+str(timestr)+"\n")
    #intersection = [x for x in object02['Labels'] for y in  bobject if x == y]
    #print(object02['Labels'][0:5])
    for aaa in object02['Labels']:
        print("此影像可能包含:"+aaa['Name'])
        print("===================")
        count2+=1
        if count2>5:
            break
        if aaa['Name']=="Female"and aaa['Name']=="girl":
            Female=1
        elif aaa['Name']=="man"and aaa['Name']=="boy":
            male=1
        else:
            print('you are moderate')
            gender=1
    sns_alert1=sns_alert(Female,male,gender)
    
#辨識是否來過
def detect_face(bucket,fileName,collection_id,threshold,maxFaces):
    client=boto3.client('rekognition')
    response=client.search_faces_by_image(CollectionId=collection_id,
                                Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)
    
    if len(response['FaceMatches']) == 1:
        faceid = response['FaceMatches'][0]['Face']['FaceId']
        print("=============$")
        print("faceid:"+faceid)
        print('Faces in collection ' + collection_id)
        print("you have been to visit this store")
        print("=============*")
        
    else:
        print("you haven't been to visit this store")
        response2=client.index_faces(CollectionId=collection_id,
                                Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                ExternalImageId=fileName,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])
        
    

#辨識label副程式
def label_detect(bucket,fileName):
    client=boto3.client('rekognition')
    client2 = boto3.client('sns')
    
    object02=client.detect_labels(
         Image={
            'S3Object': {
            'Bucket': bucket,
            'Name': fileName,
                        }
                    },
                    MaxLabels=5,
                    MinConfidence=0.9
                )
    
    tz = dateutil.tz.gettz('Asia/Taipei')
    timestr = datetime.datetime.now(tz).strftime("%Y/%m/%d/ %H:%M:%S")
    print("Time is: "+str(timestr)+"\n")
    for aaa in object02['Labels']:
        print("此影像可能包含:"+aaa['Name'])
        print("===================")
        
        
#辨識性別
def sns_alert(female,male,gender):
    client2 = boto3.client('sns')
    if female==1:
        print("you are girl")
        notification = "您好，基於您購買的商品，我們為您推薦：手帕。歡迎選購"
        response = client2.publish (
            TargetArn = "arn:aws:sns:us-east-1:411090889179:Girl",
            Message = json.dumps({'default': notification}),
            MessageStructure = 'json'
        )
    elif male==1:
        print("you are boy")
        notification = "您好，基於您購買的商品，我們為您推薦：鉛筆盒。歡迎選購"
        response = client2.publish (
            TargetArn = "arn:aws:sns:us-east-1:411090889179:Boys",
            Message = json.dumps({'default': notification}),
            MessageStructure = 'json'
        )
    elif gender==1:
        print("third gender")
        notification = "您好，基於您購買的商品，我們為您推薦：手帕,鉛筆盒。歡迎選購"
        response = client2.publish (
            TargetArn = "arn:aws:sns:us-east-1:411090889179:Third",
            Message = json.dumps({'default': notification}),
            MessageStructure = 'json'
        )
        
    
'''        
    notification = "您好，基於您購買的商品，我們為您推薦：手帕。歡迎選購"
                            response = client2.publish (
                                    TargetArn = "arn:aws:sns:us-east-1:411090889179:Boys",
                                    Message = json.dumps({'default': notification}),
                                    MessageStructure = 'json') '''

#主程式                            
def lambda_handler(event,context):
    
    tz = dateutil.tz.gettz('Asia/Taipei')
    timestr = datetime.datetime.now(tz).strftime("%Y/%m/%d/ %H:%M:%S")
    s3 = boto3.resource('s3')
    bucket ='deep-to-s3'
    collection_id ='echo01'
    fileName='photo'
    threshold = 70
    maxFaces=2
    
    
    for object in s3.Bucket(bucket).objects.all():
        detect_face001=detect_face(bucket,object.key,collection_id,threshold,maxFaces)
        indexed_faces_count = face_recognition(bucket,object.key)
        
    
    print("Time is: "+str(timestr)+"\n"+"Faces indexed count: "+str(indexed_faces_count))
    
    
    

if __name__ == "__main__":
    lambda_handler()

