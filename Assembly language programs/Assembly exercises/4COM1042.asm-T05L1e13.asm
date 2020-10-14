asect  0x00

# =================================
# INSERT YOUR CODE BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------
ldi r0, 0x20 
ld r0, r1
ldi r0, 0x21
ld r0, r2
add r1, r2
ldi r0, 0x22
st r0, r2



# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0,0x22  # Loads the address of your result into r0 for the robot
    halt         # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you, but you will need to test your program by
# compiling and running it several times with different input data values
# (different bit-strings placed at addresses 0x20 and 0x21)
# ---------------------------------------------------------------------

asect 0x20
INPUTS>
  dc 21    # Input data (for testing) should be in this memory cell
  dc 34    # Input data (for testing) should be in this memory cell
ENDINPUTS>

  ds 1     # This memory cell is where the output will end up
end

