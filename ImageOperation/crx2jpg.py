import rawpy
import cv2
import os
import multiprocessing

dir = R"E:\Desktop\test"
CRX = '.CR3'
MultiProcessing = True
DeleteTheSourceFile = True
FFmpegCompression = True

def crx_to_jpg(crx_file_path):
    if not (crx_file_path.endswith(CRX) or crx_file_path.endswith(CRX)):
        return
    print(f'Task got {crx_file_path}')
    jpg_file_path = crx_file_path.replace(CRX, '.jpg')
    jpg_file_path = crx_file_path.replace(CRX, '.jpg')
    cr2_img = rawpy.imread(crx_file_path)
    rgb_img = cr2_img.postprocess()
    bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    if cv2.imwrite(jpg_file_path, bgr_img, [cv2.IMWRITE_JPEG_QUALITY, 90]):
        print(f'Save to {jpg_file_path}')
    else:
        print(f'fail to convert: {crx_file_path}')

if __name__ == '__main__':
    files = [os.path.join(dir, file) for file in os.listdir(dir) if file.endswith(CRX)]

    if MultiProcessing:
        p = multiprocessing.Pool()
        for file in files:
            p.apply_async(crx_to_jpg, args=(file,))
        p.close()
        p.join()
    else:
        for file in files:
            crx_to_jpg(file)
    print('Conversion task completed.')

    if DeleteTheSourceFile:
        for file in files:
            os.system(f'del {file}')
    print('Deletion task completed.')

    if FFmpegCompression:
        files_jpg = [os.path.join(dir, file) for file in os.listdir(dir) if file.endswith('.jpg')]
        for file in files_jpg:
            os.system(f'ffmpeg -i {file} {file} -y')
    print('FFmpeg compression task completed.')

    print('All task completed.')
