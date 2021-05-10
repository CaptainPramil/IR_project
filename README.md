# Depression Detection using twitter data

Depression is major cause of many disease and there are majority of people(70%) who do not visit doctor for depression. Rather they rely on social sites to pour there emotions. Using computational approaches to understand mental health status (MHS) allows us to discover and identify risky behaviors, at an early stage and can be used to provide treatment and intervention, to a population that is generally hard to reach. So we try to come up with a model that can help us predict depression using social media of a person and have proper intervention at an early stage.

## Dataset

The dataset is taken from the [1]. We are using a subset of this dataset. It consists of social media details about the users such as social network features, profile details, visual features, emotion features, topic level features, domain and user specific features. The dataset has been divided into negative and positive data on the basis of whether the user was found to be positive or negative for depression. We extract and combine all the tweets posted by the users and then divide the tweets in sets of 20.

## Plan of Work

The text data is pre-processed in the following steps:
• Step 1: Convert the text to lowercase
• Step 2: Remove the user mentions from the tweets
• Step 3: Extract and remove emojis from the tweets
• Step 4: Remove links from the tweets
• Step 5: Remove punctuations
• Step 6: Perform lemmatization

Features considered:
• Social Network features
• User profile
• Visual
• Emotion
• Domain-level

We next padd the text for the training data and append it to features and then load the data in dataloader.

![image](https://user-images.githubusercontent.com/54845581/117644289-f51df200-b1a6-11eb-9276-3b23bbaf1b60.png)


## Models Used

* LSTM

•Preprocess dataset to remove special characters, convert to lowercase characters, etc
•Tokenize the data
•Pad dataset
•Create the data loaders
•Use glove embedding to encode the data
•Pass the data to LSTM block, to get next cell and hidden state
•Flatten the cell state and pass through the softmax layer

![image](https://user-images.githubusercontent.com/54845581/117645488-4a0e3800-b1a8-11eb-999b-397ebbbdf98c.png)


* LSTM with Attention

•Preprocess dataset to remove special characters, convert to lowercase characters, etc
•Tokenize the data
•Pad dataset
•Create the data loaders
•Use glove embedding to encode the data
•Pass the data to LSTM block, to get next cell state
•Pass through attention layer with a step size of 50 to get masked output
•Flatten the masked output and pass through the softmax layer

![image](https://user-images.githubusercontent.com/54845581/117645443-3b278580-b1a8-11eb-8561-a10732e81900.png)


## Authors

* **Pramil Panjawani** 
* **Vikas Balki**
* **Kriti Poddar**
* **Apratim Ankit**
* **Suverna Bisht**

## References

[1] Shen, G., Jia, J., Nie, L., Feng, F., Zhang, C., Hu, T., Chua, T.-S. and Zhu, W. 2017. Depression Detection via Harvesting Social Media: A Multimodal Dictionary Learning Solution. (2017), 3838–3844.

