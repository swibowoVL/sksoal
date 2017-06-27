ps ax |  grep python3 | cut -d" " -f1 | awk '{printf("kill -9 %s\n",$0)}'| bash
ps ax |  grep python3 | cut -d" " -f2 | awk '{printf("kill -9 %s\n",$0)}'| bash
ps ax |  grep python3 | cut -d" " -f3 | awk '{printf("kill -9 %s\n",$0)}'| bash
ps ax |  grep python3 | cut -d" " -f4 | awk '{printf("kill -9 %s\n",$0)}'| bash
