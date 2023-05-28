from ultralytics import YOLO

model = YOLO("yolov8s.pt")
model.train(data="/home/soko/Documents/ITBA/CV1/YOLOv8/data/train_config.yaml", epochs=100, pretrained=True)

model("/home/soko/Documents/ITBA/CV1/YOLOv8/data/train/images/20230520_173400.jpg", show=True)