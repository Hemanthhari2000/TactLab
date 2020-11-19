from imageai.Detection import ObjectDetection
import os
import cv2
import foreground_extration as fe


INPUT_IMAGE = 'dog_1.jpg'
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
	# print(f"Name = {detections[0]['name']}\nCo-ordinates = {detections[0]['box_points']}")
	image = fe.extract(INPUT_IMAGE,detections[0]['box_points'])

	cv2.imshow("Extracted Image", image)
	cv2.waitKey(0)

main()