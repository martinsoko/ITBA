from argparse import ArgumentParser
from ultralytics import YOLO


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-c', '--checkpoint', default="yolov8s.pt")
    parser.add_argument('-s', '--source', default=0)
    args = parser.parse_args()

    # Descargar el checkpoint
    model = YOLO(args.checkpoint)
    # Correr inferencia en vivo usando una cámara USB
    model(source=args.source, show=True)
