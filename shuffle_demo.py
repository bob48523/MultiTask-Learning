import random

......

for epoch in range(epochs)
   train()

......

train ():
   N1 = size(cifar)
   N2 = size(tiny)
   N3 = size(vgg)
   N = (N1+N2+N3)/batch_size
   batch_indx = [i for i in range(N)]
   random.shuffle(batch_indx)

   for indx in batch_indx:
      if indx >= N1+N2:
         indx = indx-N1-N2
         data_name = 'vgg'
      elif indx >= N1:
         indx = indx-N1
         data_name = 'tiny'
      else:
         data_name = 'cifar'

      inputs, targets = trainloader[data_name][indx]
      ......
   
