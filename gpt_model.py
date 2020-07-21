import torch
import torch.nn as nn
from kogpt2.pytorch_kogpt2 import get_pytorch_kogpt2_model
from kogpt2.utils import get_tokenizer
from gluonnlp.data import SentencepieceTokenizer

tok_path = get_tokenizer()
_, gpt_vocab = get_pytorch_kogpt2_model()
gpt_tokenizer = SentencepieceTokenizer(tok_path)

class GPT2(nn.Module):
    def __init__(self):
        super(GPT2, self).__init__()
        self.tok_path = get_tokenizer()
        self.gpt_model, self.vocab = get_pytorch_kogpt2_model()

    def forward(self, inputs):
        pred = self.get_gpt_hidden(inputs)
        return pred.to('cuda')

    def get_gpt_hidden(self, inputs):
        return self.gpt_model(inputs)