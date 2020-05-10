import argparse
import os
def inference(image,
              conf_thresh=0.5,
              iou_thresh=0.4,
              target_shape=(160, 160),
              draw_result=True,
              show_result=True
              ):
    print(image)



def run_on_video(video_path, output_video_name, conf_thresh):
    print(video_path)
os.sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Face Mask Detection")
    parser.add_argument('--mode', type=str, default='cemera', help='set image to run on image,video to run on video,cemera to run on cemera.')
    parser.add_argument('--path', type=str, default='0', help='path to your image or video.')
    args = parser.parse_args()

    print(args)



    if args.mode == 'image':
        imgPath = args.path
        img = cv2.imread(imgPath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        inference(img, show_result=True, target_shape=(260, 260))
    elif args.mode == 'video':
        video_path = args.path
        run_on_video(video_path, '', conf_thresh=0.5)
    else:
        run_on_video(0,'',conf_thresh=0.5)
