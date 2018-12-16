# QNAP Album Artist
This script will set the "Album Artist" ID3 tag in all the audio files in a directory.

## Why?
QNAP Music Station organizes the library using the tag "Album Artist".

## Usage

```
Usage: fillalbumartist.py [OPTIONS]

Options:
  -d, --dir TEXT  Directory  [required]
  --help          Show this message and exit.
```

## Docker image

I built a Docker image (ARMv7) for the QNAP Container Station:

https://hub.docker.com/r/xezpeleta/albumartist

You should map your Music directory to "/data" directory in the container.
