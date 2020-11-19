from imageai.Detection import ObjectDetection
import os
import cv2

INPUT_IMAGE = 'dog.jpg'
OUTPUT_IMAGE = 'dog_op_1.jpg'

def get_rect():
	current_path = os.getcwd()
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(current_path, 'resnet50_coco_best_v2.0.1.h5'))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(current_path, INPUT_IMAGE), output_image_path= os.path.join(current_path, OUTPUT_IMAGE))
	return detections

def main():
	detections = get_rect()
	print(f"Name = {detections[0]['name']}\nCo-ordinates = {detections[0]['box_points']}")

main()