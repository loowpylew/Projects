asect  0x00

# =================================
# INSERT YOUR CODE BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------

ldi r0, 3
ldi r1, 0b00000101
ldi r2, 0x0F
ldi r3, 57

# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next five instructions: they must be the last six
# instructions executed by your program.
    push r3
    push r2
    push r1
    push r0
    ldsa r0,0  # load the address of the current stack pointer into r0 for the robot
    halt       # Brings execution to a halt

# =================================
# NO DATA NEEDED BELOW
# We have set this up for you
# ---------------------------------------------------------------------

INPUTS>
ENDINPUTS>

end
