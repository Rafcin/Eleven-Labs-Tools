# Eleven Labs Tools

Just a simple repo that contains tools for Eleven Labs.

## Installation

Make sure you have `Python3` installed on your machine. You also need to install `ffmpeg`. To install `ffmpeg` on Ubuntu, run the following command:

```
    sudo apt-get install ffmpeg
```

## Audio Split

This tool allows you to split an audio file into multiple files. You can either split the files by time or by chunks.
`python split_audio.py input_file.mp3 output_directory --num_chunks 5`

## Notes

Notes regarding models I use for testing and how to get them to be accurate.

### J-V2 Model

Using a prompt pulled from a steam review, we can achive a close sounding response using a stability of 16% and similarity of 52%.
The prompt is as follows:

```
The characters: You will find that the characters are not what how they used to be since... What, Sonic Adventure 2? No huge spoilers for all who want this game, but I sincerely assert the point that they mature EVERYONE in this game with good character writing and emotional struggles and relation to one's self. You won't be disappointed.
```
