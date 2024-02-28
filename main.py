from pyfirmata import Arduino, util
board = Arduino('/dev/tty.usbserial-A6008rIF')
board.digital[13].write(1)
