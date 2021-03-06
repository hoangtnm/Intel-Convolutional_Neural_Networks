from transformers import (BertConfig, BertForMaskedLM,
                          BertForSequenceClassification, BertModel,
                          BertTokenizer, DistilBertConfig,
                          DistilBertForMaskedLM,
                          DistilBertForSequenceClassification, DistilBertModel,
                          DistilBertTokenizer, GPT2Config, GPT2LMHeadModel,
                          GPT2Model, GPT2Tokenizer, OpenAIGPTConfig,
                          OpenAIGPTLMHeadModel, OpenAIGPTModel,
                          OpenAIGPTTokenizer, RobertaConfig,
                          RobertaForMaskedLM, RobertaForSequenceClassification,
                          RobertaModel, RobertaTokenizer, XLNetConfig,
                          XLNetForSequenceClassification, XLNetModel,
                          XLNetTokenizer)

model_class_dict = {
    'bert': BertModel,
    'gpt': OpenAIGPTModel,
    'gpt2': GPT2Model,
    'xlnet': XLNetModel,
    'distilbert': DistilBertModel,
    'roberta': RobertaModel
}

model_class_lm_dict = {
    'bert': BertForMaskedLM,
    'gpt': OpenAIGPTLMHeadModel,
    'gpt2': GPT2LMHeadModel,
    'distilbert': DistilBertForMaskedLM,
    'roberta': RobertaForMaskedLM
}

model_class_glue_dict = {
    'bert': BertForSequenceClassification,
    'xlnet': XLNetForSequenceClassification,
    'distilbert': DistilBertForSequenceClassification,
    'roberta': RobertaForSequenceClassification
}

model_config_dict = {
    'bert': BertConfig,
    'gpt': OpenAIGPTConfig,
    'gpt2': GPT2Config,
    'xlnet': XLNetConfig,
    'distilbert': DistilBertConfig,
    'roberta': RobertaConfig
}

model_tokenizer_dict = {
    'bert': BertTokenizer,
    'gpt': OpenAIGPTTokenizer,
    'gpt2': GPT2Tokenizer,
    'xlnet': XLNetTokenizer,
    'distilbert': DistilBertTokenizer,
    'roberta': RobertaTokenizer
}

model_pretrained_weights = {
    'bert': 'bert-base-multilingual-cased',
    'gpt': 'openai-gpt',
    'gpt2': 'gpt2',
    'xlnet': 'xlnet-base-cased',
    'distilbert': 'distilbert-base-uncased',
    'roberta': 'roberta-base'
}
