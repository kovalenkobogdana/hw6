import numpy as np
from tree import DT, Tree
from dataset import CandyDataset
from node import Node
def buildTree(self,inputs,targets,node,depth):
 entropy_val = calculate_entropy(targets)
 if(depth >= self.max_depth or node.entropy_val <= self.min_entropy or len(targets)<=self.min_elem):
 node.T = terminal_node_output(targets)
 else:
#обучение
 node.left = Node()
 node.right = Node()
 buildTree(inputs_left,targets_left,node.left,depth+1)
 buildTree(inputs_right, targets_right, node.right,depth+1)

