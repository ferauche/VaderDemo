from subprocess import call


def play_sound( filename ):
   call(["./pifmlib/pifm", filename])
   return

def playMp3( filename ):
   call(["./mp3player.sh", filename])
