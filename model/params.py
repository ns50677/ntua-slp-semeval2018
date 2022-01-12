"""

Model Configurations

"""


TASK3_A = {
    "name": "TASK3_A",
    "token_type": "word",
    "batch_train": 64,
    "batch_eval": 64,
    "epochs": 50,
    "embeddings_file": "ntua_twitter_affect_310",
    "embed_dim": 310,
    "embed_finetune": False,
    "embed_noise": 0.05,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.2,
    "encoder_size": 150,
    "encoder_layers": 2,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 1,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.0,
    "base": 0.7,
    "patience": 10,
    "weight_decay": 0.0,
    "clip_norm": 1,
}

TASK3_B = {
    "name": "TASK3_B",
    "token_type": "word",
    "batch_train": 32,
    "batch_eval": 32,
    "epochs": 50,
    "embeddings_file": "ntua_twitter_affect_310",
    "embed_dim": 310,
    "embed_finetune": False,
    "embed_noise": 0.2,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.2,
    "encoder_size": 150,
    "encoder_layers": 2,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 1,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.0,
    "base": 0.3,
    "patience": 10,
    "weight_decay": 0.0,
    "clip_norm": 1,
}