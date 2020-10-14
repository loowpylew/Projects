asect  0x00

# =================================
# INSERT YOUR CODE BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------
ldi r0, a
ld r0, r1
ldi r0, b
ld r0, r2 
add r1, r2
ldi r0, resLo
ld r0, r1
ldi r1, 0b00000010
ld r1, r1
ldi r0, resHi
ld r0, r3
ldi r3, 0b00000000
ld r3, r3
st r1, r1
st r3, r3






# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0, resLo  # Loads the start address of your result into r0 for the robot
    halt           # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you, but you will need to test your program by
# compiling and running it several times with different input data values
# (different bit-strings placed at addresses aLo, aHi, bLo and bHi)
# ---------------------------------------------------------------------

INPUTS>
a:	dc	1 	# replace 0 by your choice of low byte for testing
b:	dc	1 	# replace 0 by your choice of high byte for testing
ENDINPUTS>

resLo:  ds  1
resHi:  ds  1		# two bytes reserved for the result
end


