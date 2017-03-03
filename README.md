           r=､r=､                  
           {θ{θ}                   
       /´l r ｀'､_,ﾉi、              
     {            )                
      `､ 　 _.r（_ ﾉ                 
        `´-r _ノ)                   
           / !`i）                  
           i　　i　｢ﾝ__r'^i          
          /!　/ (_`!し'i　j          
          Li､ '､_ツ`ｰ' /             
          __ >､j__   r'             
         i'´  Y⌒ヽ￣｝               
         `=-{        ）             
           　`-=='`='               
      @author tsunaki                 

<div id="installation"></div>Installation
============

You need to install [Tensorflow](https://www.tensorflow.org/)

```shell
    $ git clone https://github.com/tsunaki00/super_mario.git
    $ cd super_mario
```

```shell
    $ pip3 install -e .`
```

```shell
    $ python3 start.py 
    Traceback (most recent call last):
      File "start.py", line 22, in <module>
        import gym_pull
      File "/usr/local/lib/python3.6/site-packages/gym_pull/__init__.py", line 41, in <module>
        import gym_pull.monitoring.monitor
      File "/usr/local/lib/python3.6/site-packages/gym_pull/monitoring/monitor.py", line 10, in <module>
        class Monitor(gym.monitoring.monitor.Monitor):
    AttributeError: module 'gym.monitoring' has no attribute 'monitor'
```
 ↓
```shell
    $ vi /usr/local/lib/python3.6/site-packages/gym_pull/monitoring/monitor.py
     :
     :
    class Monitor(gym.monitoring.monitor.Monitor):
    ↓
    class Monitor(gym.monitoring.monitor_manager.MonitorManager):
```

Run

```shell
    $ python3 start.py
```

<div id="changeStage"></div>Change Stage
============

```python
  def __init__(self):
    self.episode_count = 10000;
    ## select stage
    self.env = gym.make('ppaquette/SuperMarioBros-1-1-Tiles-v0')
```

Environments included:
============
- ppaquette/meta-SuperMarioBros-v0
- ppaquette/meta-SuperMarioBros-Tiles-v0
- ppaquette/SuperMarioBros-1-1-v0
- ppaquette/SuperMarioBros-1-2-v0
- ppaquette/SuperMarioBros-1-3-v0
- ppaquette/SuperMarioBros-1-4-v0
- ppaquette/SuperMarioBros-2-1-v0
- ppaquette/SuperMarioBros-2-2-v0
- ppaquette/SuperMarioBros-2-3-v0
- ppaquette/SuperMarioBros-2-4-v0
- ppaquette/SuperMarioBros-3-1-v0
- ppaquette/SuperMarioBros-3-2-v0
- ppaquette/SuperMarioBros-3-3-v0
- ppaquette/SuperMarioBros-3-4-v0
- ppaquette/SuperMarioBros-4-1-v0
- ppaquette/SuperMarioBros-4-2-v0
- ppaquette/SuperMarioBros-4-3-v0
- ppaquette/SuperMarioBros-4-4-v0
- ppaquette/SuperMarioBros-5-1-v0
- ppaquette/SuperMarioBros-5-2-v0
- ppaquette/SuperMarioBros-5-3-v0
- ppaquette/SuperMarioBros-5-4-v0
- ppaquette/SuperMarioBros-6-1-v0
- ppaquette/SuperMarioBros-6-2-v0
- ppaquette/SuperMarioBros-6-3-v0
- ppaquette/SuperMarioBros-6-4-v0
- ppaquette/SuperMarioBros-7-1-v0
- ppaquette/SuperMarioBros-7-2-v0
- ppaquette/SuperMarioBros-7-3-v0
- ppaquette/SuperMarioBros-7-4-v0
- ppaquette/SuperMarioBros-8-1-v0
- ppaquette/SuperMarioBros-8-2-v0
- ppaquette/SuperMarioBros-8-3-v0
- ppaquette/SuperMarioBros-8-4-v0
- ppaquette/SuperMarioBros-1-1-Tiles-v0
- ppaquette/SuperMarioBros-1-2-Tiles-v0
- ppaquette/SuperMarioBros-1-3-Tiles-v0
- ppaquette/SuperMarioBros-1-4-Tiles-v0
- ppaquette/SuperMarioBros-2-1-Tiles-v0
- ppaquette/SuperMarioBros-2-2-Tiles-v0
- ppaquette/SuperMarioBros-2-3-Tiles-v0
- ppaquette/SuperMarioBros-2-4-Tiles-v0
- ppaquette/SuperMarioBros-3-1-Tiles-v0
- ppaquette/SuperMarioBros-3-2-Tiles-v0
- ppaquette/SuperMarioBros-3-3-Tiles-v0
- ppaquette/SuperMarioBros-3-4-Tiles-v0
- ppaquette/SuperMarioBros-4-1-Tiles-v0
- ppaquette/SuperMarioBros-4-2-Tiles-v0
- ppaquette/SuperMarioBros-4-3-Tiles-v0
- ppaquette/SuperMarioBros-4-4-Tiles-v0
- ppaquette/SuperMarioBros-5-1-Tiles-v0
- ppaquette/SuperMarioBros-5-2-Tiles-v0
- ppaquette/SuperMarioBros-5-3-Tiles-v0
- ppaquette/SuperMarioBros-5-4-Tiles-v0
- ppaquette/SuperMarioBros-6-1-Tiles-v0
- ppaquette/SuperMarioBros-6-2-Tiles-v0
- ppaquette/SuperMarioBros-6-3-Tiles-v0
- ppaquette/SuperMarioBros-6-4-Tiles-v0
- ppaquette/SuperMarioBros-7-1-Tiles-v0
- ppaquette/SuperMarioBros-7-2-Tiles-v0
- ppaquette/SuperMarioBros-7-3-Tiles-v0
- ppaquette/SuperMarioBros-7-4-Tiles-v0
- ppaquette/SuperMarioBros-8-1-Tiles-v0
- ppaquette/SuperMarioBros-8-2-Tiles-v0
- ppaquette/SuperMarioBros-8-3-Tiles-v0
- ppaquette/SuperMarioBros-8-4-Tiles-v0
