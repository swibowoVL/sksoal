ps ax | grep usr | grep python | grep sksoal | cut -d" " -f1 | awk '{printf("kill -9 %s\n",$0)}'| bash
ps ax | grep usr | grep python | grep sksoal | cut -d" " -f2 | awk '{printf("kill -9 %s\n",$0)}'| bash
ps ax | grep usr | grep python | grep sksoal | cut -d" " -f3 | awk '{printf("kill -9 %s\n",$0)}'| bash
