asect  0x00

# =================================
# INSERT YOUR CODE BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------
ldi r0, a 
ld r0, r0 
ldi r1, 1
if 
cmp r0, r1
is mi 
ldi r0, 0x2D
ldi r1, sign 
st r1, r0  
fi
if
cmp r0, r1
is pl 
ldi r0, 0x2B
ldi r1, sign 
st r1, r0
fi
if 
cmp r0, r0
is eq
ldi r0, 0x00
ldi r1, sign 
st r1, r0
fi



# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0, sign  # Loads the address of your result into r0 for the robot
    halt          # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you, but you will need to test your program by
# compiling and running it several times with different input data values
# (different integers placed at address a)
# ---------------------------------------------------------------------

INPUTS>
a:    dc  1    # replace -8 by your choice of integers for testing
ENDINPUTS>

sign:  ds 1    # one byte reserved for the result
end

