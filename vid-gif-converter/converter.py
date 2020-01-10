import imageio
import os

clip = os.path.abspath("4_2.mp4")

def gifMaker(inputPath, inputFormat):
    outputPath = os.path.splitext(inputPath[0] + inputFormat)

    print(f"Converting {outputPath} \n to {outputPath}")
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()["fps"]

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)

    print("Done!")
    writer.close()

gifMaker(clip, ".gif")
#print(clip)
