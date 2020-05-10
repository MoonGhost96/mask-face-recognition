模型来源于https://github.com/AIZOOTech/FaceMaskDetection

使用方法
运行keras_infer.py脚本即可，所有包都可以使用默认版本，keras需要调用backend，至少需要tensorflow等一个框架

1 图片 --mode image --path [yourimage]  
例 : python keras_infer.py --mode image --path ./testimages/timg.jpg

2 视频 --mode video --path [yourvideo] 

例 : python keras_infer.py --mode video --path ./testvideos/test.mp4

3 摄像头 直接运行keras_infer.py

目前运行时无法停止问题，请直接ctrl+c解决


