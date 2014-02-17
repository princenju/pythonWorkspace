import os
cpu_num=0
if "NUMBER_OF_PROCESSORS" in os.environ:
    cpu_num=os.environ["NUMBER_OF_PROCESSORS"]
print cpu_num
print os.environ