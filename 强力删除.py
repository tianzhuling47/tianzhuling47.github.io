import os
def get_all_files(directory):
    file_paths = []  # 用于存储所有文件路径的列表
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)  # 构建完整路径
	# 如果是文件，则添加到列表中
        if os.path.isfile(item_path):
            file_paths.append(item_path)
        # 如果是目录，则递归调用该函数
        elif os.path.isdir(item_path):
            file_paths.extend(get_all_files(item_path))  # 合并子目录的文件路径列表

    return file_paths  # 返回所有文件的路径列表

# 示例用法

def is_image_file(file_path):
    """判断文件是否为图片类型"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tif', '.tiff']
    file_extension = os.path.splitext(file_path)[-1].lower()
    return file_extension in image_extensions and not file_path.split('/')[-1][0]=='.'
# 打印获取到的图片文件路径
def is_audio_file(file_path):
	audio_extensions = [
    ".mp3",
    ".wav",
    ".aac",
    ".flac",
    ".ogg",
    ".wma",
    ".m4a",
    ".amr",
    ".aiff",
    ".au"
]
	file_extension = os.path.splitext(file_path)[-1].lower()
	return file_extension in audio_extensions and not file_path.split('/')[-1][0]=='.'
def is_video_file(file_path):
	video_extensions = [
    ".avi",
    ".wmv",
    ".mpg",
    ".mpeg",
    ".mov",
    ".rm",
    ".ram",
    ".swf",
    ".flv",
    ".mp4",
    ".mkv",
    ".vob",
    ".3gp",
    ".asf",
    ".asx",
    ".divx",
    ".mpe",
    ".rmvb"
]
	file_extension = os.path.splitext(file_path)[-1].lower()
	return file_extension in video_extensions and not file_path.split('/')[-1][0]=='.'
def is_apk_file(file_path):
	file_extension = os.path.splitext(file_path)[-1].lower()
	return file_extension=='.apk' and not file_path.split('/')[-1][0]=='.' 
def is_zip_file(file_path):
	file_extension = os.path.splitext(file_path)[-1].lower()
	return file_extension=='.zip' and not file_path.split('/')[-1][0]=='.' 
def is_doc_file(file_path):
	document_extensions = [
    ".txt",    # 文本文件
    ".docx",   # Microsoft Word 文档
    ".doc",    # 旧版 Microsoft Word 文档
    ".xlsx",   # Microsoft Excel 工作簿
    ".xls",    # 旧版 Microsoft Excel 工作簿
    ".pptx",   # Microsoft PowerPoint 演示文稿
    ".ppt",    # 旧版 Microsoft PowerPoint 演示文稿
    ".pdf",    # Adobe PDF 文件
    ".odt",    # OpenDocument 文本文件
    ".ods",    # OpenDocument 表格文件
    ".odp",    # OpenDocument 演示文稿文件
    ".md",     # Markdown 文件
    ".html",   # HTML 文件
    ".htm",    # HTML 文件（旧版后缀）
    ".rtf",    # Rich Text Format 文件
    ".pages",  # Apple Pages 文档
    ".numbers",# Apple Numbers 表格
    ".key",    # Apple Keynote 演示文稿
]
	file_extension = os.path.splitext(file_path)[-1].lower()
	return file_extension in document_extensions and not file_path.split('/')[-1][0]=='.'
directory_path = '/storage/emulated/0/'  # 替换为你的目录路径
all_files = get_all_files(directory_path)
image_files=[]
for i in all_files:
	if is_image_file(i):
		image_files.append(i)
a=0
for image_file in image_files:
    a+=1
    print(image_file)
a=input('以上为根目录下所有的图片，是否删除(y/n):')
if a=='y':
	if input('确定(y/n)(1/3):')=='y':
		if input('确定(y/n)(2/3):')=='y':
			if input('确定(y/n)(3/3):')=='y':
				for i in image_files:
						os.remove(i)
del image_file
audio_files=[]
for i in all_files:
	if is_audio_file(i):
		audio_files.append(i)
for audio in audio_files:
	print(audio)				
a=input('以上为根目录下所有的音频文件,是否删除 (y/n) ')	
if a=='y':
	if input('确定(y/n)(1/3):')=='y':
		if input('确定(y/n)(2/3):')=='y':
			if input('确定(y/n)(3/3):')=='y':
				for i in audio_files:
					os.remove(i)
del audio_files
video_files=[]
for i in all_files:
	if is_video_file(i):
		video_files.append(i)
for video in video_files:
	print(video)				
a=input('以上为根目录下所有的视频文件,是否删除 (y/n) ')	
if a=='y':
	if input('确定(y/n)(1/3):')=='y':
		if input('确定(y/n)(2/3):')=='y':
			if input('确定(y/n)(3/3):')=='y':
				for i in video_files:
					os.remove(i)
del video_files
apk_files=[]
for i in all_files:
	if is_apk_file(i):
		apk_files.append(i)
for apk in apk_files:
	print(apk)				
a=input('以上为根目录下所有的安装包文件,是否删除 (y/n) ')	
if a=='y':
	if input('确定(y/n)(1/3):')=='y':
		if input('确定(y/n)(2/3):')=='y':
			if input('确定(y/n)(3/3):')=='y':
				for i in apk_files:
					os.remove(i)
del apk_files
zip_files=[]
for i in all_files:
	if is_zip_file(i):
		zip_files.append(i)
for zip in zip_files:
	print(zip)				
a=input('以上为根目录下所有的压缩包文件,是否删除 (y/n) ')	
if a=='y':
	if input('确定(y/n)(1/3):')=='y':
		if input('确定(y/n)(2/3):')=='y':
			if input('确定(y/n)(3/3):')=='y':
				for i in zip_files:
					os.remove(i)
del zip_files
doc_files=[]
for i in all_files:
	if is_doc_file(i):
		doc_files.append(i)
for doc in doc_files:
	print(doc)
a=input('以上为根目录下所有的文档文件以及HTML文件 ,是否删除 (y/n) ')	
if a=='y':
	if input('确定(y/n)(1/3):')=='y':
		if input('确定(y/n)(2/3):')=='y':
			if input('确定(y/n)(3/3):')=='y':
				for i in doc_files:
					os.remove(i)