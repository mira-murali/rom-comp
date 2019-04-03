import torch, sys, time, os
import numpy as np

array_of_lists = np.load(sys.argv[1])	#(latent_vector,loss,loss,loss)
tensor_of_latents = torch.FloatTensor([latent_vector for latent_vector,loss0,loss1,loss2 in array_of_lists]).cuda()
x_tensor = tensor_of_latents.repeat(tensor_of_latents.shape[0],1)
y_tensor = tensor_of_latents.unsqueeze(1).repeat(1,tensor_of_latents.shape[0],1).reshape(-1,tensor_of_latents.shape[-1])
cos = torch.nn.CosineSimilarity(dim=1)
cos = cos.cuda()
similarity = []
for i in range(0,x_tensor.shape[0],tensor_of_latents.shape[0]):
	similarity.append(cos(y_tensor[i:i+tensor_of_latents.shape[0],:],x_tensor[i:i+tensor_of_latents.shape[0],:]).data.cpu())
sim_matrix = torch.cat(similarity,-1).reshape(-1,tensor_of_latents.shape[0]).numpy()

np.save(sys.argv[1][:sys.argv[1].index(".np")]+"_sim", sim_matrix)