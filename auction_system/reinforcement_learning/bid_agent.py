# auction_system/reinforcement_learning/bid_agent.py
import ray.rllib.algorithms.ppo as ppo

config = ppo.DEFAULT_CONFIG.copy()
config["env"] = "BiddingEnv"
config["num_workers"] = 4
trainer = ppo.PPOTrainer(config=config)