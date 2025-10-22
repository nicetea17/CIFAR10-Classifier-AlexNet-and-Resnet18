# CIFAR10 Classification:
The objective is to properly classify CIFAR10 images using two models: AlexNet and ResNet18.

# Model:
The configuration of each model can be found in the "configs" folder in this repo.

AlexNet uses a deep convolutional neural network (CNN) architecture with ReLU activations, max pooling, dropout, and fully connected layers.

ResNet uses residual (skip) connections composed of convolutional, batch normalization, and ReLU layers with identity shortcuts that learn residual mappings instead of direct mappings.

# Results:
<img src="wandb visual.png" alt="Wandb Visualization" width="1000"/>

The maximum accuracy for Resnet18 is 91.00%.

The maximum accuracy for AlexNet is 77.45%.

<img src="wandb visual with details.png" alt="Wandb Visualization" width="1000"/>
