#! /usr/bin/env python

import os
import logging
import click
from mutagen.easyid3 import EasyID3

extensions = ('.ogg', '.mp3', '.flac')

@click.command()
@click.option('--dir', '-d', required=True, help="Directory")
def main(dir):
    rootdir = dir
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                filepath = os.path.join(subdir, file)
                
                logging.debug('File: %s' % filepath)
                
                try:
                    audio = EasyID3(filepath)
                except:
                    logging.error ('Error reading ID3 tags: %s' % filepath)
                    break
                
                try:
                    if not 'artist' in audio:
                        logging.warning ('WARNING: Artist tag empty')
                        break;
                    else:
                        logging.debug ('Artist: %s' % audio['artist'][0])
                except:
                    print ('error')
                    
                try:
                    if not 'albumartist' in audio:
                        audio['albumartist'] = audio['artist']
                        logging.info ('Writing tag <albumartist>: %s' % audio['artist'][0])
                        audio.save()
                except:
                    logging.error ("Error saving ID3 tags: %s" % filepath)

if __name__ == '__main__':
    main()