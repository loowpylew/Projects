asect  0x00

# =================================
# INSERT YOUR CODE BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------
ldi r0, a 
ld r0, r1
move r1, r2
shla r1
shla r1
shla r1
add r2, r1
add r2, r1 
ldi r0, b
ld r0, r3
shla r3
shla r3
ldi r0, 12
add r0, r3
sub r1, r3
ldi r0, res
st r0, r3




# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0, res  # Loads the address of your result into r0 for the robot
    halt         # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you, but you will need to test your program by
# compiling and running it several times with different input data values
# (different bit-strings placed at addresses a and b)
# ---------------------------------------------------------------------

INPUTS>
a:  dc  1       # replace 0 by your choice of integer for testing
b:  dc  1       # replace 0 by your choice of integer for testing
ENDINPUTS>

res:	ds	1		# one byte reserved for the result
end

