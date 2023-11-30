 from PIL import Image
import os

def compress_and_convert(source_path, dest_path, quality=50, format='JPEG'):
    """
   转换图片格式
    :param source_path: 原图片路径
    :param dest_path: 目标图片路径
    :param quality: 图片质量，取值范围0-100，默认为50
    :param format: 目标图片格式，默认为JPEG
    """
    # 打开原图片
    with Image.open(source_path) as img:
        # 压缩图片
        img.save(dest_path, optimize=True, quality=quality)

        # 转换图片格式
        if format != img.format:
            file_name = os.path.splitext(dest_path)[0]
            dest_path = f"{file_name}.{format.lower()}"
            img.save(dest_path, optimize=True, quality=quality)

# 示例调用
compress_and_convert("input.png", "output.jpg", quality=60, format='JPEG')
