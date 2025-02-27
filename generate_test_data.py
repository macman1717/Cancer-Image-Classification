import os
import shutil
import random

data_dir = "archive/Multi Cancer/data/Brain Cancer"
test_dir = "archive/Multi Cancer/data/test"

test_split = 0.15

os.makedirs(test_dir, exist_ok=True)

for class_name in os.listdir(data_dir):
    class_path = os.path.join(data_dir, class_name)
    test_class_path = os.path.join(test_dir, class_name)
    os.makedirs(test_class_path, exist_ok=True)
    
    images = [f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

    num_test_images = int(len(images) * test_split)
    test_images = random.sample(images, num_test_images)

    for img in test_images:
        src_path = os.path.join(class_path, img)
        dst_path = os.path.join(test_class_path, img)
        shutil.move(src_path, dst_path)

    print(f"moved {num_test_images} images from {class_name} to test set.")

print("all done :)")
