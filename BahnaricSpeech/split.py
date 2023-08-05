import glob
from collections import defaultdict

if __name__ == "__main__":
    # Collect all the original videos
    file_paths = sorted(glob.glob("BahnaricSpeech/wavs/*.wav"))
    original_videos = defaultdict(list)
    for file_path in file_paths:
        video_id = file_path[:-8]
        original_videos[video_id].append(file_path)

    # Use the original videos to split the data into train, val
    train_videos = list(original_videos.keys())[: int(len(original_videos) * 0.95)]
    val_videos = list(original_videos.keys() - set(train_videos))

    train_audios = sum([original_videos[video_id] for video_id in train_videos], [])
    val_audios = sum([original_videos[video_id] for video_id in val_videos], [])

    # Save the split into a file
    with open("BahnaricSpeech/training.txt", "w") as f:
        f.write("\n".join(train_audios))
    with open("BahnaricSpeech/validation.txt", "w") as f:
        f.write("\n".join(val_audios))
