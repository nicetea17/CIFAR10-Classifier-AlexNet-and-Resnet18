import wandb
import random

wandb.login()

project = "AlexNet visualize"
config = {'epochs':20, 'lr':3e-4}

with wandb.init(project=project, config=config) as run:
    offset = random.random() / 5
    for epoch in range(2, config['epochs']):
        acc = 1 - 2**-config['epochs'] - random.random() / config['epochs'] - offset
        loss = 2**-config['epochs'] + random.random() / config['epochs'] + offset
        run.log({"accuracy": acc, "loss": loss})
