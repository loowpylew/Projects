asect  0x00

# =================================
# INSERT YOUR CODE BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------

  ldi r1,16     # r1 = 16
  ldi r2,0x20   # r2 = 0x20
  st  r2,r1     # mem[r2] = r1



# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0,0x20  # Loads the start address of your result into r0 for the robot
    halt         # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you. You will need to test your program by
# compiling and running it
# ---------------------------------------------------------------------

INPUTS>
ENDINPUTS>

asect 0x20
ds 3	# ds 3 reserves three memory cells for program output

end



