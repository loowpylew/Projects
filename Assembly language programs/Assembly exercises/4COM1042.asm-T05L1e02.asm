asect  0x00


# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0, 0x0F # Loads the address of your result into r0 for the robot
    halt         # Brings execution to a halt

# =================================
# DATA GOES BELOW
# Just add here the data definitions as instructed.
# (different values, starting with address 0x10)
# ---------------------------------------------------------------------

INPUTS>

ENDINPUTS>

asect 0x0F

dc 13

end



