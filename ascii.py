import ascii_magic

my_art = ascii_magic.from_image('C:/E/IMPP!/Untitled.png')
my_art.to_html_file(path='hmm.html',columns=500, width_ratio=2,monochrome=True)


