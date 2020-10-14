asect  0x00


# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0, result: # Loads the address of your result into r0 for the robot
    halt         # Brings execution to a halt
result: 	dc 0x0A,0x16,0x1f	# addresses of three items
# =================================
# DATA GOES BELOW
# Just add here the data definitions as instructed.
# (different values, starting with address 0x0A)
# ---------------------------------------------------------------------

INPUTS>
asect 0x0A
dc "Hello world",0

ENDINPUTS>

end



