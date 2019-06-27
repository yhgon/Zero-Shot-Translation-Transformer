# -*- coding: utf-8 -*-
#/usr/bin/python2

import os

class Hyperparams:

    # preprocessor.py - DownLoad & Preprocess & Save data to disk

    DATASET = 'OpenSubTitle2018'  # You can use 'OpenSubTitle2018' dataset if you change DATASET as 'OpenSubTitle2018' MultiUN
    # data_path: dir for raw data (download dir)
    data_path = '/mnt/workspace/zst/raw'
    # save_path: dir for [training / development / vocabulary data] (preprocessed data will be save at this dir)
    save_path = '/mnt/workspace/zst/dataset'
    # languages: Languages that will be used for training and development (for download)
    # you can check possible languages in "http://opus.nlpl.eu/OpenSubtitles2018.php" / "http://opus.nlpl.eu/UN.php"
    languages = ['ES', 'EN', 'FR', 'KO', 'DE', 'JA', 'ZH','IT', 'EL', 'MN','RO','RU'  ]
    #EL : greek, DE: deutch, JA : japan, FR: french, ES : spanish, ZH : chinese, IT : italian,  MN: mongolian, RO : romanian, RU : russian
    # resampling_size: # Maximum size of each parallel language data
    resampling_size = int(5*1e8)
    # dev_from / dev_t0 Development data ( From Language / To Language )
    dev_from = 'EN'
    dev_to = 'KR'
    # dev_size: Define Development data size
    dev_size = int(5*1e5)
    # max_len: Maximum length of tokenized data
    max_len = 60
    min_len = 10

    # data_load.py

    # vocab_path: dir contains vocab files
    vocab_path = os.path.join(save_path, 'vocab')
    # minimum_count: Vocab having lower frequency than minimum count will be discarded
    minimum_count = 10
    zeroshot_train_input = os.path.join(save_path, 'train', 'FROM')  # training data file (FROM)
    zeroshot_train_output = os.path.join(save_path, 'train', 'TO')  # training data file (TO)
    zeroshot_dev_input = os.path.join(save_path, 'dev', 'FROM')  # development data file (FROM)
    zeroshot_dev_output = os.path.join(save_path, 'dev', 'TO')  # development data file (TO)

    batch_size = 256
    num_epochs = 100
    
    # train.py

    # train path : path for saving event / graph ...
    train_path = os.path.join(save_path, 'train')
    num_units = 256
    num_blocks = 6  # number of encoder/decoder blocks
    num_heads = 8
    dropout_rate = 0.2
    warmup_step = 10000

    summary_every_n_step = 300
    save_every_n_step = 3000
    evaluate_every_n_step = 1000

hp = Hyperparams()

