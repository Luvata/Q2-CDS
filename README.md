# Q2-CDS
Write up Q2 CDS

## Traffic signs classifier 

Data set lay 1 phan tu [Belgium Traffic sign dataset](http://btsd.ethz.ch/shareddata/)
[Training](http://btsd.ethz.ch/shareddata/BelgiumTSC/BelgiumTSC_Training.zip)

Em lam theo huong dan trong bai [nay](https://hackernoon.com/creating-insanely-fast-image-classifiers-with-mobilenet-in-tensorflow-f030ce0a2991), su dung api image-retraining cua Tensorflow voi model la mobile net v1

[source tensorflow](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/image_retraining)

folder data gom co 4 sub folder :
 - canh_bao 
 - duong_1_chieu
 - giao_lo
 - stop
 - file labels.txt chua ten cac folder
Theo data tu BTSD : tat ca anh la dinh dang .ppm, Converter.py de chuyen anh trong folder sang .jpg
## prerequisite
 - Python 3
 - Tensorflow 1.3
 - [optional] Cuda & Cudnn ( giup training nhanh hon )
 
## Cac buoc hoan thanh
 1. override folder data den 
 ```
  /tensorflow/examples/image_retraining
 ```
 2. terminal : ~/tensorflow/examples/image_retraining :
 ```
 python retrain.py --image_dir=data/ \
 --learning_rate=0.0001 \
 --testing_percentage=20 \
 --validation_percentage=20 \
 --train_batch_size=32 \
 --validation_batch_size=-1 \
 --flip_left_right True \
 --random_scale=30 \
 --random_brightness=30 \
 --eval_step_interval=100 \
 --how_many_training_steps=1000 \
 --architecture mobilenet_1.0_224

 ```
### chu thich : 

 - --image_dir : vi tri de data anh
 - --learning_rate : alpha
 - --testing_percentage & --validation_percentage : % so data lay lam tap testing va validate, su dung de tinh train accuracy
 - --validation_batch_size=-1 : su dung tat ca data de validate ( khi data khong co nhieu )
 - --architecture : loai model su dung
### Sau khi train, trong folder /tmp/ se co 2 file
> - output_graph.pb
> - output_labels.txt
 
### Su dung label_image.py cung 2 file nay de predict bien bao trong anh
 ```
 python label_image.py --image=images.jpeg --graph=output_graph.pb --labels=output_labels.txt
 ```
 va ket qua thu duoc :
 ```
 stop 0.961738

 ```
 ## TODO : Modify lai file label_image voi input la directory chua anh, output ghi ra file txt

 
