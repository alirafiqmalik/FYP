linux folder contains the yosys,CSAW,monosat libraries
change yosys path in cmds to ur path for yosys


# ##############################################################
# RUNNING SAT ATTACK
# For NOW
python3 /home/alira/FYP/sat_attack/run.py <locked> <unlocked> file_type(b or v)
Example
python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/tmp/tmprtl.v /home/alira/FYP/tmp/ortl.v v
# ##############################################################



# PUSING DIR after PULL
git add .
git commit -m "version 0.1.2" 
git branch -M main
git push -u upstream main
# ##############################################################