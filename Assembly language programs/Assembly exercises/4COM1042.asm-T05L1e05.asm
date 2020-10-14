asect  0x00
# =================================
# LEAVE THIS PART OF THE FILE ALONE
# This is some initialisation code to load some values into the registers
	ldi r1,x
	ld r1,r1	  # r1 = mem[x]
	ldi r2,y
	ld r2,r2	  # r2 = mem[y]

# =================================
# INSERT YOUR ADDITIONAL CODE BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------




# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next four instructions: they must be the last four
# instructions executed by your program.
    push r2
    push r1
    ldsa r0,0  # load the address of the current stack pointer into r0 for the robot
    halt       # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you, but you will need to test your program by
# compiling and running it several times with different input data values
# ---------------------------------------------------------------------

INPUTS>
# Input data (for testing) should be in the following memory cells:
 x:   dc 15
 y:   dc 14
ENDINPUTS>

end



