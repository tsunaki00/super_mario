########################################
##   http://siva-ai.com               ##
##           r=､r=､                   ##
##           {θ{θ}                    ##
##       /´l r ｀'､_,ﾉi、              ##
##     {            )                 ##
##      `､ 　 _.r（_ ﾉ                 ##
##        `´-r _ノ)                   ##
##           / !`i）                  ##
##           i　　i　｢ﾝ__r'^i          ##
##          /!　/ (_`!し'i　j          ##
##          Li､ '､_ツ`ｰ' /             ##
##          __ >､j__   r'             ##
##         i'´  Y⌒ヽ￣｝               ##
##         `=-{        ）             ##
##           　`-=='`='               ##
##    @author tsunaki                 ##
########################################
import tensorflow as tf
import gym
import gym_pull
import ppaquette_gym_super_mario
from gym.wrappers import Monitor
import random
import numpy as np
class Game :

  def __init__(self):
    self.episode_count = 10000;
    ## select stage
    self.env = gym.make('ppaquette/SuperMarioBros-1-1-Tiles-v0')

  def weight_variable(self, shape):
    initial = tf.truncated_normal(shape, stddev = 0.01)
    return tf.Variable(initial)

  
  def bias_variable(self, shape):
    initial = tf.constant(0.01, shape = shape)
    return tf.Variable(initial)

  def conv2d(self, x, W, stride):
    return tf.nn.conv2d(x, W, strides = [1, stride, stride, 1], padding = "SAME")

  def max_pool_2x2(self, x):
    return tf.nn.max_pool(x, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = "SAME")

  
  def create_network(self, action_size):
    W_conv1 = self.weight_variable([3, 3, 1, 8])
    b_conv1 = self.bias_variable([8])
    W_conv2 = self.weight_variable([2, 2, 8, 16])
    b_conv2 = self.bias_variable([16])
    W_fc1 = self.weight_variable([512, action_size])
    b_fc1 = self.bias_variable([action_size])
    s = tf.placeholder("float", [None, 13, 16, 1])
    # hidden layers
    h_conv1 = tf.nn.relu(self.conv2d(s, W_conv1, 1) + b_conv1)
    h_conv2 = tf.nn.relu(self.conv2d(W_conv1, W_conv2, 2) + b_conv2)
    h_conv3_flat = tf.reshape(W_conv2, [-1, 512])
    readout = tf.matmul(h_conv3_flat, W_fc1) + b_fc1
    return s, readout 


  def play_game(self) :
    action_list = []
    for i in range(64) :
      command = format(i, 'b')
      command = '{0:06d}'.format(int(command))
      actions = []
      for cmd in list(command) :
        actions.append(int(cmd))
      action_list.append(actions)
    sess = tf.InteractiveSession()
    s, readout = self.create_network(len(action_list))
    a = tf.placeholder("float", [None, len(action_list)])
    y = tf.placeholder("float", [None, 1])
    readout_action = tf.reduce_sum(tf.multiply(readout, a), reduction_indices = 1)
    cost = tf.reduce_mean(tf.square(y - readout_action))
    train_step = tf.train.AdamOptimizer(1e-6).minimize(cost)
    saver = tf.train.Saver()
    sess.run(tf.initialize_all_variables())
    checkpoint = tf.train.get_checkpoint_state("./saved_networks/checkpoints")
    if checkpoint and checkpoint.model_checkpoint_path:
      saver.restore(sess, checkpoint.model_checkpoint_path)
      print ("Successfully loaded:", checkpoint.model_checkpoint_path)
    else:
      print ("Could not find old network weights")
    for episode in range(self.episode_count):
      self.env.reset()
      total_score = 0
      distance = 0
      is_finished = False
      actions, rewards, images = [], [] ,[]
      while is_finished == False :
        screen = np.reshape(self.env.tiles, (13, 16, 1))
        if episode < 10 :
          action_index = random.randint(0, len(action_list) - 1)
        else :
          readout_t = readout.eval(feed_dict = {s : [screen]})[0]
          action_index = np.argmax(readout_t)
        # action
        obs, reward, is_finished, info = self.env.step(action_list[action_index])
        action_array = np.zeros(len(action_list))
        action_array[action_index] = 1
        actions.append(action_array)
        rewards.append([float(info['distance'])])
        images.append(screen)

        train_step.run(feed_dict = {
          a : actions, y : rewards, s : images
        })
        print('Episode : ', episode, 'Actions : ', action_list[action_index], 'Rewards', reward)
        actions, rewards, images = [], [] ,[]
        
        self.env.render()
      saver.save(sess, 'saved_networks/model-dqn', global_step = episode)

if __name__ == '__main__' :
  game = Game()
  game.play_game()