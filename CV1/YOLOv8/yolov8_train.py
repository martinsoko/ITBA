from argparse import ArgumentParser
from ultralytics import YOLO


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-c', '--config-file', required=True)
    parser.add_argument('-e', '--epochs', type=int, required=True)
    parser.add_argument('-m', '--model', default='yolov8s.pt')
    args = parser.parse_args()


    model = YOLO(args.model)
    model.train(data=args.config_file, epochs=args.epochs, pretrained=True)

