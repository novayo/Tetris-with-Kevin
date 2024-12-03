"This is a file for building relative paths"

from pathlib import Path

picture_directory = Path(__file__).parent / "picture"
block_picture = [
    "picture_1.jpg",
    "picture_2.jpg",
    "picture_3.jpg",
    "picture_4.jpg",
    "picture_5.jpg",
    "picture_6.jpg",
    "picture_7.jpg",
]
block_picture_path = [picture_directory/ picture for picture in block_picture]
background_picture_path = picture_directory/ "background.jpeg"
