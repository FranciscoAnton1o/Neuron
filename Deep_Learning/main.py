from core import predictor
from core.VideoCamera import VideoCamera, start_Test

if __name__ == "__main__":
    model = predictor.predictor_load_model()
    camera = VideoCamera(model)
    start_Test(camera)
