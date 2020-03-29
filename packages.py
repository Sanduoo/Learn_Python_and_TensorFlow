#包 package

#以life为例
import life.work,life.sleep

life.sleep.life_sleep()
life.work.life_work()


###########################
from life.play import life_play
life_play()


###########################
from life import eat as e
e.life_eat()

###########################
import init_data
print(init_data.Mydata)