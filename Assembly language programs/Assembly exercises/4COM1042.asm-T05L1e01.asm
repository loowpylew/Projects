asect  0x00

# =================================
# UNCOMMENT THE CODE BELOW by removing the # at the
# beginning of each line that contains a CdM-8 instruction
# No need to add any instructions of your own
# Test the program by re-compiling and running with
# different values placed in locations 0x20 and 0x21
# Check the result that ends up in location 0x30 each time
# ---------------------------------------------------------------------

#    ldi r0, 0x20
#    ld  r0, r1
#    ldi r0, 0x21
#    ld  r0, r2
#    add r1, r2
#    ldi r0, 0x30
#    st  r0, r2

# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0, 0x30    # Loads the address 0x30 (where the result was stored) into r0 for the robot
    halt            # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you, but you will need to test your program by
# compiling and running it several times with different input data values
# (different values placed at addresses 0x20 and 0x21)
# ---------------------------------------------------------------------

asect 0x20
INPUTS>
dc 15    # Change the number after the dc to change the input data placed at location 0x20
dc 26    # Change the number after the dc to change the input data placed at location 0x21
ENDINPUTS>

RESULTS>
asect 0x30
ds 1     # Memory cell 0x30 is where the output will end up
ENDRESULTS>

end

