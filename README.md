# startmeapp-hackaton-lstm
#Startmeapp Huawei y EL PAÍS RETINA se unen para lanzar el primer hackathon de Inteligencia Artificial. En este repositorio se puede encontrar la solución del equipo LSTM (finalista y compitiendo por el primer puesto) 

## Set-up

1. Download model weights from [here](https://drive.google.com/drive/folders/1zG9meAedyeCRKdn9ITongVCa8vIInBxM?usp=sharing).
2. Move model files to src/model_data.
3. Run YOLO detection specifying the model to use.
```
python predict.py [OPTIONS...] --image, for image detection mode,
python predict.py [video_path] [output_path (optional)] for video detection mode OR
python predict.py [--webcam] for webcam detection
```

### Usage
Use --help to see usage of predict.py:
```
usage: predict.py [-h] [--model MODEL] [--anchors ANCHORS]
                     [--classes CLASSES] [--gpu_num GPU_NUM]
                     [--image] [--webcam]
                     [--input] [--output]

positional arguments:
  --input_path  INPUT      Input path
  --output_path INPUT      Output path

optional arguments:
  -h, --help         show this help message and exit
  --model_path MODEL      path to model weight file, default model_data/yolo.h5
  --anchors_path ANCHORS  path to anchor definitions, default model_data/yolo_anchors.txt
  --classes_path CLASSES  path to class definitions, default model_data/coco_classes.txt
  --gpu_num GPU_NUM  Number of GPU to use, default 1
  --image            Image detection mode
  --webcam           Webcam detection mode

customization arguments:
  --colors 'r, b, ...' Force bboxes colors to given list, current options (r, g, b, c, m, y, k, w)
  --noescore           Avoid printing score on bboxes
```
