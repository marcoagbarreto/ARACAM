import yaml
import numpy as np

def save_to_yaml(file_name, data):
    with open(file_name, 'w') as f:
        yaml.dump(data, f)
        

def get_transformation_matrix(transformation_devices):
    transformations = {}
    for serial, transformation_matrix in transformation_devices.items():
        transformations[serial] = np.asarray(transformation_matrix.pose_mat).tolist()
    
    return transformations

def get_intrinsics_matrix(intrinsics_devices):
    camera_intrinsics = {}
    for serial, intrinsics in intrinsics_devices.items():
        # Obtain intrinsic parameters from color stream
        fx = intrinsics[2].fx
        fy = intrinsics[2].fy
        cx = intrinsics[2].ppx
        cy = intrinsics[2].ppy
        camera_intrinsics[serial] = np.asarray([[fx, 0, cx], [0, fy, cy], [0, 0, 1]]).tolist()
    
    return camera_intrinsics

def get_index(string, images):
    index = []
    if not isinstance(string, str):
        raise Exception('string needed to search within the images titles. Try "color" or "depth"')

    for n in range(len(images)):
        if (string in images[n]):
            index.append(n)
    
    return index


def get_serial_dictionary(files, matrix):
    
    serial_path = {}
    for serial in matrix:
        for n in range(len(files)):
            if (serial in files[n]):
                serial_path[serial] = files[n]
                
    return serial_path