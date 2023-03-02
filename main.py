import argparse
import os
from pydub import AudioSegment

#`python split_audio.py input_file.mp3 output_directory --num_chunks 5`
def split_audio(input_file, output_directory, num_chunks=None, time_limit=None):
    # read input file
    audio = AudioSegment.from_file(input_file, format="mp3")

    # calculate chunk size based on number of chunks or time limit
    if num_chunks is not None:
        chunk_size = len(audio) // num_chunks
    elif time_limit is not None:
        chunk_size = time_limit * 1000
    else:
        raise ValueError("Either num_chunks or time_limit must be specified")

    # create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # split audio into chunks and save each chunk as a separate file
    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, len(audio))
        chunk = audio[start:end]
        output_file = os.path.join(output_directory, f"chunk{i+1}.mp3")
        chunk.export(output_file, format="mp3")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split an MP3 file into chunks.")
    parser.add_argument("input_file", help="path to input MP3 file")
    parser.add_argument("output_directory", help="path to output directory")
    parser.add_argument("--num_chunks", type=int, help="number of chunks to split the audio into")
    parser.add_argument("--time_limit", type=float, help="time limit for each audio clip in seconds")
    args = parser.parse_args()

    split_audio(args.input_file, args.output_directory, args.num_chunks, args.time_limit)