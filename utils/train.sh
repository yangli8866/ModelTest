#!/bin/bash

for i in {1..6}; do
  export RUN_INFO$i="srun -p dcbcfc7b-5e9f-4619-ac29-abae8f9b4857 --workspace-idb191b219-b7d8-4b76-85a3-a2c31087ee08 -r N1lS.Ib.I20.1 --container-image registry.st-sh-01.sensecore.cn/deeplink/dev:latest -j test$i -m --framework pytorch bash -c 'echo $i &&sleep 10' 2>&1 |tee $i.log"
done

# 执行命令
eval "$RUN_INFO1" &
sleep 1
eval "$RUN_INFO2" &
sleep 1
eval "$RUN_INFO3" &
sleep 1
eval "$RUN_INFO4" &
sleep 1
eval "$RUN_INFO5" &
sleep 1
eval "$RUN_INFO6" &

#等待所有后台进程完成
wait

#!/bin/bash

eval "bash sleep.job " &
sleep 1
eval "bash sleep.job " &
sleep 1
eval "bash sleep.job " &
sleep 1
eval "bash sleep.job " &
sleep 1
eval "bash sleep.job " &
sleep 1
eval "bash sleep.job " &
sleep 1
eval "bash sleep.job " &
sleep 1
eval "bash sleep.job " &
sleep 1
eval "bash sleep.job " &
sleep 1

wait