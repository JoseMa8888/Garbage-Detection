import onnxruntime as rt
import cv2
import numpy as np
import time
import service.main as s


def detector(image_array, is_vit: bool):
    if len(image_array.shape) == 2:
        image_array = cv2.cvtColor(image_array, cv2.COLOR_GRAY2BGR)

    time_init = time.time()

    test_image = cv2.resize(image_array, (224, 224))
    im = np.float32(test_image)
    img_array = np.expand_dims(im, axis=0)

    time_elapsed_preprocessed = time.time() - time_init

    if is_vit:
        onnx_pred = s.vit.run(s.vit_output_name, {"input": img_array})

    onnx_pred = s.mn.run(s.mn_output_name, {"input": img_array})

    time_elapsed = time.time() - time_init

    garbage_type = s.class_names[np.argmax(onnx_pred[0][0])]

    return  {
        "garbage_type": garbage_type,
        "time_elapse": time_elapsed,
        "time_elapsed_preprocessed": time_elapsed_preprocessed
    }

