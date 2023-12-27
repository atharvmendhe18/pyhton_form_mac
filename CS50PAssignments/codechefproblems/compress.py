def main():
    for _ in range(int(input(""))):
        compress_video()


def compress_video():
    total_frames = int(input(""))
    frames = input("").split(" ")
    compressed_frames = frames.copy()
    for i in range(len(frames) - 1):
        if frames[i] == frames[i + 1]:
            compressed_frames.remove(frames[i + 1])

    print(len(compressed_frames))


if __name__ == "__main__":
    main()
