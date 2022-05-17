# YoutubeToStems
Convert a youtube (musical) video into 5 audio stems (Vocals, Bass, Piano, Drums and Everything_else)

Credits:
90% of the credits and the magic goes to [Spleeter](https://github.com/deezer/spleeter) for their awesome ML algorithm.<br>
5% goes to [pytube](https://pytube.io/en/latest/) for the youtube download package.

## Setup:

0. I highly recommend using a [venv](https://docs.python.org/3/library/venv.html).
1. Run <code>pip3 install requirements.txt</code>
2. install [Spleeter](https://github.com/deezer/spleeter)

## Usage (in progress):


1. Paste all the youtube's url you want to convert to <code>inputFile.txt</code>, one below the other (I do not take any responsability for copyright infringments)
2. Run <code>./run.sh  <instrument_to_remove></code> 
 (vocals, drum or bass)
3. A <code><i>current date</i>_separated_stems</code> folder will be created in the root directory. You can find in there the stem folder, and the mp3 without the istrument to remove.
4. Enjoy!!
