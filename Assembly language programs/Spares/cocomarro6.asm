asect  0x00

# =================================
# ADD YOUR CODE AFTER OURS BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------

    ldi r0, 0x20
    ld  r0, r1
    ldi r0, 0x21
    ld  r0, r2
    ldi r0, 0x22
    ld  r0, r3


# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next four instructions: they must be the last four
# instructions executed by your program.
    push r3
    push r2
    push r1
    ldsa r0,0 # loads the address of the current stack pointer into r0 for the robot
    halt      # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you, but you will need to test your program by
# compiling and running it several times with different input data values
# (different values placed at addresses 0x20 and 0x21)
# ---------------------------------------------------------------------

asect 0x20
INPUTS>
# Input data (for testing) should be in the following memory cells:
dc 25
dc 14
dc 37
ENDINPUTS>

end





