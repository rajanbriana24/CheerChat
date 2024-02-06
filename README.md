# CheerChat: A Mental Health Chatbot

CheerChat is a mental health chatbot designed to provide support and guidance to users experiencing mental health issues. It leverages advanced natural language processing techniques to engage in conversations with users, offering empathy, resources, and encouragement.

# Backend Script: Fine-tuning a Pre-trained Model for News Classification

The backend script provided in this repository focuses on fine-tuning a pre-trained language model for news classification using the Hugging Face Transformers library and Parameter-Efficient Fine-Tuning (PEFT) techniques. Below is an overview of the key components of the script:

## Installation of Required Libraries

The script begins by installing necessary libraries such as transformers, bitsandbytes, accelerate, peft, and trl using pip.

## Loading Required Libraries

Various libraries and modules are imported, including those for loading datasets, defining model configurations, and setting up the training environment.

## Hugging Face Hub Login

Instructions are provided for logging in to the Hugging Face Hub, which is required for accessing pre-trained models.

## Creating Bitsandbytes Configuration

A function is defined to configure model quantization using the bitsandbytes library, enabling 4-bit precision loading of the model.

## Loading Hugging Face Model and Tokenizer

Functions are provided for loading a pre-trained language model from the Hugging Face model hub and its corresponding tokenizer.

## Loading Dataset

The script loads the mental health conversational dataset from Kaggle, which contains prompts for training the chatbot.

## Preprocessing Dataset

The provided code preprocesses the dataset, including loading the JSON data, extracting intents, creating a DataFrame, iterating over patterns and responses, filling NaN values, preparing input text for training, and saving the DataFrame to a CSV file.

# Fine-tuning the Pre-trained Model

The main function `fine_tune` orchestrates the fine-tuning process, enabling PEFT and configuring training parameters. The script utilizes the Trainer class from Hugging Face Transformers for training.

# Merging Weights & Pushing to Hugging Face

Finally, the script merges the fine-tuned model's weights and pushes the model and tokenizer to the Hugging Face Hub for public usage.
